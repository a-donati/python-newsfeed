from app.db import Base
# map models to MySQL tables
from sqlalchemy import Column, Integer, String
# create User class that inherits Base class
# declare several properties that parent Base class will use
# to make the table
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)