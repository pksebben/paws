import flask
import werkzeug.exceptions
from .models import Person, UserAuth, UserProfile, Org, OrgMembership, Fundraiser

bp = flask.Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/')
def index():
    """Return api description."""
    return "TODO:api"


