from flask import Blueprint

pandaboss = Blueprint('pandaboss', __name__, url_prefix='/panda_boss', template_folder='templates')

from .profile import views