#!C:\Python\Python27\python.exe -u

import cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()
	
print "Content-type:text/html\r\n\r\n"

d=form.getvalue('d')
db = MySQLdb.connect("localhost","root","","banking" )
cur = db.cursor()
cur.execute("SELECT balance FROM passbook where accno='%s' order by id desc"%(d))
bal = cur.fetchone()
sql = ("SELECT firstname FROM reg WHERE `accno`='%s'"%(d))
result = cur.execute(sql)
data=cur.fetchone()
data1=str(data[0])
print '''<html lang="en">
	<head>
	<title>Corporate Bank a Banking Category Bootstrap responsive Website Template | Home :: w3layouts</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta charset="utf-8">
	<meta name="keywords" content="Corporate Bank a Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
	Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
	<!-- .css files -->
	
		<style> .z {
			border-radius: 25px;
			border: 2px solid #73AD21;
			padding: 30px;
			margin: 30px auto auto auto;
			width: 50%;
			height: 150px;
			text-align: center;
		} 
		.z1 { margin: 10px}
		</style>
		<link href="css/bars.css" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" href="css/bootstrap.min.css" type="text/css" media="all" />
		<link rel="stylesheet" href="css/style.css" type="text/css" media="all" />
		<link rel="stylesheet" href="css/font-awesome.css" />
	<!-- //.css files -->
	<!-- Default-JavaScript-File -->
		<script type="text/javascript" src="js/jquery-2.1.4.min.js"></script>
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<!-- //Default-JavaScript-File -->
	<!-- fonts -->
		<link href="//fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&amp;subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese" rel="stylesheet">
		<link href="//fonts.googleapis.com/css?family=Ropa+Sans:400,400i&amp;subset=latin-ext" rel="stylesheet">
	<!-- //fonts -->
	<!-- scrolling script -->
	<script type="text/javascript">
		jQuery(document).ready(function($) {
			$(".scroll").click(function(event){		
				event.preventDefault();
				$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
			});
		});
	</script>
	<!-- //scrolling script -->
	</head>
	<!-- //Head -->
	<!-- Body -->
	<body>
		<div class="top-main">
			<div class="number">
				<h3><i class="fa fa-phone" aria-hidden="true"></i> +91-9974421198</h3>
				<div class="clearfix"></div>
			</div>
			<div class="social-icons">
			<ul class="top-icons">
				<li><a href="https://www.facebook.com/impatelravi"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
				<li><a href="https://twitter.com/officialpravi"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
				<li><a href="https://plus.google.com/u/0/116133161153308173208"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li>
				<li><a href="https://www.instagram.com/impatelravi/"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
			</ul>
			<!--<div class="form-top">
			  <form action="#" method="post" class="navbar-form navbar-left">
				<div class="form-group">
					<input type="search" class="form-control" placeholder="Search">
				</div>
					<button type="submit" class="btn btn-default"><i class="fa fa-search" aria-hidden="true"></i></button>
					<!-- <button type="submit" class="btn btn-default">Submit</button> ->
				</form>
			</div> -->
				<div class="clearfix"></div>
			</div>
				<div class="clearfix"></div>
		</div>
		<!-- Top-Bar -->
		<div class="top-bar">
			<nav class="navbar navbar-default">
				<div class="container-fluid">
				<!-- Brand and toggle get grouped for better mobile display -->
					<div class="navbar-header">
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#myNavbar">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
					</div>
					<div class="collapse navbar-collapse" id="myNavbar">
						<ul class="nav navbar-nav navbar-right">
							<li><a href="home.py">home</a></li>
							<li><a href="home.py">services</a></li>'''
print '''					<li><a href="home.py#skills">skills</a></li>
							<!--<li><a href="#team">team</a></li>-->
							<li><a href="home.py#payment">payment</a></li>
							<!--<li><a href="#blog">blog</a></li>-->
							<li><a href="home.py#about">about</a></li>
							<li><a href="home.py#contact">contact</a></li>
							<li><a href="../index.py">Logout</a></li>
							<li><a>Hi %s</a></li>'''%(data1)
print '''
						</ul>
					</div>
				</div>
			</nav>
		</div>
		<div class="z">
			<h1> YOUR CURRENT BALANCE <h1>'''
if (bal==None):
	print '		<h2 class="z1">Rs.0</h2>'
else:
	print '		<h2 class="z1">Rs.%s</h2>'%(bal)
print '''</div>
	</body>
</html>'''