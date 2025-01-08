from flask import Flask
from app.web import web_bp  # web blueprint'i burada import edilmiş olmalı
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Config dosyasını yükle

    # Blueprint'i kaydet
    app.register_blueprint(web_bp, url_prefix='/')

    # Upload klasörünü oluştur
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    return app

