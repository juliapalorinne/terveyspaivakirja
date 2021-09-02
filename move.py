from app import app
from flask import redirect, render_template, request, session
from os import getenv
from querys import *
from user import user_id, error, error_shown, remove_error_message, reset_error_message
from input import *


# GET ALL MOVES
@app.route("/moves")
def moves():
    reset_error_message()
    user = get_user_by_id(user_id())
    moves = get_all_moves()
    length = count=len(list)
    return render_template("moves.html", moves=moves, user=user)


# GET NEW WORKOUT PAGE
@app.route("/moves/new", methods=["GET"])
def see_new_move_page():
    reset_error_message()
    user = get_user_by_id(user_id())
    moves = get_all_moves()
    return render_template("new_move.html", moves=moves, user=user)


# POST NEW MOVE
@app.route("/moves/new", methods=["POST"])
def new_move():
    name = request.form["name"]
    category = request.form["category"]
    instructions = request.form["instructions"]

    if check_name(name) and check_name(category) and len(instructions) < 1000:
        add_move(name, category, instructions)
    else:
        if check_name(name) == False:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        if check_name(category) == False:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        if len(instructions) >= 1000:
            session["error"] = "Ohjeet ovat liian pitkät"
            session["error_shown"] = 1
    
    return see_new_move_page()