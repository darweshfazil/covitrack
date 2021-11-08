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

def getConCurs():
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
   
    return conn

#write personal information
def addPersonalToDB(pid,name,image,dob,age,gender,phone,email,guardian,address):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO personal values({pid},'{name}',{age},'{dob}','{image}','{gender}','{phone}','{email}','{guardian}','{address}')".format(pid=pid,name=name,image=image,dob=dob,age=age,gender=gender,phone=phone,email=email,guardian=guardian,address=address)
    cursor.execute(query)
    conn.commit()
    return "done"

#add covid addHistory
def addHistoryToDB(pid,name,blood,height,weight,vaccinated,temperature,cstatus,location):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO history values({pid},'{name}','{blood}',{weight},{height},{temperature},'{cstatus}','{vaccinated}','{location}')".format(pid=pid,name=name,blood=blood,weight=weight,height=height,temperature=temperature,cstatus=cstatus,vaccinated=vaccinated,location=location)
    cursor.execute(query)
    cursor.close()
    conn.commit()

#add homeq
def addHomeToDB(pid,name,latitude,longitude):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO homeq values({pid},'{name}','{latitude}','{longitude}')".format(pid=pid,name=name,latitude=latitude,longitude=longitude)
    cursor.execute(query)
    conn.commit()
#add hospital
def addHospitalToDB(pid,ward,room,bed):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO inpatient values({pid},'{ward}',{room},{bed})".format(pid=pid,ward=ward,room=room,bed=bed)
    cursor.execute(query)
    conn.commit()

#add prescription to db
def addPrescriptionToDB(pid,pres_id,name,timings,quantity,date):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO prescriptions values({pid},{pres_id},'{name}','{timings}',{quantity},'{date}')".format(pid=pid,name=name,timings=timings,quantity=quantity,date=date,pres_id=pres_id)
    cursor.execute(query)
    conn.commit()

#add emergency to db
def addEmergencyToDB(pid,name,age,area,date,time,status):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO emergencies values({pid},'{name}',{age},'{area}','{date}','{time}','{status}')".format(pid=pid,name=name,age=age,area=area,date=date,time=time,status=status)
    cursor.execute(query)
    conn.commit()

#add daily to db
def addDailyScoreToDB(pid,date,score):
    conn = getConCurs()
    cursor =conn.cursor()
    query="INSERT INTO dailyscore values({pid},'{date}',{score})".format(pid=pid,date=date,score=score)
    cursor.execute(query)
    conn.commit()

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
    #print(type(pid))
    addPersonalToDB(int(pid),name,image,dob,int(age),gender,phone,email,guardian,address)
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
    addHistoryToDB(int(pid),name,blood,int(height),int(weight),vaccinated,int(temperature),cstatus,location)
    return redirect(url_for('addpatient'))

@app.route('/api/addHome',methods=['POST'])
def addHome():
    pid=request.form['id']
    name=request.form['name']
    latitude=request.form['latitude']
    longitude=request.form['longitude']
    addHomeToDB(int(pid),name,latitude,longitude)
    return redirect(url_for('addpatient'))

@app.route('/api/addHospital',methods=['POST'])
def addHospital():
    pid=request.form['id']
    ward=request.form['ward']
    room=request.form['room']
    bed=request.form['bed']
    addHospitalToDB(int(pid),ward,int(room),int(bed))
    return redirect(url_for('addpatient'))

@app.route('/api/addPrescription',methods=['POST'])
def addPrescription():
    pid=request.form['pid']
    pres_id=request.form['id']
    name=request.form['name']
    timings=request.form['timings']
    quantity=request.form['quantity']
    date=request.form['date']
    addPrescriptionToDB(int(pid),int(pres_id),name,timings,int(quantity),date)
    return redirect(url_for('addpatient'))



#mobile api
def checkUserInDB(id,email):
    cursor = getCon()
    cursor.execute("select id,name,age,address,image,gender from personal where id={id} and email='{email}'".format(id=id,email=email))
    data = cursor.fetchone()
    cursor.close()
    if len(data)==0:
        return {"status":False}
    else:
        print(data)

        return {"status":True,"id":data[0],"name":data[1],"age":data[2],"area":data[3],"image":data[4],"gender":data[5]}
    

