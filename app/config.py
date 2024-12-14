import os

class Config:
    SECRET_KEY = 'your_secret_key'
    UPLOAD_FOLDER = os.path.join('app', 'web', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max dosya boyutu: 16 MB