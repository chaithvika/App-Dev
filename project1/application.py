import os
import hashlib

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from usersDb import *
from usersDbIni import *
from werkzeug.security import generate_password_hash, check_password_hash

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def index():
    return "Project 1: TODO. Yayy!!"

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("registration.html")
    else:
        if request.form["button"]=="Sign In":
            email = request.form.get("emailId")
            paswd = request.form.get("password")
            passwd = generate_password_hash(paswd)
            user = User.query.get(email)
            if user is not None:
                if passwd == user.password:
                    return render_template("login.html")
                else:
                    return "wrong password"
            else:
                return "wrong emailId /not registered"

        elif request.form["button"]=="Sign Up":
            name = request.form.get('Username')
            email = request.form.get('email')
            pwd = request.form.get('password1')
            password = generate_password_hash(pwd)
            repwd = request.form.get('password2')
            if pwd == repwd:
                user = User(email, name, password)
                db.session.add(user)
                db.session.commit()
                return "Thank you for registering {}. :)".format(name)
            else:
                return "passwords do not match. Kindly try again."
                
@app.route("/admin")
def admin():
    users = User.query.order_by("timestamp").all()
    return render_template("admin.html", users = users)

@app.route("/login")
def login():
    return render_template("login.html")