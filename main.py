from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if password != verify_password:
        verify_password_error="Passwords must match."

    if ' ' in username or len(username) > 20 or len(username) < 3:
        username_error="Username is not valid."

    if ' ' in password or len(password) > 20 or len(password) < 3:
        password_error="Password is not valid."

    if username == "":
        username_error="Username cannot be blank."

    if password == "" or verify_password == "":
        password_error="Password cannot be blank."

    if email != "":
        if " " in email or "@" not in email or "." not in email or len(email) > 20 or len(email) < 3:
            email_error="Email is not valid."

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, 
        email_error=email_error, username=username, email=email)


    # return render_template('welcome.html', username=username)

@app.route("/welcome", methods=['POST', 'GET'])
def welcome():

    if request.method == 'POST':
        username = request.form['username']
    elif request.method == 'GET':
        username = request.args.get('username')

    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()