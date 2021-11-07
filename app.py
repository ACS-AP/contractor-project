from flask import Flask, render_template, url_for, request
from pymongo import MongoClient
from datetime import datetime
import os


app = Flask(__name__)

host = os.environ.get('MONGODB_URI')
client = MongoClient(host=host)
db = client.get_database('contractor-project')

users = db.users
charities = db.charities

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)