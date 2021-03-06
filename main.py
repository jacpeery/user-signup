from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("user-signup.html")

# are the user inputs filled in?

def filled_in(inp):
    if inp != "":
        return True
    else:
        return False

# whitespace is not permitted!

def no_whitespace(inp):
    whitespace = " "
    if whitespace not in inp:
        return True
    else:
        return False

# must have @ and .

def has_at_sign(inp):
    at_sign = '@'
    if at_sign in inp:
        return True
    else:
        return False 

def has_period(inp):
    period = '.'
    if period in inp:
        return True
    else:
        return False     


@app.route('/validate', methods=['POST'])
def validate():
    username_inp = request.form['username']
    password_inp = request.form['password']
    verify_pw = request.form['verify']
    email_inp = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if not filled_in(username_inp):
        username_error = "Please enter a username."
        username_inp = ""
    else:
        len_username = len(username_inp)
        if len_username > 20 or len_username < 3:
            username_error = "Username must be greater than 3 and less than 20 characters."
            
        else:
            if not no_whitespace(username_inp):
                username_error = "Spaces are not permitted."
                

    if not filled_in(password_inp):
        password_error = "Please enter a creative password."
        password_inp = ""
    else:
        len_password = len(password_inp)
        if len_password > 20 or len_password < 3:
            password_error = "Password must be greater than 3 and less than 20 characters."
            password_inp = ""
        else:
            if not no_whitespace(password_inp):
                password_error = "Spaces are not permitted."
                password_inp = ""

    if not filled_in(verify_pw):
        verify_error = "Please reenter the same creative password."
        verify_pw = ""
    else:
        if verify_pw != password_inp:
            verify_error = "Creative passwords must match!"
            verify_pw = ""

# email is optional but must be valid if entered 
# valid_email = input > 3 and < 20 with @ and '.'    

    if not filled_in(email_inp):
        email_error = ""
        
    else:
        len_email = len(email_inp)
        if len_email > 20 or len_email < 3:
            email_error = "Email must be greater than 3 and less than 20 characters."
            
        elif not no_whitespace(email_inp):
            email_error = "Spaces are not permitted."
                
        elif not email_inp.count("@") == 1:
            email_error = "Email must contain one at sign (@)"
                   
        elif not email_inp.count(".") == 1:
            email_error = "Email must contain one period (.)"
                
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username_inp)
    else:
        return render_template("user-signup.html", username=username_inp, password=password_inp, verify=verify_pw,email=email_inp,
        username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()