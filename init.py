import datetime
import os
from flask import Flask, session, redirect, url_for, escape, request
from dotenv import load_dotenv

# Read .env
load_dotenv()

class Configuration:
    # Static Variables
    COOKIE_AGE = int(os.getenv("COOKIE_AGE"))
    COOKIE_SECRET = os.getenv("COOKIE_SECRET")

    PORT = int(os.getenv("PORT"))
    EMAIL = os.getenv("EMAIL")
    TESTING = int(os.getenv("TESTING")) == 1
    
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_CLUSTER = os.getenv("DB_CLUSTER")

# Set up App
app = Flask(__name__)

# Set up flask session
app.secret_key = Configuration.COOKIE_SECRET
app.permanent_session_lifetime = datetime.timedelta(seconds=Configuration.COOKIE_AGE)
SESSION_COOKIE_SECURE = True

# Setup Debugging and Testing Routes
@app.before_request
def make_session_permanent():
    session.permanent = True
