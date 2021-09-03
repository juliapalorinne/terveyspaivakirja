from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from querys import *
from input import *


def user_id():
    return session.get("user_id", 0)

def error():
    return session.get("error", 0)

def error_shown():
    return session.get("error_shown")


# GET LOGIN PAGE
@app.route("/")
def index():
    reset_error_message()
    
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
        session["error"] = "Käyttäjätunnus on virheellinen"
        session["error_shown"] = 1
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            id = user.id
            session["user_id"] = id
            return show_user(id)
        else:
            session["error"] = "Salasana on virheellinen"
            session["error_shown"] = 1


    return redirect("/")


# GET NEW USER PAGE
@app.route("/new_user", methods=["GET"])
def new_user():
    reset_error_message()
    return render_template("new_user.html")


# POST INFO FOR NEW USER
@app.route("/new_user", methods=["POST"])
def post_new_user():
    username = request.form["username"]
    password = request.form["password"]
    password_again = request.form["password_again"]
    user = get_user(username)
    
    if not user:
        if password == password_again and check_username(username):
            hash_value = generate_password_hash(password)
            add_user(username, hash_value)
            user = get_user(username)
            id = user.id
            return show_user(id)
        elif check_username(username) == False:
            session["error"] = "Käyttäjätunnus on virheellinen"
            session["error_shown"] = 1
        elif password != password_again:
            session["error"] = "Salasanat eivät täsmää"
            session["error_shown"] = 1
    else:
        session["error"] = "Käyttäjätunnus on käytössä"
        session["error_shown"] = 1
        
    return new_user()


# GET USER PAGE
@app.route("/user/<int:id>", methods=["GET"])
def show_user(id):
    reset_error_message()
    user = get_user_by_id(id)
    workouts = number_of_workouts(id)
    routines = number_of_routines(id)
    return render_template("user.html", user=user, workouts=workouts, routines=routines)


# ADD NAME
@app.route("/user/<int:id>/change_name", methods=["POST"])
def add_name(id):
    name = request.form["name"]
    if check_name(name):
        change_name(id, name)
    else:
        session["error"] =  "Nimi on virheellinen"
        session["error_shown"] = 1
    return show_user(id)


# ADD BIRTH DATE
@app.route("/user/<int:id>/change_birth_date", methods=["POST"])
def add_birth_date(id):
    birth_date = request.form["birth_date"]
    if not_empty(birth_date):
        change_birth_date(id, birth_date)
    else:
        session["error"] = "Päivämäärä on virheellinen"
        session["error_shown"] = 1
    return show_user(id)


# ADD HEIGHT
@app.route("/user/<int:id>/change_height", methods=["POST"])
def add_height(id):
    height = request.form["height"]
    if check_number(height):
        change_height(id, height)
    else:
        session["error"] = "Pituus on virheellinen"
        session["error_shown"] = 1
    return show_user(id)


# ADD WEIGHT
@app.route("/user/<int:id>/change_weight", methods=["POST"])
def add_weight(id):
    weight = request.form["weight"]
    if check_number(weight):
        change_weight(id, weight)
    else:
        session["error"] = "Paino on virheellinen"
        session["error_shown"] = 1
    return show_user(id)


# GET USER UPDATE PAGE
@app.route("/user/<int:id>/update", methods=["GET"])
def get_user_update(id):
    reset_error_message()
    user = get_user_by_id(id)
    return render_template("update_user.html", user=user)


# UPDATE USER INFO
@app.route("/user/<int:id>/update", methods=["POST"])
def update_user(id):
    username = request.form["username"]
    name = request.form["name"]
    birth_date = request.form["birth_date"]
    height = request.form["height"]
    weight = request.form["weight"]

    if check_name(username) and check_name(name) and check_number(height) and check_number(weight) and not_empty(birth_date):
        change_user_info(id, username, name, birth_date, height, weight)
        return show_user(id)
    else:
        if check_username(username):
            change_username(id, username)            
        elif len(username) > 0:
            session["error"] = "Käyttäjänimi on virheellinen"
            session["error_shown"] = 1

        if check_name(name):
            change_name(id, name)
        elif len(name) > 0:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1

        if not_empty(birth_date):
            change_birth_date(id, birth_date)

        if check_number(height):
            change_height(id, height)
        elif len(height) > 0:
            session["error"] = "Pituus on virheellinen"
            session["error_shown"] = 1

        if check_number(weight):
            change_weight(id, weight)
        elif len(weight) > 0:
            session["error"] = "Paino on virheellinen"
            session["error_shown"] = 1

    return get_user_update(id)


# CHANGE PASSWORD
@app.route("/user/<int:id>/change_password", methods=["POST"])
def update_password(id):
    old_password = request.form["old_password"]
    password = request.form["password"]
    password_again = request.form["password_again"]
    user = get_user_by_id(id)

    hash_value = user.password
    if check_password_hash(hash_value, old_password):
        if password == password_again:
            hash_value = generate_password_hash(password)
            change_password(id, hash_value)
            return show_user(id)
        else:
            session["error"] = "Salasanat eivät täsmää"
            session["error_shown"] = 1
    else:
        session["error"] = "Vanha salasana on virheellinen"
        session["error_shown"] = 1
    return get_user_update(id)


# DELETE USER
@app.route("/user/<int:id>/delete", methods=["POST"])
def delete_user_and_workouts(id):
    password = request.form["password"]
    user = get_user_by_id(id)
    hash_value = user.password

    if check_password_hash(hash_value, password):
        workout_list = get_all_workouts(id)
        for workout in workout_list:
            delete_workout(id, workout.id)

        routine_list = get_all_routines(id)
        for routine in routine_list:
            delete_routine(id, routine.id)
        
        delete_user(id)
        return index()
    else:
        session["error"] = "Salasana on virheellinen"
        session["error_shown"] = 1
    return get_user_update(id)
    
    

# LOG OUT
@app.route("/logout", methods=["GET"])
def logout():
    del session["user_id"]
    remove_error_message()
    return redirect("/")


def reset_error_message():
    if error_shown():
        session["error_shown"] = session["error_shown"] + 1
        if session["error_shown"] > 2:
            del session["error_shown"]
            del session["error"]


def remove_error_message():
    if error():
        del session["error_shown"]
        del session["error"]
