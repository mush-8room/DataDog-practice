from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/page1')
def page1():
    return render_template('main/page1.html')


@main.route('/page2')
def page2():
    return render_template('main/page2.html')
