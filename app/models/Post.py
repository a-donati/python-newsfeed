from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property
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
  # Raw SQL Query of vote_count:
# SELECT COUNT(votes.id) AS vote_count FROM votes WHERE votes.post_id = 1;
  vote_count = column_property(
  select([func.count(Vote.id)]).where(Vote.post_id == id)
)
  user = relationship('User')
  #   query for Post returns comments associated with it
  comments = relationship('Comment', cascade='all,delete')
#   ON DELETE CASCADE - delete corresponding foreign key records when record is deleted - deleting a post will delete associated comments
  votes = relationship('Vote', cascade='all,delete')
#   on delete ^ remove associates votes