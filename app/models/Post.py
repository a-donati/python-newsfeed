from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

# write SQLAlchemy models as Python classes
class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
#   foreign key
  user_id = Column(Integer, ForeignKey('users.id'))
#   use built in Python datetime module to generate timestamps
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  user = relationship('User')
  #   query for Post returns comments associated with it
  comments = relationship('Comment', cascade='all,delete')
#   ON DELETE CASCADE - delete corresponding foreign key records when record is deleted - deleting a post will delete associated comments