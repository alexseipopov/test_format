from flask import Flask, render_template
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY']='83fb6dabd51d8e022dd9a59b4f9f3079eecb7b8f'
app.config['RECAPTCHA_PUBLIC_KEY']='6LdGYJ0cAAAAAIpekcs--P6f3t7l_9SmHt97iEMw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = LoginManager(app)
manager.login_view = 'index'

from .logreg import logreg as lr_bp
app.register_blueprint(lr_bp)


from .admin import admin as admin_bp
app.register_blueprint(admin_bp)

from .personalpage import pp
app.register_blueprint(pp)

from .panda_boss import pandaboss
app.register_blueprint(pandaboss)

from ._socialnet import views
