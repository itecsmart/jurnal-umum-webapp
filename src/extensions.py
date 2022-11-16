from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = basedir+'/static/media/'