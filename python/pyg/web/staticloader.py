import os
import pkgutil
import sys
import weakref
from types import ModuleType
from os import path
from hashlib import sha1
from jinja2.exceptions import TemplateNotFound
from jinja2.utils import open_if_exists, internalcode
from jinja2._compat import string_types, iteritems, fspath, abc

class BaseLoader(object):
    """Baseclass for all loaders.  Subclass this and override `get_source` to
    implement a custom loading mechanism.  The environment provides a
    `get_template` method that calls the loader's `load` method to get the
    :class:`Template` object.
    A very basic example for a loader that looks up templates on the file
    system could look like this::
        from jinja2 import BaseLoader, TemplateNotFound
        from os.path import join, exists, getmtime
        class MyLoader(BaseLoader):
            def __init__(self, path):
                self.path = path
            def get_source(self, environment, template):
                path = join(self.path, template)
                if not exists(path):
                    raise TemplateNotFound(template)
                mtime = getmtime(path)
                with file(path) as f:
                    source = f.read().decode('utf-8')
                return source, path, lambda: mtime == getmtime(path)
    """

    #: if set to `False` it indicates that the loader cannot provide access
    #: to the source of templates.
    #:
    #: .. versionadded:: 2.4
    has_source_access = True

    def get_source(self, environment, template):
        """Get the template source, filename and reload helper for a template.
        It's passed the environment and template name and has to return a
        tuple in the form ``(source, filename, uptodate)`` or raise a
        `TemplateNotFound` error if it can't locate the template.
        The source part of the returned tuple must be the source of the
        template as unicode string or a ASCII bytestring.  The filename should
        be the name of the file on the filesystem if it was loaded from there,
        otherwise `None`.  The filename is used by python for the tracebacks
        if no loader extension is used.
        The last item in the tuple is the `uptodate` function.  If auto
        reloading is enabled it's always called to check if the template
        changed.  No arguments are passed so the function must store the
        old state somewhere (for example in a closure).  If it returns `False`
        the template will be reloaded.
        """
        if not self.has_source_access:
            raise RuntimeError('%s cannot provide access to the source' %
                               self.__class__.__name__)
        raise TemplateNotFound(template)

    def list_templates(self):
        """Iterates over all templates.  If the loader does not support that
        it should raise a :exc:`TypeError` which is the default behavior.
        """
        raise TypeError('this loader cannot iterate over all templates')

    @internalcode
    def load(self, environment, name, globals=None):
        """Loads a template.  This method looks up the template in the cache
        or loads one by calling :meth:`get_source`.  Subclasses should not
        override this method as loaders working on collections of other
        loaders (such as :class:`PrefixLoader` or :class:`ChoiceLoader`)
        will not call this method but `get_source` directly.
        """
        code = None
        if globals is None:
            globals = {}

        # first we try to get the source for this template together
        # with the filename and the uptodate function.
        source, filename, uptodate = self.get_source(environment, name)

        # try to load the code from the bytecode cache if there is a
        # bytecode cache configured.
        bcc = environment.bytecode_cache
        if bcc is not None:
            bucket = bcc.get_bucket(environment, name, filename, source)
            code = bucket.code

        # if we don't have code so far (not cached, no longer up to
        # date) etc. we compile the template
        if code is None:
            code = environment.compile(source, name, filename)

        # if the bytecode cache is available and the bucket doesn't
        # have a code so far, we give the bucket the new code and put
        # it back to the bytecode cache.
        if bcc is not None and bucket.code is None:
            bucket.code = code
            bcc.set_bucket(bucket)

        return environment.template_class.from_code(environment, code,
                                                    globals, uptodate)

class PackageLoader(BaseLoader):
    """Load templates from a directory in a Python package.
    :param package_name: Import name of the package that contains the
        template directory.
    :param package_path: Directory within the imported package that
        contains the templates.
    :param encoding: Encoding of template files.
    The following example looks up templates in the ``pages`` directory
    within the ``project.ui`` package.
    .. code-block:: python
        loader = PackageLoader("project.ui", "pages")
    Only packages installed as directories (standard pip behavior) or
    zip/egg files (less common) are supported. The Python API for
    introspecting data in packages is too limited to support other
    installation methods the way this loader requires.
    .. versionchanged:: 2.11.0
        No longer uses ``setuptools`` as a dependency.
    """

    def __init__(self, package_name, package_path="static", encoding="utf-8"):
        if package_path == os.path.curdir:
            package_path = ""
        elif package_path[:2] == os.path.curdir + os.path.sep:
            package_path = package_path[2:]

        package_path = os.path.normpath(package_path)

        self.package_name = package_name
        self.package_path = package_path
        self.encoding = encoding

        self._loader = pkgutil.get_loader(package_name)
        # Zip loader's archive attribute points at the zip.
        self._archive = getattr(self._loader, "archive", None)
        self._template_root = os.path.join(
            os.path.dirname(self._loader.get_filename(package_name)), package_path
        ).rstrip(os.path.sep)

    def get_source(self, environment, template):
        p = os.path.join(self._template_root, *split_template_path(template))

        if self._archive is None:
            # Package is a directory.
            if not os.path.isfile(p):
                raise TemplateNotFound(template)

            with open(p, "rb") as f:
                source = f.read()

            mtime = os.path.getmtime(p)

            def up_to_date():
                return os.path.isfile(p) and os.path.getmtime(p) == mtime
        else:
            # Package is a zip file.
            try:
                source = self._loader.get_data(p)
            except OSError:
                raise TemplateNotFound(template)

            # Could use the zip's mtime for all template mtimes, but
            # would need to safely reload the module if it's out of
            # date, so just report it as always current.
            up_to_date = None

        return source.decode(self.encoding), p, up_to_date

    def list_templates(self):
        results = []

        if self._archive is None:
            # Package is a directory.
            offset = len(self._template_root)

            for dirpath, _, filenames in os.walk(self._template_root):
                dirpath = dirpath[offset:].lstrip(os.path.sep)
                results.extend(
                    os.path.join(dirpath, name).replace(os.path.sep, "/")
                    for name in filenames
                )
        else:
            if not hasattr(self._loader, "_files"):
                raise TypeError(
                    "This zip import does not have the required"
                    " metadata to list templates."
                )

            # Package is a zip file.
            prefix = (
                self._template_root[len(self._archive):].lstrip(os.path.sep)
                + os.path.sep
            )
            offset = len(prefix)

            for name in self._loader._files.keys():
                # Find names under the templates directory that aren't directories.
                if name.startswith(prefix) and name[-1] != os.path.sep:
                    results.append(name[offset:].replace(os.path.sep, "/"))

        results.sort()
        return results
