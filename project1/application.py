import os

from flask import Flask, session , render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO. Yayy!!"

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("registration.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        return "Hello {}. Your password is encrypted as {}. So don't worry, you are in safe hands".format(name,generate_password_hash(password))
