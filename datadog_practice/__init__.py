from flask import Flask, render_template

from datadog_practice.main import main


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    app.register_blueprint(main, url_prefix='/main')

    return app
