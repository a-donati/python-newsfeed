from flask import Blueprint, request
from app.models import User
from app.db import get_db
# establish api blueprint
bp = Blueprint('api', __name__, url_prefix='/api')

# route will resolve to - /api/users - POST route
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  print(data)

  return ''