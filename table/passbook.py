#!C:\Python\Python27\python.exe -u

import cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()
	
print "Content-type:text/html\r\n\r\n"

d=form.getvalue('d')
db = MySQLdb.connect("localhost","root","","banking" )
cur = db.cursor()
sql1 = "SELECT * FROM passbook where accno='%s'"%(d)
result = cur.execute(sql1)

print '''<html lang="en">
<head>
	<title>Table V04</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100 ver1 m-b-110">
					<div class="table100-head">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Date</th>
									<th class="cell100 column2">Narration</th>
									<th class="cell100 column3">Debit/Credit Amount</th>
									<th class="cell100 column4">Total Balance</th>
								</tr>
							</thead>
						</table>
					</div>'''

print '''			<div class="table100-body js-pscroll">
						<table>
							<tbody>'''
row = cur.fetchall()
for l1 in row :
    print ''' 						<tr class="row100 body">
     							<td class="cell100 column1">%s</td>
     							<td class="cell100 column2">%s</td>
     							<td class="cell100 column3">%s</td>
     							<td class="cell100 column4">%s</td>
     						</tr>'''%(l1[2],l1[3],l1[4],l1[5])

print '''					</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>'''
cur.close()
db.close()