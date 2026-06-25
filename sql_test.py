import sqlite3

#conection

connection=sqlite3.connect("student.db")


##create a acursor object to insert records
cursor=connection.cursor()



##create table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

##insert records

cursor.execute('''Insert into STUDENT values('keshav','datascience','A',90)''')
cursor.execute('''Insert into STUDENT values('kk','commerce','B',45)''')
cursor.execute('''Insert into STUDENT values('abc','math','D',94)''')
cursor.execute('''Insert into STUDENT values('keshav','ssc','A',80)''')
cursor.execute('''Insert into STUDENT values('xyz','sanskrit','B',70)''')
cursor.execute('''Insert into STUDENT values('ram','datascience','C',60)''')

##DISPLAY RECORDS

print("the inserted records are:")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)
    

##commit changes

connection.commit()
connection.close()