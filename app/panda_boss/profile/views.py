from flask import render_template
from .. import pandaboss


@pandaboss.route('/')
def index():
    return render_template('pb_main.html')