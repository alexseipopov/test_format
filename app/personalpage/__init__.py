from flask import Blueprint

pp = Blueprint('pp', __name__, url_prefix='/profile', template_folder='templates')

from .profile import views