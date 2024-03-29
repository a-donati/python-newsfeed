from app.db import Base
# map models to MySQL tables
from sqlalchemy import Column, Integer, String
# create User class that inherits Base class
from sqlalchemy.orm import validates
# validates function decorator SQLAlchemy
import bcrypt
# import bcrypt for pw hashing

# before creating user:
salt = bcrypt.gensalt()

# declare several properties that parent Base class will use
# to make the table
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
# validate email
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email
    # validate password
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

    # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)
  def verify_password(self, password):
    return bcrypt.checkpw(
    password.encode('utf-8'),
    self.password.encode('utf-8')
    )