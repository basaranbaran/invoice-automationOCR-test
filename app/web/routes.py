import os
from flask import render_template, Blueprint, flash, request, redirect, url_for, current_app

# Blueprint tanımlıyoruz
web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static')


def allowed_file(filename):
    """İzin verilen dosya uzantılarını kontrol eder."""
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@web_bp.route('/')
def index():
    """Ana sayfa."""
    return render_template('base.html')


@web_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Dosya yükleme fonksiyonu"""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Dosya bulunamadı.')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('Dosya seçilmedi.')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Filename ve kaydedileceği yolun belirlenmesi
            filename = file.filename
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            # Dosyanın belirtilen klasöre kaydedilmesi
            file.save(upload_path)

            flash(f"{filename} başarıyla yüklendi!")
            return redirect(url_for('web.index'))

        flash('İzin verilmeyen dosya türü!')
        return redirect(request.url)

    return render_template('upload.html')