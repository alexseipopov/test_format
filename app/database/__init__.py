from flask_sqlalchemy import SQLAlchemy
from .. import app

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