@app.route('/api/addEmergency',methods=['POST'])
def addEmergency():
    data=request.get_json()
    pid=int(data["pid"])
    name=data["name"]
    age=int(data["age"])
    area=data["area"]
    date=data["date"]
    time=data["time"]
    status="pending"
    addEmergencyToDB(pid,name,age,area,date,time,status)
    return jsonify({"status":"success"})

@app.route('/api/addDailyScore',methods=['POST'])
def addDailyScore():
    data=request.get_json()
    pid=int(data["pid"])
    date=data["date"]
    score=int(data["score"])
    
    addDailyScoreToDB(pid,date,score)
    return jsonify({"status":"success"})

@app.route('/api/checkUser',methods=['POST'])
def checkUser():
    data=request.get_json()
    id=int(data['id'])
    email=data['email']
    return jsonify(checkUserInDB(id,email))

@app.route('/api/IndividualPrescription/<id>',methods=['GET'])
def getPrescription(id):
    print(id)
    cursor = getCon()
    query="SELECT * FROM prescriptions where id={id}".format(id=id)
    cursor.execute(query)
    data=cursor.fetchall()
    res={}
    lis=[]
    for i in data:
        obj={}
        obj['id']=i[0]
        obj['pid']=i[1]
        obj['name']=i[2]
        obj['timing']=i[3]
        obj['quantity']=i[4]
        obj['date']=i[5]
        lis.append(obj)
    
    
    return jsonify({"prescription":lis})

#testing api calls
@app.route('/api/allPatients',methods=['GET'])
def allPatients():
    cursor = getCon()
    query="SELECT * FROM personal"
    cursor.execute(query)
    data=cursor.fetchall()
    return jsonify(data)

@app.route('/api/allHistory',methods=['GET'])
def allHistory():
    cursor = getCon()
    query="SELECT * FROM history"
    cursor.execute(query)
    data=cursor.fetchall()
    return jsonify(data)


#routes
@app.route('/')

def home():
    cursor = getCon()
    query="SELECT personal.id,personal.name,personal.image,history.status FROM personal INNER JOIN history ON personal.id=history.pid"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    return render_template('index.html',data=data)
    

@app.route('/index')
def index():
    return redirect(url_for('home'))

@app.route('/medicalhistory')
def history():
    cursor = getCon()
    query="SELECT * FROM history INNER JOIN homeq ON history.pid=homeq.pid"
    cursor.execute(query)
    dataHome=cursor.fetchall()
    print(dataHome)
    query="SELECT * FROM history INNER JOIN inpatient ON history.pid=inpatient.pid"
    cursor.execute(query)
    dataIn=cursor.fetchall()
    print(dataIn)
    return render_template('medicalhistory.html',dataHome=dataHome,dataIn=dataIn)

@app.route('/emergency')
def emergency():
    cursor = getCon()
    query="SELECT * FROM emergencies"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    return render_template('emergency.html',data=data)
    

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/prescription')
def prescription():
    cursor = getCon()
    query="SELECT * FROM prescriptions"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    return render_template('prescription.html',data=data)
    

@app.route('/addpatient')
def addpatient():
    return render_template('addpatient.html')

@app.route('/patientinfo/<id>')
def addpatientid(id):
    cursor = getCon()
    query="SELECT personal.id,personal.name,personal.age,personal.gender,personal.image,personal.address,history.status,history.location FROM personal INNER JOIN history ON personal.id = history.pid where personal.id={id}".format(id=id)
    cursor.execute(query)
    pdata=cursor.fetchone()
    query="SELECT * FROM prescriptions where pid={id}".format(id=id)
    cursor.execute(query)
    pres=cursor.fetchone()
    query="SELECT * FROM dailyscore where pid={id}".format(id=id)
    cursor.execute(query)
    score=cursor.fetchall()
    print(pdata)
    print(pres)
    print(score)
    return render_template('patientinfo.html',pdata=pdata,pres=pres,score=score)

@app.route('/patientinfo')
def patientinfo():
    return render_template('patientinfo.html')

if __name__ == '__main__':
    app.run(debug=True)