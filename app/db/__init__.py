from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# load_dotenv() from python-dotenv module
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# temp connections for CRUD operations
Session = sessionmaker(bind=engine)
# map models to MySQL tables
Base = declarative_base()