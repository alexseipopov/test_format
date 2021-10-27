from flask_login.utils import login_required
from .. import admin
from ...database import db
from ...database.models import Users, Personal
from flask import render_template, redirect, url_for

@admin.route('/')
def index():
    users_data = Users.query.order_by()
    return render_template("admin.html", user_table = users_data)

@admin.route('/back')
def back():
    return redirect(url_for('admin.index'))

@admin.route('/go')
def go():
    return redirect(url_for('logreg.index'))