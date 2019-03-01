from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
import psycopg2
import json

from services import ItemService
from infrastructure.exceptions import InvalidModel, ModelConflict
from db import Session

database_env = {
    "user": os.environ['PG_USERNAME'],
    "password": os.environ['PG_PASSWORD'],
    "host": os.environ['PG_HOST'],
    "database": os.environ['PG_DATABASE']
}

print("THIS IS THE ROOT")
DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}/{database}'.format(**database_env)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)

@app.route("/api/user/<username>")
def user(username):
    admin = User(username=username, email=username + '@meowtron.com')
    db.session.add(admin)
    db.session.commit()
    print(User.query.all())
    return 'OK'

@app.route("/api/test")
def test():
    with open('fake.json') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route("/api/items", methods=["POST"])
def add_item():
    session = Session()
    service = ItemService(session)

    item_params = {
        'name': request.json['name'],
        'status': request.json['status'],
        'type': request.json['type']
    }

    item = None
    status = 201
    try:
        item = service.save(item_params)
    except InvalidModel as e:
        return Response(data=json.dumps(e.errors), status=400)
    except ModelConflict as e:
        item = e.model
        status = 409
    
    json_response = json.dumps({
        'id': item.attrs['id'],
        'name': item.attrs['name'],
        'status': item.attrs['status'],
        'type': item.attrs['type']
    })

    session.commit()
    session.close()
    return Response(json_response, status=status)
    

@app.route("/healthz")
def healthz():
    return 'OK'

if __name__ == "__main__":
    print("THIS IS THE __MAIN__")
    app.run()
    