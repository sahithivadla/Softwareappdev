import os
import datetime
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from  models import *
from create import app
from sqlalchemy.sql import exists



@app.route("/register.html", methods=["GET", "POST"])
def register():
    msg=None
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['mail']
        passw = request.form['passw']
        gender = request.form['optradio']
        count = user.query.filter_by(email=mail)

        try:
            msg = name+" "+"account created successfully"
            register = user(username = name, email = mail, password = passw,gender=gender)
            db.session.add(register)
            db.session.commit()
            return render_template("register.html",name=msg)


        except:
            error="You already registered with this email id"
            return render_template("register.html",name=error)


    return render_template("register.html")


# @app.route("/login.html", methods=["GET", "POST"])
# def login():
#     msg=None
#     if request.method == "POST":
#         mail = request.form['mail']
#         passw = request.form['passw']
#         count = user.query(user.password).filter_by(email=mail)

#         try:
#             if db.String(passw)==user.password:
#                 msg = "You have logged inthe account successfully"
#                 return render_template("url_for(login.html)",blah=msg)
#             else:
#                 msg = "Incorrect Password"
#                 return render_template("login.html",blah=msg)
#         except:
#             error="This email doesnt exist!! Please register yourself first"
#             return render_template("register.html",msg=error)

#     return render_template("login.html")

@app.route("/admin.html", methods=["GET"])
def admin():
    pichilist = user.query.with_entities(user.email, user.password,user.created).order_by(user.created).all()
    print(pichilist)
    return render_template("admin.html",
                            users = pichilist)



