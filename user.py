from app import app
from flask import render_template
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash


# GET LOGIN PAGE
@app.route("/")
def index():
    return render_template("index.html")


# POST LOGIN INFO
@app.route("/", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # check username and password

    session["username"] = username
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        # TODO: invalid username
        print("invalid username")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # TODO: correct username and password
            print("password correct")
        else:
            # TODO: invalid password
            print("password incorrect")

    return redirect("/")


# GET NEW USER PAGE
@app.route("/new_user", methods=["GET"])
def new_user():
    return render_template("new_user.html")


# POST INFO FOR NEW USER
@app.route("/new_user", methods=["POST"])
def post_new_user():
    username = request.form["username"]
    password = request.form["password"]
    password_again = request.form["password_again"]

    if (password == password_again):
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        return redirect("/")
    
    return redirect("/new_user")