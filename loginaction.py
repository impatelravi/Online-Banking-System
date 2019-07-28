#!C:\Python\Python27\python.exe -u

import cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()
	
print "Content-type:text/html\r\n\r\n"
username=form.getvalue('username')
passw=form.getvalue('password')

db = MySQLdb.connect("localhost","root","","banking" )
cursor=db.cursor()
sql = ("SELECT * FROM reg WHERE `username`='%s' AND pass='%s'"%(username,passw))
result = cursor.execute(sql)
data=cursor.fetchone()
d=data[1]
row=cursor.rowcount

if(row > 0):
	URL = "html/home.py?d=%s"%(d)
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
	print('  </head>')
	print('</html>')
else:
	URL = "index.py?a='Invalid Username or Password'"
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
	print('  </head>')
	print('</html>')

db.close()