from flask import Blueprint, render_template
# # import Blueprint and render_template from flask
bp = Blueprint('home', __name__, url_prefix='/')
# # consolidate single routes to bp object
from app.models import Post
from app.db import get_db

@bp.route('/')
def index():
  # get all posts - get_db() returns session connection
  db = get_db()
  # query posts
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
# return homepage template along with post data
  return render_template(
  'homepage.html',
  posts=posts
)

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')