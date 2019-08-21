import flask
import werkzeug.exceptions

bp = flask.Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/')
def index():
    """Return api description."""
    return "TODO:api"


