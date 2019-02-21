import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_env = {
    "user": os.environ['PG_USERNAME'],
    "password": os.environ['PG_PASSWORD'],
    "host": os.environ['PG_HOST'],
    "database": os.environ['PG_DATABASE']
}

db_url = "postgresql://{user}:{password}@{host}/{database}".format(**database_env)

engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)