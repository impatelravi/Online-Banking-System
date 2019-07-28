#!C:\Python\Python27\python.exe -u

# Import modules for CGI handling 
import cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()

	
print "Content-type:text/html\r\n\r\n"

title=form.getvalue('title')
first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')
email=form.getvalue('email')
mobile=form.getvalue('mobile')
address=form.getvalue('address')
district=form.getvalue('district')
city=form.getvalue('city')
zipcode=form.getvalue('zipcode')
state=form.getvalue('state')
dob=form.getvalue('dob')
country=form.getvalue('country')
accno=form.getvalue('acc_no')
aadharno=form.getvalue('aadhar_no')
username=form.getvalue('user_name')
passw=form.getvalue('pass')
cpassw=form.getvalue('cpass')
name=title+first_name

db = MySQLdb.connect("localhost","root","","banking" )
cursor=db.cursor()

sql = "SELECT accno FROM reg where accno='%s'"%(accno)
sql0 = "SELECT username FROM reg where username='%s'"%(username)
sql1 = ("INSERT INTO `reg`(`accno`, `username`, `firstname`, `lastname`, `address`, `city`, `state`, `zip`, `country`, `dob`, `aadharno`, `email`, `mobno`, `pass`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(accno,username,name,last_name,address,city,state,zip,country,dob,aadharno,email,mobile,passw))
result=cursor.execute(sql0)
result1=cursor.execute(sql)


if (passw==cpassw):
	if (result1>0):
		URL = "register.py?a=*Account Number Already Exists"
		print('<html>')
		print('  <head>')
		print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
		print('  </head>')
		print('</html>')
	elif (result>0):
		URL = "register.py?b=*Username Already Exists"
		print('<html>')
		print('  <head>')
		print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
		print('  </head>')
		print('</html>')
	else:
		try:	
			cursor.execute(sql1)
			db.commit()
			URL = "index.py?a=Register Successfull"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
			print('  </head>')
			print('</html>')
		except:
			print "record not inserted"
else:
	URL = "register.py?c=*Password Must Be Same"
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
	print('  </head>')
	print('</html>')

db.close()





