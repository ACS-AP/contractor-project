from flask import Flask, render_template, url_for, request, make_response
from pymongo import MongoClient
from datetime import datetime
from werkzeug.utils import redirect

import bcrypt
import os

app = Flask(__name__)

@app.route('/')
def charity_tracker_index():
  return render_template('new_donation.html') 


@app.route('/login')
def login_form():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
  user = {
    'email': request.form.get('email'),
    'password': request.form.get('password')
  }
  print(user)
  return render_template('new_donation.html')

@app.route('/signup')
def signup_form():
  return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
  new_user = {
    'email': request.form.get('email'),
    'password': request.form.get('password'),
    'confirm_password': request.form.get('confirm_password'),
  }
  print(new_user)
  return render_template('login.html')

@app.route('/profile')
def donor_profile():
  return render_template('profile.html')

@app.route('/charity')
def charity_profile():
  return render_template('charity.html')

@app.route('/donation/new')
def track_donation():
  return render_template('new_donation.html') 

@app.route('/donation', methods=['POST'])
def donation_submit():
  donation = {
    'charity_name': request.form.get('charity_name'),
    'amount_in_cents': request.form.get('donation_amount'),
    'date': request.form.get('date_donated'),
  }
  print(donation)
  return render_template('new_donation.html')

