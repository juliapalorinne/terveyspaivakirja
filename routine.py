from app import app
from flask import redirect, render_template, request, session
from os import getenv
from querys import *
from user import user_id


# GET ALL ROUTINES
@app.route("/user/<int:user_id>/routines")
def routines(user_id):
    list = get_all_routines(user_id)
    length = count=len(list)
    user = get_user_by_id(user_id)
    return render_template("routines.html", routines = list, user = user)


# GET ONE ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>")
def see_routine(user_id, routineid):
    routine = get_one_routine(user_id, workout_id)
    user = get_user_by_id(user_id)
    moves = get_all_moves_by_routine(user_id, routine_id)
    all_moves = get_all_moves()
    return render_template("routine.html", user = user, routine = routine, moves = moves, all_moves = all_moves)


# GET NEW ROUTINE PAGE
@app.route("/user/<int:user_id>/routines/new", methods=["GET"])
def see_new_routine_page(user_id):
    user = get_user_by_id(user_id)
    return render_template("new_routine.html", user = user)


# POST NEW ROUTINE
@app.route("/user/<int:user_id>/routines/new", methods=["POST"])
def new_routine(user_id):
    name = request.form["name"]
    category = request.form["category"]
    instructions = request.form["instructions"]
    routine_id = add_routine(name, category, instructions, user_id)
    
    return redirect(see_routine(user_id, routine_id))