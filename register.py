#!C:\Python\Python27\python.exe -u

import cgi, cgitb, MySQLdb, re
form = cgi.FieldStorage() 
cgitb.enable()
	
print "Content-type:text/html\r\n\r\n"
a=form.getvalue('a')
b=form.getvalue('b')
c=form.getvalue('c')

print '''
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Registration</title>
	<!--
    Template 2105 Input
	http://www.tooplate.com/view/2105-input
	-->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/materialize.min.css">
    <link rel="stylesheet" href="css/tooplate.css">
</head>

<body id="register">
    <div class="container">
        <div class="row tm-register-row">
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 tm-register-col-l">
                <form action="regaction.py" method="get" id="login-form">
                    <div class="mb-2">
                        <label class="mr-4">
                            <input class="with-gap" name="title" type="radio" value="mr" />
                            <span>Mr.</span>
                        </label>
                        <label class="mr-4">
                            <input class="with-gap" name="title" type="radio" value="ms" />
                            <span>Ms.</span>
                        </label>
                        <label>
                            <input class="with-gap" name="title" type="radio" value="mrs" />
                            <span>Mrs.</span>
                        </label>
                    </div>

                    <div class="input-field">
                        <input placeholder="First Name" id="first_name" name="first_name" type="text" class="validate" required>
                    </div>
                    <div class="input-field">
                        <input placeholder="Last Name" id="last_name" name="last_name" type="text" class="validate" required>
                    </div>'''
if a>0:
	print '<div style=color:white>%s</div>'%(a)					
print '''			<div class="input-field">
                        <input placeholder="Account Number" id="acc_no" name="acc_no" type="text" class="validate" required>
                    </div>'''
if b>0:
	print '<div style=color:white>%s</div>'%(b)					
print '''			<div class="input-field">
                        <input placeholder="User Name" id="user_name" name="user_name" type="text" class="validate" required>
                    </div>
					<div class="input-field">
                        <input placeholder="Aadhar Card Number" id="aadhar_no" name="aadhar_no" type="text" class="validate" required>
                    </div>
                    <div class="input-field">
                        <input placeholder="Email" id="email" name="email" type="email" class="validate" required>
                    </div>
                    <div class="input-field">
                        <input placeholder="Mobile" id="mobile" name="mobile" type="text" class="validate" required>
                    </div>
                    <div class="input-field">
                        <input placeholder="Address" id="address" name="address" type="text" class="validate" required>
                    </div>
					<div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
							<div class="input-field">
								<input placeholder="Country" id="country" name="country" type="text" class="validate" required>
							</div>
						</div>
						<div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
							<div class="input-field">
								<input placeholder="State" id="state" name="state" type="text" class="validate" required>
							</div>
						</div>
					</div>
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
							<input placeholder="City" id="city" name="city" type="text" class="validate" required>

							<!--<select name="city" required>
                                <option value="-">Your City</option>
                                <option value="Ahmedabad">Ahmedabad</option>
                                <option value="Surat">Surat</option>
                                <option value="Gandhinagar">Gandhinagar</option>
                                <option value="Mehsana">Mehsana</option>
                            </select>//-->
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pr-0 tm-pl-xs-0">
                            <div class="input-field">
                                <input placeholder="Zip Code" id="zipcode" name="zipcode" type="text" class="validate" required>
                            </div>
                        </div>
                    </div>
					<div class="input-field">
                        <input placeholder="Date of Birth" id="dob" name="dob" type="text" class="validate" required>
                    </div>'''
if c>0:
	print '<div style=color:white>%s</div>'%(c)					
print '''			<div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
							<div class="input-field">
								<input placeholder="Password" id="pass" name="pass" type="password" class="validate" required>
							</div>
						</div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
							<div class="input-field">
								<input placeholder="Confirm Password" id="cpass" name="cpass" type="password" class="validate" required>
							</div>
						</div>
					</div>
                    <div class="text-right mt-4">
                        <button type="submit" class="waves-effect btn-large btn-large-white px-4 black-text">SUBMIT</button>
                    </div>
                </form>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 tm-register-col-r">
                <header class="mb-5">
                    <h3 class="mt-0 text-white">REGISTER Yourself</h3>
                    <p class="grey-text">Welcome to the Bank Of Patidar.</p>
                    <p class="grey-text">We always provide best services to our customer and our motto is 
					"Customer is God".
                    </p>
					<p class="grey-text">Please all information fill up.
                    </p>
                </header>

            </div>
        </div>
        <footer class="row tm-mt-big mb-3">
            <div class="col-xl-12">
                <p class="text-center grey-text text-lighten-2 tm-footer-text-small">
                    Copyright &copy; 2018 Bank Of Patidar 
                </p>
            </div>
        </footer>
    </div>

    <script src="js/jquery-3.2.1.slim.min.js"></script>
    <script src="js/materialize.min.js"></script>
    <script>
        $(document).ready(function () {
            $('select').formSelect();
        });
    </script>
</body>

</html>'''