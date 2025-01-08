# web/__init__.py
from flask import Blueprint

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
def home():
    return "Hello from web module"