import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Logmein1234@",
  database="Restaurant"
)


mycursor = mydb.cursor()

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

mycursor.execute("CREATE TABLE Bookings (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), reservationno VARCHAR(255))")

