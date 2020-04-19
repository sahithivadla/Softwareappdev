import os
import datetime
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from  models import *
from create import app
import secrets

from sqlalchemy.sql import exists
app.config['SESSION_PERMANENT']=False
app.config["SESSION_TYPE"]="filesystem"
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
Session(app)


@app.route("/index.html",methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route("/register.html", methods=["GET", "POST"])
def register():
    msg=None
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['mail']
        passw = request.form['passw']
        gender = request.form['optradio']
        count = user.query.filter_by(email=mail).first()

        if count:
            error="You already registered with this email id"
            return render_template("register.html",name=error)
        else:
            msg = name+" "+"account created successfully"
            register = user(username = name, email = mail, password = passw,gender=gender)
            db.session.add(register)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    msg=None

    if request.method == "POST":
        mail = request.form['mail']
        passw = request.form['passw']
        count = user.query.filter_by(email=mail).first()

        if count:
            user_data = user.query.filter_by(email=mail).all()
            paswrd= user_data[0].password
            if passw==paswrd:
                msg = "You have logged inthe account successfully"
                session["email"] = mail
                return render_template("userprofile.html")
            else:
                msg = "Incorrect Password"
                return render_template("login.html",blah=msg)
        else:
            return redirect(url_for("register"))

    return render_template("login.html")

@app.route("/admin.html", methods=["GET"])
def admin():
    pichilist = user.query.with_entities(user.email, user.password,user.created).order_by(user.created).all()
    print(pichilist)
    return render_template("admin.html",
                            users = pichilist)

# @app.route("/userprofile",methods=["GET"])
# def userprofile():
#     if request.method=="GET" and session["email"] is not None:
#         return render_template("userprofile.html")
#     else:
#         return redirect(url_for("login"))

@app.route("/logout")
def logout():
   session["email"]=None
   return redirect(url_for("login"))

