import os
from flask import Flask
from extensions import *
from models import *
from blueprint import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia'
app.config['SQLALCHEMY_DATABASE_URI']= \
    'sqlite:///' + os.path.join(basedir,'database.db')



db.init_app(app)
migrate.init_app(app=app, db=db)
csrf.init_app(app)
login_manager.init_app(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(jurnal_bp)


if __name__ == '__main__':
    app.run(debug=True)