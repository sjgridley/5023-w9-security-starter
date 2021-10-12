from flask import Blueprint

bp = Blueprint('animal', __name__, template_folder='templates')

from app.animal import routes