from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user-signup2.html')


def checkBlank(val):
    if val == '' or (' ' in val):
        return True
    else:
        return False

def checkLength(val):
    if len(val) < 3 or len(val) > 20:
        return False
    else:
        return True

def checkMatch(val, val2):
    if val != val2:
        return False
    else:
        return True

def checkEmail(val):
    if checkLength(val) and val.count('@') == 1 and val.count('.') == 1 and (' ' in val) == False:
        return True
    else:
        return False


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username_inp']
    password = request.form['password_inp']
    verif_password = request.form['verify_inp']
    email = request.form['email_inp']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    
    if checkBlank(username):
        username_error = 'Value cannot be blank or have any spaces'
    
    elif not checkLength(username):
        username_error = 'Value must be between 3 and 20 characters'

    if checkBlank(password):
        password_error = 'Value cannot be blank or have any spaces'
    
    elif not checkLength(password):
        password_error = 'Value must be between 3 and 20 characters'
    
    elif not checkMatch(password, verif_password):
        verify_error = 'Password and Verify Password do not match'

    if checkEmail(email):
        email_error = ''
    else:
        email_error = 'Email must be between 3-20 characters, have no spaces, contain only a single @ and period sign'
   
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('user-signup2.html', username_error=username_error,
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error,
        username=username,
        password='',
        verify='',
        email=email)
    
app.run()   