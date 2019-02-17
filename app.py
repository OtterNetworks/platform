from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

database_env = {
    "user": os.environ['PG_USERNAME'],
    "password": os.environ['PG_PASSWORD'],
    "host": os.environ['PG_HOST'],
    "database": os.environ['PG_DATABASE']
}

# Create database
con = psycopg2.connect(user=database_env["user"], 
                       host=database_env["host"],
                       password=database_env["password"])
con.autocommit = True
cur = con.cursor()
try:
    cur.execute('CREATE DATABASE {};'.format(database_env["database"]))
except:
	print("Database {} already exists".format(database_env["database"]))

DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}/{database}'.format(**database_env)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/api/user/<username>")
def hello(username):
    admin = User(username=username, email=username + '@meowtron.com')
    db.session.add(admin)
    db.session.commit()
    print(User.query.all())
    return 'OK'

@app.route("/healthz")
def healthz():
    return 'OK'

if __name__ == "__main__":
    db.create_all()
    app.run()


