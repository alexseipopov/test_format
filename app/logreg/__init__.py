
from flask import Blueprint

logreg = Blueprint('logreg', __name__, template_folder='templates', url_prefix='/auth')

from .profile import views