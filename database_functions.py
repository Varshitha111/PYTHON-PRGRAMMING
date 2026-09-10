
import psycopg2

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_wV2Qr7TWOebM@ep-cool-breeze-aen9dkik-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)
cur = conn.cursor() 

create_table=""" create table if not exists students_new(id int primary key,name varchar(50),age float)"""
cur.execute(create_table)
conn.commit()
def validate_input(entry):
    if len(entry)!=3:
        print("need 3 entries")
        return
    id_value=entry[0]
    name_value=entry[1]
    age_value=entry[2]
    try:
        id_value=int(id_value)
    except ValueError:
        print("id was not an integer")
    try:
        age_value=float(age_value)
    except ValueError:
        print("age was not a valid number should be in float format")
        return
    
def check_user(entry):
    id_value=entry[0]
    name_value=entry[1]
    age_value=entry[2]
    cur.execute("select * from students_new where id=%s",(id_value,))
    data=cur.fetchall()
    if len(data)>0:
        print("id already exists")
        return
def insert_data(entry):
    id_value=entry[0]
    name_value=entry[1]
    age_value=entry[2]
    cur.execute("insert into students_new values(%s,%s,%s)",(id_value,name_value,age_value))
    conn.commit()
    print("inserted successfully")
        
for i in range(3):
    entry=input(f"Enter details for student {i+1} (ID Name Age): ").split()
    validate_input(entry)
    check_user(entry)
    insert_data(entry)
cur.execute("select * from students_new")
for row in cur.fetchall():
    print(row)
    