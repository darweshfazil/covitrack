import psycopg2

# Update connection string information
host = "agada-s1.postgres.database.azure.com"
dbname = "postgres"
user = "agada@agada-s1"
password = "Password123$"
sslmode = "require"


conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
#cursor.execute("create table prescriptions(pid int,id int,name varchar(50),timings varchar(50),quantity int,date varchar(50))")

#cursor.execute("CREATE TABLE personal(id int ,name varchar(50),age int,dob varchar(50),image varchar(50),gender varchar(50),phone varchar(50),email varchar(50),guardian varchar(50),address varchar(50));")
#cursor.execute("create table history(pid int,name varchar(50),blood varchar(50),weight int,height int,temp int,status varchar(50),vaccinated varchar(50),location varchar(50))")
#prescriptions
# cursor.execute("create table homeq(pid int,location varchar(50),latitude varchar(50),longitude varchar(50))")
# cursor.execute("create table dailyscore(pid int,date varchar(50),score int)")
# cursor.execute("create table emergencies(pid int,name varchar(50),age int,area varchar(50),date varchar(50),time varchar(50),status varchar(50))")
# cursor.execute("create table inpatient(pid int,ward varchar(50),room int,bed int)")


cursor.execute("update personal set image='https://www.cheatsheet.com/wp-content/uploads/2021/10/Penn-Badgley.jpg' where id=1")
cursor.close()
conn.commit()