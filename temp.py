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

#write personal information
def addPersonalToDB(pid,name,image,dob,age,gender,phone,email,guardian,address):
    cursor = getCon()
    cursor.execute("INSERT INTO personal values(%d,%s,%d,%s,%s,%s,%s,%s,%s,%s)",(pid,name,age,dob,image,gender,phone,email,guardian,address))

#add covid addHistory
def addHistoryToDB(pid,name,blood,height,weight,vaccinated,temperature,cstatus,location):
    cursor = getCon()
    cursor.execute("INSERT INTO history values(%d,%s,%s,%d,%d,%d,%s,%s,%s)",(pid,name,blood,weight,height,temperature,cstatus,vaccinated,location))

#add homeq
def addHomeToDB(pid,name,latitude,longitude):
    cursor = getCon()
    cursor.execute("INSERT INTO homeq values(%d,%s,%s,%s)",(pid,name,latitude,longitude))
#add hospital
def addHospitalToDB(pid,ward,room,bed):
    cursor = getCon()
    cursor.execute("INSERT INTO inpatient values(%d,%s,%d,%d)",(pid,ward,room,bed))

#add prescription to db
def addPrescriptionToDb(pid,pres_id,name,timings,quantity,date):
    cursor = getCon()
    cursor.execute("INSERT INTO prescriptions values(%d,%d,%s,%s,%d,%s)",(pid,pres_id,name,timings,quantity,date))

#add emergency to db
def addEmergencyToDB(pid,name,age,area,date,time,status):
    cursor = getCon()
    cursor.execute("INSERT INTO emergencies values(%d,%s,%d,%s,%s,%s,%s)",(pid,name,age,area,date,time,status))


#add daily to db
def addDailyScoreToDB(pid,date,score):
    cursor = getCon()
    cursor.execute("INSERT INTO dailyscore values(%d,%s,%d)",(pid,date,score))

#api routes 
@app.route('/api/addPersonal',methods=['POST'])
def addPersonal():
    pid=request.form['id']
    name=request.form['name']
    image=request.form['image']
    dob=request.form['dob']
    age=request.form['age']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    guardian=request.form['guardian']
    address=request.form['address']
    print(type(pid))
    print(int(pid),name,image,dob,int(age),gender,phone,email,guardian,address)
    return redirect(url_for('addpatient'))

@app.route('/api/addHistory',methods=['POST'])
def addHistory():
    pid=request.form['id']
    name=request.form['name']
    blood=request.form['blood']
    height=request.form['height']
    weight=request.form['weight']
    vaccinated=request.form['vaccine']
    temperature=request.form['temp']
    cstatus=request.form['cstatus']
    location=request.form['location']
    print(int(pid),name,blood,int(height),int(weight),vaccinated,int(temperature),cstatus,location)
    return redirect(url_for('addpatient'))

@app.route('/api/addHome',methods=['POST'])
def addHome():
    pid=request.form['id']
    name=request.form['name']
    latitude=request.form['latitude']
    longitude=request.form['longitude']
    print(int(pid),name,latitude,longitude)
    return redirect(url_for('addpatient'))

@app.route('/api/addHospital',methods=['POST'])
def addHospital():
    pid=request.form['id']
    ward=request.form['ward']
    room=request.form['room']
    bed=request.form['bed']
    print(int(pid),ward,int(room),int(bed))
    return redirect(url_for('addpatient'))

@app.route('/api/addPrescription',methods=['POST'])
def addPrescription():
    pid=request.form['pid']
    pres_id=request.form['id']
    name=request.form['name']
    timings=request.form['timings']
    quantity=request.form['quantity']
    date=request.form['date']
    print(int(pid),int(pres_id),name,timings,int(quantity),date)
    return redirect(url_for('addpatient'))

@app.route('/api/addEmergency',methods=['POST'])
def addEmergency():
    data=request.get_json()
    pid=int(data["pid"])
    name=data["name"]
    age=int(data["age"])
    area=data["area"]
    date=data["date"]
    time=data["time"]
    status=data["status"]
    print(pid,name,age,area,date,time,status)

@app.route('/api/addDailyScore',methods=['POST'])
def addDailyScore():
    data=request.get_json()
    pid=int(data["pid"])
    date=data["date"]
    score=int(data["score"])
    
    print(pid,date,score)

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