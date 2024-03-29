from flask import Blueprint, render_template, session, redirect
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
  posts=posts,
  loggedIn=session.get('loggedIn')
)

@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')
  

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  # filter post by id
  post = db.query(Post).filter(Post.id == id).one()

  # render single post to template
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )