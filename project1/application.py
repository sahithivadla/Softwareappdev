import os

from flask import Flask, session,request,render_template,flash,logging
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/register.html", methods=["GET", "POST"])
def register():
    msg=None
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['mail']
        passw = request.form['passw']
        gender = request.form.get('gender')

        # print(passw)
        # register = user(username = uname, email = mail, password = passw)
        # return redirect(url_for("login"),mail)
        if(len(passw)<8):
            app.logger.info('%s password is less than 8 chars',name)
            msg="The length of password should be greater than 8"
            return render_template("register.html",name=msg)
        elif(not name.isalpha()):
            app.logger.info('the name has numbers in it')
            msg = "The name has numbers in it!!"
            return render_template("register.html",name=msg)
        else:
            app.logger.info('%s logged in successfully',name)
            app.logger.info(mail)
            app.logger.info(gender)
            msg = name+"account created successfully"
            return render_template("register.html",name=msg)

    return render_template("register.html")
