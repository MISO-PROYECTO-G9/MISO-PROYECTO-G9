from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

from src.health.api.health import health

app.register_blueprint(health, url_prefix='/health')

app.config['JWT_SECRET_KEY'] = 'frase-secreta'


def gunicorn():
    return app


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=3000, debug=True
    )

jwt = JWTManager(app)
