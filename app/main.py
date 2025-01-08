from flask import Flask
from flask_cors import CORS
from app.web.routes import web_bp
from config import DevelopmentConfig
import os
from app.make_celery import make_celery

def create_app():
    """Flask application factory."""
    app = Flask(__name__, static_folder='static')

    # CORS configuration
    CORS(app)

    # Load configuration
    app.config.from_object(DevelopmentConfig)

    # Celery configuration
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )
    celery = make_celery(app)

    # Create upload directory
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprint
    app.register_blueprint(web_bp)

    return app, celery

app, celery = create_app()

if __name__ == '__main__':
    app.run(port=5002, debug=True)
