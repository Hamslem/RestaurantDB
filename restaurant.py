import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Logmein1234@",
  database="Restaurant"
)




#Creating Database 'Restaurant'

'''
mycursor.execute("CREATE DATABASE Restaurant")

'''


#Verify the database is created

'''
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''



#Creating a table 'bookings'

'''
mycursor.execute("CREATE TABLE Bookings (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), reservationno VARCHAR(255))")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

'''



#Adding to the table 'bookings'

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

for x in mycursor:
  print(x)

'''



#Checking if a data was captured using the SQL query to find a particular name

'''
mycursor = mydb.cursor()

sql = "SELECT * FROM bookings WHERE lastname ='Akinje'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''




#How many occurrence of 'Daniel' is present as the first name.(prevent SQL injection)

'''
mycursor = mydb.cursor()

sql = "SELECT COUNT(*) FROM bookings WHERE firstname = %s"
val = ("daniel",)

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

count = myresult[0]

for x in myresult:
  print(x)

'''




#find out the most booked table

'''
mycursor = mydb.cursor()

sql = "SELECT COUNT(*) FROM bookings WHERE reservationno = %s"
val = ("Table",)

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

count = myresult[0]

for x in myresult:
  print(x)

'''


#The names of those who booked Table 2

'''
mycursor = mydb.cursor()

sql = "SELECT firstname FROM bookings WHERE reservationno = %s"
reservationno = 'Table 2'

mycursor.execute(sql, (reservationno,))

myresult = mycursor.fetchall()


for x in myresult:
  print(x)

'''


#First name in alphabetical order

'''
mycursor = mydb.cursor()

sql = "SELECT * FROM bookings ORDER BY firstname"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''



#A customer whose email address is gab@mail.com wants to change his reservation number to Table 5

'''
mycursor = mydb.cursor()

sql = "UPDATE bookings SET reservationno = %s WHERE email = %s"

val = ("new_reservationno", "email")

email = "gab@mail.com"
new_reservationno = "Table 5"

mycursor.execute(sql, val)

mydb.commit()

'''



#Your line manager called you to notify you that the company is willing to give a 5% discount to the first 5 customers who reserved a sit at the restaurant.

'''
mycursor = mydb.cursor()

sql = " SELECT firstname FROM bookings ORDER BY reservationno ASC LIMIT 5"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''

#After some while, your line manager called again to notify you that the fourth and fifth customer will instead receive a 3.5% discount. Write a SQL query to find out who they are.

'''
mycursor = mydb.cursor()

sql = "SELECT firstname FROM bookings WHERE reservationno LIMIT 2 OFFSET 3"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''


#Deleting a customer records, with the email address of pinkyqueen@mail.com 

'''
mycursor = mydb.cursor()

sql = "DELETE FROM bookings WHERE email = 'pinkyqueen@mail.com'"

mycursor.execute(sql)

mydb.commit()

'''



#A new table named 'prevcustomer', with columns of firstname, email, reservationno. 

'''
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Prevcustomers (firstname VARCHAR(255), email VARCHAR(255), reservationno VARCHAR(255))")

myresult = mycursor.fetchall()

for x in mycursor:
  print(x)

'''


#Delete the table 'Prevcustomers' as it doesn't impact business operations.

'''
mycursor = mydb.cursor()

sql = "DROP TABLE Prevcustomers"

mycursor.execute(sql)

'''