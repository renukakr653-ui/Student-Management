import mysql.connector
# step 3
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 's2013089',
    database = 'student_db'
)
cursor = conn.cursor()
print('connected successfully')

# step 4  ADD STUDENT(CREATE)
while True:
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    course = input('Enter Course: ')
    query = 'insert into students(name,age,course) values(%s,%s,%s)'
    values = (name,age,course)
    cursor.execute(query,values)
    conn.commit()
    print('successfull')
    choice = input('add another student?(y/n): ')
    if choice!='y':
        break

#step 5 View Students(read)
cursor.execute('select * from students')
for row in cursor.fetchall():
    print(row)

# step 6 update student
name = input('Enter the name')
new_course = input('Enter New course: ')
query = 'update students set course=%s where name=%s'
cursor.execute(query,(new_course,name))
conn.commit()
print('updated successfully')

# step 7 delet student

name=input('Enter the name: ')
query = 'delete from students where name=%s'
cursor.execute(query,(name,))
conn.commit()
print('Deleted successfully')

# step 8 search student

name=input('Enter student Name: ')
query = 'select * from students where name=%s'
cursor.execute(query,(name,))
for row in cursor.fetchall():
    print(row)

# Generate the report
cursor.execute('select count(*) from students')
print('Total students:',cursor.fetchone()[0])

# Delete the table data
cursor.execute('truncate table students')
print('table data deleted')
conn.commit()
print('All Student data deleted Succefully')