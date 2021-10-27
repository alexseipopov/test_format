from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators, RecaptchaField
from wtforms import StringField
from wtforms.fields.core import IntegerField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class PersonalForm(FlaskForm):
    


    

    first_name = StringField('your name', render_kw={'value': 'll'})
    last_name = StringField('Your last name')
    city = StringField('your city')
    age = IntegerField('your age')


