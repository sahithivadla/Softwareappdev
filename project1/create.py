import os

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://dwrfhsnkkoycwg:5aa7d494dbf047ec4358a261c295c6435bbd8306038c4f766ef149c685c103e7@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d5rvrtadpnmjnd'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
    # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()