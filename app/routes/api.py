from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db
# establish api blueprint
bp = Blueprint('api', __name__, url_prefix='/api')

# route will resolve to - /api/users - POST route
@bp.route('/users', methods=['POST'])

def signup():
  data = request.get_json()
  db = get_db()

  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )
  # save in database - prep INSERT statement
    db.add(newUser)
    db.commit()
  except:
    # insert failed, so send error to front end
    return jsonify(message = 'Signup failed'), 500

  return jsonify(id = newUser.id)