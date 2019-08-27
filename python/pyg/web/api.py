import flask
import werkzeug.exceptions
from .models import Person, UserAuth, UserProfile, Org, OrgMembership, Fundraiser
from sqlwizardry import SQLAlchemy

bp = flask.Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/')
def index():
    """Return api description."""
    return "TODO:api"


