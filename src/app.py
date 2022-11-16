import imp
from flask import Flask
from extensions import db, migrate, csrf
from blueprint.album import album_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia'
app.config['SQLALCHEMY_DATABASE_URI']= ''



db.init_app(app)
migrate.init_app(app=app, db=db)
csrf.init_app(app)


app.register_blueprint(album_blueprint)

if __name__ == '__main__':
    app.run(debug=True)