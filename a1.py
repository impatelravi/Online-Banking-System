#!C:\Python27\python.exe -u
print "Content-type: text/html\n\n" ; 
import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully<br>";
print '''<html>
  <head>
    <title>Employee Information</title>
   <style>
	body{
	background-color:#f2f2f2;
	}
	table {
	width:1000px;
	font-size:20px;
	margin:auto;

	}
	table,td,th{
	border:1px solid blue;
	border-collapse:collapse;
	text-align:center;
	}
	th, td {
	padding:15px;
	}
	th {
	background-color:red;
	color:white;
	}
	</style>
  </head>
  <body>'''

	  

try:
	conn.execute('''CREATE TABLE COMPANY
			 (ID INT PRIMARY KEY     NOT NULL,
			 NAME           TEXT    NOT NULL,
			 AGE            INT     NOT NULL,
			 ADDRESS        CHAR(50),
			 SALARY         REAL);''')
	print "Table created successfully<br>";
	
except:
	print "table already created go ahead<br>";

try:
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (1, 'Paul', 32, 'California', 20000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
		  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

	conn.commit()
	print "Records created successfully<br>";
	
except:
	print "record present in DB<br>";

	cursor = conn.execute("SELECT ID,NAME,age,ADDRESS,SALARY from COMPANY")
print cursor	
print '''<br><br><br>
		<table>
      <caption>Employee Information</caption>
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">AGE</th>
		  <th scope="col">Address</th>
          <th scope="col">Salary</th>
        </tr>
      </thead>'''


for row in cursor:
	print '''<tr>
			<th scope="row">%s</th>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
			<td>%s</td>
        </tr>'''%(row[0],row[1],row[2],row[3],row[4])


print " </tbody></table><br><br></body></html>"
print "Operation done successfully<br>";


conn.close()

print "<b>Have a Nice Day<br></b>"
#####---> for python Version 2.x, use: print "helloooooo"