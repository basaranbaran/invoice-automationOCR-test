from flask import Blueprint


# Blueprint tanımlama
web_bp = Blueprint('web', __name__)

# Routes dosyasını import et
from . import routes
