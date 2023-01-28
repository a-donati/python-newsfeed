from flask import Flask
from app.routes import home, dashboard, api
# import our app routes from routes folder
from app.db import init_db
# import init_db func
from app.utils import filters
# import filter functions

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path="/")
    app.url_map.strict_slashes = False
    app.config.from_mapping(SECRET_KEY="super_secret_key")
    # any routes defined in api.py module will automatically become part of flask app and have the prefix of /api
    app.register_blueprint(api)
    @app.route("/hello")
    def hello():
        return "hello world"

    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    # initialize db
    init_db(app)
    # init_db()
    # complete registration of filters
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    return app