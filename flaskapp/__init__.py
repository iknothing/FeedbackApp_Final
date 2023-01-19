from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    newpath = os.path.join(basedir, 'worksheets')
    newpath1 = os.path.join(basedir, 'images')
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if not os.path.exists(newpath1):
        os.mkdir(newpath1)
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user.db')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app
app=create_app()
app.app_context().push()
db.create_all()

