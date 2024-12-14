from flask import Flask
from web import web_bp
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Config dosyasını ekle

    # Blueprint'i kaydet
    app.register_blueprint(web_bp, url_prefix='/')

    # Upload klasörünü oluştur
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    return app