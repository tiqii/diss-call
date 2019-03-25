from flask import render_template
from . import main


@main.route('/')
def index():
    """ index路由 """
    return render_template('index.html')
