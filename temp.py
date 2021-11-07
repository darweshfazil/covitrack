from flask import Flask, render_template , request,jsonify,redirect,url_for
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
@app.route('/')

def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return redirect(url_for('home'))

@app.route('/medicalhistory')
def history():
    return render_template('medicalhistory.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/prescription')
def prescription():
    return render_template('prescription.html')

@app.route('/addpatient')
def addpatient():
    return render_template('addpatient.html')

@app.route('/patientinfo')
def patientinfo():
    return render_template('patientinfo.html')

if __name__ == '__main__':
    app.run(debug=True)