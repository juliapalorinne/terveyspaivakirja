from app import app
from flask import redirect, render_template, request, session
from os import getenv
from querys import *
from user import user_id, error, error_shown, remove_error_message, reset_error_message
from input import *


# GET ALL ROUTINES
@app.route("/user/<int:user_id>/routines", methods=["GET"])
def routines(user_id):
    reset_error_message()
    routines = get_all_routines(user_id)
    user = get_user_by_id(user_id)
    return render_template("routines.html", routines=routines, user=user)


# GET ROUTINES AND SEARCH RESULTS
@app.route("/user/<int:user_id>/routines/term/<string:term>")
def routines_and_results(user_id, term):
    reset_error_message()
    routines = get_all_routines(user_id)
    user = get_user_by_id(user_id)
    search = search_routines(user_id, term)
    return render_template("routines.html", routines=routines, user=user, search=search, term=term)


# SEARCH ROUTINES
@app.route("/user/<int:user_id>/routines/search", methods=["POST"])
def search_routine(user_id):
    term = request.form["term"]
    if check_name(term):
        return routines_and_results(user_id, term)
    else:
        session["error"] = "Hakusana on virheellinen"
        session["error_shown"] = 1
    return routines(user_id)


# GET NEW ROUTINE PAGE
@app.route("/user/<int:user_id>/routines/new", methods=["GET"])
def see_new_routine_page(user_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    return render_template("new_routine.html", user=user)


# POST NEW ROUTINE
@app.route("/user/<int:user_id>/routines/new", methods=["POST"])
def new_routine(user_id):
    name = request.form["name"]
    category = request.form["category"]
    instructions = request.form["instructions"]

    if check_name(name) and check_text(category) and len(instructions) < 1000:
        routine_id = add_routine(name, category, instructions, user_id)
        return see_routine(user_id, routine_id)
    else:
        if check_name(name) == False:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        if check_text(category) == False:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        if len(instructions) >= 1000:
            session["error"] = "Ohjeet on liian pitkä"
            session["error_shown"] = 1
    
    return see_new_routine_page(user_id)
    

# GET ONE ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>", methods=["GET"])
def see_routine(user_id, routine_id):
    reset_error_message()
    routine = get_one_routine(user_id, routine_id)
    user = get_user_by_id(user_id)
    moves = get_all_moves_by_routine(routine_id)
    workouts = get_all_workouts_by_routine(routine_id)

    return render_template("routine.html", user=user, routine=routine, moves=moves, workouts=workouts)


# ADD MOVES TO ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>/add_moves", methods=["POST"])
def add_moves_to_routine(user_id, routine_id):
    error = ""
    moves = request.form.getlist("move_id")

    if not_empty(moves):
        for move_id in moves:
            sets = request.form["sets" + move_id]
            reps = request.form["reps" + move_id]
            load = request.form["load" + move_id]
            move = get_one_move(move_id)

            if check_number(sets) and check_number(reps) and check_number(load):
                move_to_routine(sets, reps, load, move_id, move.name, routine_id)
            else:
                if check_number(sets) == False:
                    error = error + " \ Liikkeen " + move.name + " sarjat on virheellinen"
                    session["error_shown"] = 1
                if check_number(reps) == False:
                    error = error + " \ Liikkeen " + move.name + " toistot on virheellinen"
                    session["error_shown"] = 1
                if check_number(load) == False:
                    error = error + " \ Liikkeen " + move.name + " vastus on virheellinen"
                    session["error_shown"] = 1
    else:
        error = "Yhtään liikettä ei valittu"
        session["error_shown"] = 1
    
    session["error"] = error
    return see_routine(user_id, routine_id)


# GET UPDATE ROUTINE PAGE
@app.route("/user/<int:user_id>/routines/<int:routine_id>/update", methods=["GET"])
def get_update_routine_page(user_id, routine_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    routine = get_one_routine(user_id, routine_id)
    moves = get_all_moves_by_routine(routine_id)
    all_moves = get_all_moves()
    return render_template("update_routine.html", user=user, routine=routine, moves=moves, all_moves=all_moves)


# UPDATE ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>/update", methods=["POST"])
def update_routine(user_id, routine_id):
    user = get_user_by_id(user_id)
    routine = get_one_routine(user_id, routine_id)

    name = request.form["name"]
    category = request.form["category"]
    comments = request.form["comments"]

    if check_name(name) and check_text(category) and len(comments) < 1000:
        routine_id = change_routine_info(routine_id, name, time, category, comments)
        return see_routine(user_id, routine_id)
    else:
        if check_name(name):
            change_routine_name(routine_id, name)
        elif len(name) > 0:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        
        if check_text(category):
            change_routine_category(routine_id, category)
        elif len(category) > 0:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        
        if len(comments) < 1000:
            change_routine_instructions(routine_id, comments)
        elif len(comments) >= 1000:
            session["error"] = "Lisätiedot on liian pitkä"
            session["error_shown"] = 1

    return get_update_routine_page(user_id, routine_id)


# DELETE MOVES FROM ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>/delete_moves", methods=["POST"])
def delete_moves_from_routine(user_id, routine_id):
    moves = request.form.getlist("move_id")

    if not_empty(moves):
        for move_id in moves:
            delete_move_from_routine(move_id, routine_id)
    else:
        session["error"] = "Yhtään liikettä ei valittu"
        session["error_shown"] = 1
    
    return get_update_routine_page(user_id, routine_id)


# DELETE ROUTINE
@app.route("/user/<int:user_id>/routines/<int:routine_id>/delete", methods=["POST"])
def delete_this_routine(user_id, routine_id):
    delete_routine(routine_id)
    return routines(user_id)
