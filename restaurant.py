import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Logmein1234@",
  database="Restaurant"
)




'''
TASK 1: Create a new database named 'restaurant'
'''

#mycursor.execute("CREATE DATABASE Restaurant")


'''
Task 2: Verify that your database is created.
'''

#mycursor.execute("SHOW DATABASES")


'''
Task 3: Create a new table named 'bookings', and verify it is created.
The table has the following columns: id (primary key)(int), firstname(varchar), secondname(varchar), email(varchar), reservationno(varchar)
'''


#mycursor.execute("CREATE TABLE Bookings (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), reservationno VARCHAR(255))")

'''mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)'''




'''
Task 5: Add the following into the table
'''
'''
'Tomiwa', 'Adeyanju', 'tom@mail.com', 'Table 1', 
'Precious', 'Garba', 'presh@mail.com', 'Table 11',
'Daniel', 'Akinje', 'dant@mail.com', 'Table 3',
'Tomiwa', 'Lawal', 'md@mail.com', 'Table 15',
'Lawal', 'Yusuf', 'lawal15@mail.com', 'Table 3',
'Olamide', 'Opeyemi', 'Horpi@mail.com', 'Table 2',
'Victor', 'Gabriel', 'gab@mail.com', 'Table 2',
'Mayowa', 'Fatai', 'mayo@mail.com', 'Table 2',
'Daniel', 'Lawal', 'xyz@mail.com', 'Table 1',
'Daniel', 'Bright', 'daniboy@mail.com', 'Table 1',
'Dorime', 'Akpan', 'pinkyqueen@mail.com', 'Table 2',
'''

mycursor = mydb.cursor()

sql = "INSERT INTO Bookings (firstname, lastname, email, reservationno) VALUES (%s, %s, %s, %s)"
val = [
 ('Tomiwa', 'Adeyanju', 'tom@mail.com', 'Table 1'),
 ('Precious', 'Garba', 'presh@mail.com', 'Table 11'),
 ('Daniel', 'Akinje', 'dant@mail.com', 'Table 3'),
('Tomiwa', 'Lawal', 'md@mail.com', 'Table 15'),
('Lawal', 'Yusuf', 'lawal15@mail.com', 'Table 3'),
('Olamide', 'Opeyemi', 'Horpi@mail.com', 'Table 2'),
('Victor', 'Gabriel', 'gab@mail.com', 'Table 2'),
('Mayowa', 'Fatai', 'mayo@mail.com', 'Table 2'),
('Daniel', 'Lawal', 'xyz@mail.com', 'Table 1'),
('Daniel', 'Bright', 'daniboy@mail.com', 'Table 1'),
('Dorime', 'Akpan', 'pinkyqueen@mail.com', 'Table 2')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")

