from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from querys import get_user, get_user_by_id, add_user, change_name, change_birth_date, change_height, change_weight, change_user_info


def user_id():
    return session.get("user_id", 0)


# GET LOGIN PAGE
@app.route("/")
def index():
    if not user_id():
        return render_template("index.html")
    else:
        user = get_user_by_id(user_id())
        return render_template("index.html", user=user)


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
            id = user.id
            session["user_id"] = id
            return show_user(id)
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
        if password == password_again:
            hash_value = generate_password_hash(password)
            add_user(username, hash_value)
            user = get_user(username)
            id = user.id
            return show_user(id)
        
    return redirect("/new_user")


# GET USER PAGE
@app.route("/user/<int:id>", methods=["GET"])
def show_user(id):
    user = get_user_by_id(id)
    return render_template("user.html", user=user)


# ADD NAME
@app.route("/user/<int:id>/change_name", methods=["POST"])
def add_name(id):
    name = request.form["name"]
    change_name(id, name)
    return show_user(id)


# ADD BIRTH DATE
@app.route("/user/<int:id>/change_birth_date", methods=["POST"])
def add_birth_date(id):
    birth_date = request.form["birth_date"]
    change_birth_date(id, birth_date)
    return show_user(id)


# ADD HEIGHT
@app.route("/user/<int:id>/change_height", methods=["POST"])
def add_height(id):
    user = get_user_by_id(id)
    height = request.form["height"]
    change_height(id, height)
    return show_user(id)


# ADD WEIGHT
@app.route("/user/<int:id>/change_weight", methods=["POST"])
def add_weight(id):
    weight = request.form["weight"]
    change_weight(id, weight)
    return show_user(id)


# GET USER UPDATE PAGE
@app.route("/user/<int:id>/update", methods=["GET"])
def get_user_update():
    return render_template("update_user.html")


# UPDATE USER INFO
@app.route("/user/<int:id>/update", methods=["POST"])
def update_user(id):
    username = request.form["username"]
    name = request.form["name"]
    birth_date = request.form["birth_date"]
    height = request.form["height"]
    weight = request.form["weight"]
    change_user_info(id, username, name, birth_date, height, weight)
    return show_user(id)



# LOG OUT
@app.route("/logout", methods=["GET"])
def logout():
    del session["user_id"]
    return redirect("/")