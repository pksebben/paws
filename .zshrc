export PYTHONPATH=`pwd`/python

source /home/coffee/.virtualenvs/pyg/bin/activate

function unmagic() {
    deactivate
    unset PYTHONPATH
    export PYTHONPATH
}
