import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")

conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Raju', '9179876567', 'Mumbai','MCA204', 'CA')");

conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Nancy', '9179785695', 'Andheri','MCA211', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Prashant', '9179876564', 'Andheri','MCA203', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Tanashree', '9179876563', 'Virar','MCA202', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Khushboo', '9179876562', 'Kalyan','MCA201', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Gayatri', '9179876567', 'Andheri','MCA206', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Ronit', '9179876567', 'Nagpur','MCA207', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Nike', '9179876567', 'Dadar','MCA208', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Ajay', '9179876567', 'Pune','MCA209', 'CA')");
conn.execute("INSERT INTO STUD_REGISTRATIONS (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Raj', '9179876567', 'Mumbai','MCA210', 'CA')");

conn.commit()
print ("Records inserted successfully")
conn.close()