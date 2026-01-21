import psycopg2 as psy

conn=psy.connect(dbname="College",user="postgres",password="shannu..",host="localhost")

if conn:
    print("connection successful")
else:
    print("connection failed.")

curr=conn.cursor() #cursor creation
curr.execute("""
        Create table IF NOT EXISTS students1 (
            student_id SERIAL primary key,
            student_name Varchar(50)NOT NULL,
            grade varchar(10) NOT NULL,
            section VARCHAR(10) NOT NULL);
    """)
print("Table created.")
conn.commit()
curr.execute("Insert into students1 VALUES(DEFAULT,'shannu', 'A' , 'D')")
conn.commit()
curr.execute('Select * from students1')
rows=curr.fetchall()
conn.commit()
for row in rows:
    # print(*row) #we use * to remove
    print(" ".join(map(str,row))) #removing the parantehsis using map
    
conn.close()
curr.close()