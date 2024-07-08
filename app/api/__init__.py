from flask import Blueprint

from app.api import routes

api_bp = Blueprint("api", __name__)
