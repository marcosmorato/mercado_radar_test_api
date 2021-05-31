from backend.services.request_coin import request_coin

from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"], strict_slashes=False)
    def get():
        return request_coin()

    return app
