from flask.helpers import url_for
from werkzeug.utils import redirect

from .forms import PersonalForm
from ...database import db
from .. import pp
from flask import render_template
from flask_login.utils import login_required
from flask_login import current_user
from ...database.models import Users, Personal

@pp.route('/id_<int:id>')
def personalpage(id):
    user = Users.query.filter_by(id=id).first()
    data = Personal.query.filter_by(fk_user_id = id).first()
    check = False
    if current_user.id == id:
        check = True
    return render_template('personalpage.html', user=user, data=data, check = check, title = 'Profile')
    # return 'Personal page of id: {}; username: {}'.format(id, current_user.username)

@pp.route('/edit', methods=['post', 'get'])
@login_required
def edit():
    # if current_user.id != id:
    #     return redirect(url_for('edit', id = current_user.id))
    personal = Personal.query.filter_by(fk_user_id = current_user.id).first()
    print('found user')
    print(personal)
    form = PersonalForm()
    print('created form')
    if form.validate_on_submit():
        print('i dont have to be here')
        personal.first_name = form.first_name.data
        personal.last_name = form.last_name.data
        db.session.commit()
        return redirect(url_for('pp.personalpage', id = current_user.id))
    return render_template('personal_data.html', form=form, title = 'Edit', db=Users.query.filter_by(username='bear'))
    