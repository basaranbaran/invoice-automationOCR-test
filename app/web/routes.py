from flask import render_template
from . import web_bp


# Blueprint route'ları
@web_bp.route('/')
def home():
    return render_template('base.html')  # Genel kullanılan base.html burada çağrılıyor


@web_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    return render_template('upload.html')  # upload.html genel bir şablon olarak çağrılıyor
