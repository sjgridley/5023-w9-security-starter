from flask import Blueprint

bp = Blueprint('pet', __name__, template_folder='templates')

from app.pet import routes