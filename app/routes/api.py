from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db
import sys
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
    print(sys.exe_info()[0])
    # insert failed, so rollback and send error to front end
  db.rollback()
  return jsonify(message = 'Signup failed'), 500

# An AssertionError is thrown when our custom validations fail. An IntegrityError is thrown when something specific to MySQL (like a UNIQUE constraint) fails.
  return jsonify(id = newUser.id)