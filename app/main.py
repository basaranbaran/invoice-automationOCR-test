from flask import Flask
from flask_cors import CORS
from web.routes import web_bp
from config import DevelopmentConfig
import os


def create_app():
    """Flask uygulamasını kurar."""
    app = Flask(__name__, static_folder='static')

    # CORS yapılandırması
    CORS(app)

    # Config ayarları
    app.config.from_object(DevelopmentConfig)

    # Yükleme dizinini oluştur
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Blueprint kaydedin
    app.register_blueprint(web_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5001, debug=True)

