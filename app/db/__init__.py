from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g
# implement Application Context from Flask. 

# load_dotenv() from python-dotenv module
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# temp connections for CRUD operations
Session = sessionmaker(bind=engine)
# map models to MySQL tables
Base = declarative_base()
# call init_db when flask app ready 
def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db)
  # return new session connection object - other modules can import the session from db
# run app.teardown when context is destroyed
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()
    # return current connection object from g instead of creating new session
  return g.db
# close connection
def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()
# return new session connection object
def get_db():
  return Session()