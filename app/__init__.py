from flask import Flask

app = Flask(__name__)

from app import views

print("this statemnent from init")
