from flask import Blueprint

web_bp = Blueprint('web', __package__)
from app.web import book