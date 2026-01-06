import psycopg2 as psy

conn=psy.connect(dbname='Student',user='postgres',password='shannu..',host='localhost')

if conn:
    print("Connected")
else:
    print("Connection error")

curr=conn.cursor()

curr.execute(
    """
    create table IF NOT EXISTS students1(
    srn SERIAL primary key,
    s_name VARCHAR(20) NOT NULL,
    Python integer NOT NULL,
    DS integer NOT NULL,
    SE integer NOT NULL,
    OS integer NOT NULL,
    Java integer NOT NULL,
    PD integer NOT NULL
    );
    """)
conn.commit()
print("Table Created Successfully.")

curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Jane', 85, 78, 80, 75, 88, 90)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Steve', 65, 68, 46, 71, 50, 64)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Jonathan', 55, 76, 43, 94, 67, 60)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Dustin', 60, 97, 67, 89, 78, 54)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Max', 39, 39, 52, 39, 44, 50)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Lucas', 88, 69, 70, 51, 84, 52)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Will', 89, 73, 96, 39, 47, 75)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Erika', 77, 97, 58, 94, 88, 35)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Henry', 65, 68, 46, 71, 50, 64)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Nancy', 55, 76, 43, 94, 67, 60)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Eddi', 60, 97, 67, 89, 78, 54)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Billy', 39, 39, 52, 39, 44, 50)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Mike', 88, 69, 70, 51, 84, 52)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Jim', 89, 73, 96, 39, 47, 75)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Joyce', 77, 97, 58, 94, 88, 35)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Robin', 39, 39, 52, 39, 44, 50)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Suzie', 88, 69, 70, 51, 84, 52)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Brett', 89, 73, 96, 39, 47, 75)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Holly', 77, 97, 58, 94, 88, 35)""")
curr.execute("""INSERT INTO students1(s_name, Python, DS, SE, OS, Java, PD)VALUES('Dr.Kay', 65, 68, 46, 71, 50, 64)""")
conn.commit()
print("Data inserted successfully.")

# curr.execute("DELETE FROM students1")

# curr.execute("SELECT * from students1")
# rows=curr.fetchall()
# conn.commit()
# for row in rows:
#     print(row)
curr.close()

conn.close()