from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 
  
file_path = os.path.abspath(os.getcwd())+"/todo.db"
  
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app) 
  

from app import routes 

with app.app_context():
    db.create_all()