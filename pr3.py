import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")
conn.execute("""
CREATE TABLE STUD_REGISTRATIONS(
STU_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
STU_NAME TEXT NOT NULL, 
STU_CONTACT TEXT,
STU_ADDRESS TEXT,
STU_ROLLNO TEXT NOT NULL,
COURSE_NAME TEXT NOT NULL)
""")
print ("Table STUD_REGISTRATION created successfully")
