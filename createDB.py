import os
import psycopg2

database_env = {
    "user": os.environ['PG_USERNAME'],
    "password": os.environ['PG_PASSWORD'],
    "host": os.environ['PG_HOST'],
    "database": os.environ['PG_DATABASE']
}

# Create database
con = psycopg2.connect(dbname='postgres',
	                   user=database_env["user"], 
                       host=database_env["host"],
                       password=database_env["password"])

con.autocommit = True
cur = con.cursor()
#cur.execute('CREATE DATABASE "{}";'.format(database_env["database"]))
try:
    cur.execute('CREATE DATABASE {};'.format(database_env["database"]))
except psycopg2.ProgrammingError as e:
    print("Database {} probably already exists".format(database_env["database"]))
    pass