#!C:\Python\Python27\python.exe -u

# Import modules for CGI handling 
import datetime, cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()

	
print "Content-type:text/html\r\n\r\n"

uaccno=form.getvalue('d')
baccno=form.getvalue('accno1')
name=form.getvalue('bname')
amt=form.getvalue('amt')
remark=form.getvalue('remark')
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

db = MySQLdb.connect("localhost","root","","banking" )
cursor=db.cursor()

sql = "SELECT accno FROM reg where accno='%s'"%(baccno)
sql2 = "SELECT balance FROM passbook where accno='%s' order by id desc"%(uaccno)
sql3 = "SELECT balance FROM passbook where accno='%s' order by id desc"%(baccno)
result=cursor.execute(sql)
unewbal=0
bnewbal=0

if (result>0):
	try:	
		cursor.execute(sql2)
		ubal = cursor.fetchone()	
		unewbal=int(ubal[0])-int(amt)
		sql1 = "INSERT INTO `passbook`(`accno`, `date`, `narration`, `dorc`, `Balance`) VALUES ('%s', '%s', '%s', '%s', '%s')"%(uaccno,date,'Debit to accno:'+baccno,amt,unewbal)
		cursor.execute(sql3)
		bbal = cursor.fetchone()	
		bnewbal=int(bbal[0])+int(amt)
		sql2 = "INSERT INTO `passbook`(`accno`, `date`, `narration`, `dorc`, `Balance`) VALUES ('%s', '%s', '%s', '%s', '%s')"%(baccno,date,'Credit from accno:'+uaccno,amt,bnewbal)
		cursor.execute(sql1)
		cursor.execute(sql2)
		db.commit()
		URL = "ft.py?a=Trasfer Successfull&d=%s"%(uaccno)
		print('<html>')
		print('  <head>')
		print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
		print('  </head>')
		print('</html>')
		#print "record inserted successfully"
	except:
		print "record not inserted"
		db.rollback()
else:
	URL = "ft.py?a=*Enter Valid Account Number"
	print('<html>')
	print('  <head>')
	print('    <meta http-equiv="refresh" content="0;url='+str(URL)+'" />') 
	print('  </head>')
	print('</html>')
# disconnect from server
db.close()