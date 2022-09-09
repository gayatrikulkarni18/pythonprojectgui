import squlite 3
#define connection and cursor
connection = squlite3.connect('store_student.db')

cursor = connection.cursor()
# create and store table
command1="""create table if not exisits
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""
