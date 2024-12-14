from flask import Blueprint

# Blueprint'in adını tanımlayın
web_bp = Blueprint(
    'web',  # Blueprint ismi
    __name__,
    template_folder='templates',  # Blueprint'e özel templates dizini
    static_folder='static'  # Blueprint'e özel statik dosya dizini
)

# Route dosyasını Blueprint'e ilişkilendirin
from . import routes
