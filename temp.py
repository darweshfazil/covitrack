from flask import Flask, render_template , request,jsonify
import psycopg2
app = Flask(__name__)

#api for postgres covitrack
host = "agada-s1.postgres.database.azure.com"
dbname = "postgres"
user = "agada@agada-s1"
password = "Password123$"
sslmode = "require"

#DB functions
#DB connection
def getCon():
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()
    return cursor



#routes
def home():
    return render_template('index.html')