from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# creates any tables that Base mapped, in a class that inherits Base (like User)