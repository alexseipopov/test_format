from .. import app
from flask import render_template
from ..database.models import Users
from flask_login import login_required




@app.route('/')
def index():
    count = Users.query.count()
    return render_template('main.html', title = "Main", count = count)


@app.route('/private')
@login_required
def private():
    return 'Вы удачно зашли на приватную страничку, значит вы зарегистрированны'
