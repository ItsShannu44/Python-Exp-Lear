import psycopg2 as psy

conn=psy.connect(dbname="College",user='postgres',password='shannu..',host='localhost',port='5432')

if conn:
    print("Connection successfull.")
else:
    print("Conn Error.")

curr=conn.cursor() #create and open cursor

#---------Create a table-----------

# curr.execute(
#     """
#     create table students(
#     srn SERIAL PRIMARY KEY,
#     student_name VARCHAR(80)NOT NULL,
#     semister VARCHAR(10)NOT NULL,
#     section VARCHAR(2)NOT NULL
#     );
#     """)

# conn.commit()

#-------------------INSERTION-------------------------

# curr.execute("Insert into students(srn,student_name,semister,section) VALUES('197','GAMORA','sem 1','A')")
# curr.execute("Insert into students(srn,student_name,semister,section) VALUES('198','DRAX','sem 1','A')")
# curr.execute("Insert into students(srn,student_name,semister,section) VALUES('199','NEBULA','sem 1','B')")
# curr.execute("Insert into students(srn,student_name,semister,section) VALUES('200','MANTIS','sem 1','B')")

#-------------------

curr.execute("Select * from students")
rows=curr.fetchall()

conn.commit()


curr.close()
conn.close()

for row in rows :
    print(row)





conn=psy.connect(dbname="College",user='postgres',password='shannu..',host='localhost',port='5432')

if conn:
    print("Connection successfull.")
else:
    print("Conn Error.")

curr=conn.cursor()
curr.execute("UPDATE students SET student_name='ROCKET' where srn=197")

conn.commit()
curr.close()
conn.close()
