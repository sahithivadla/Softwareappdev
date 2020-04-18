import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from  models import *
from create import app
from sqlalchemy.sql import exists
import csv

def main():
      f = open("books.csv")
      reader = csv.reader(f)
      for ISBN, title, author , year in reader:
          book = Books(ISBN=ISBN, title=title, author=author,year=year)
          db.session.add(book)
          print(f"Added the entry {ISBN} {title} {author} {year}")
      db.session.commit()



