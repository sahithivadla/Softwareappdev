import os
import datetime
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import csv
from  models import *
from create import app




# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://dwrfhsnkkoycwg:5aa7d494dbf047ec4358a261c295c6435bbd8306038c4f766ef149c685c103e7@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d5rvrtadpnmjnd'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy()
# # db.init_app(app)
# def main():
#     with app.app_context():
#         db.create_all()
# db.init_app(app)





def main():
    f = open("books.csv")
    reader = csv.reader(f)
    c=0
    for isbn, title, author ,year in reader:
        if c!=0:
            book = Book(isbn=isbn, title=title, author=author,year=year)
            db.session.add(book)
            print(f"Added book of title {title}.")
            db.session.commit()
        c=c+1

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()

