from flask import Blueprint, request, jsonify, session
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

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)
# An AssertionError is thrown when our custom validations fail. An IntegrityError is thrown when something specific to MySQL (like a UNIQUE constraint) fails.
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])
    # data['password'] becomes the second parameter in the verify_password() method of the class, because the first parameter is reserved for self
  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400
    # return message of incorrect credentials with 400 err
  session.clear()
  # send back valid response 
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)
