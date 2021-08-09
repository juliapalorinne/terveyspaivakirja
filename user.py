from app import app
from flask import render_template
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash


def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]


# GET LOGIN PAGE
@app.route("/")
def index():
    return render_template("index.html")


# POST LOGIN INFO
@app.route("/", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = get_user(username)

    if not user:
        # TODO: invalid username
        print("invalid username")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            user_id = user.id
            session["user_id"] = user_id
            return redirect("/<int:user_id>")
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
    user = get_user(username)

    if not user:
        if (password == password_again):
            hash_value = generate_password_hash(password)
            add_user(username, hash_value)
            return redirect("/")
        
    return redirect("/new_user")


# GET USER PAGE
@app.route("/<int:user_id>", methods=["GET"])
def show_user(user_id())
    user = get_user
    return render_template("user.html", user=user)