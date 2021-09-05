from app import app
from flask import redirect, render_template, request, session
from os import getenv
from querys import *
from user import user_id, error, error_shown, remove_error_message, reset_error_message
from input import *



# GET ALL WORKOUTS
@app.route("/user/<int:user_id>/workouts")
def workouts(user_id):
    reset_error_message()
    workouts = get_all_workouts(user_id)
    user = get_user_by_id(user_id)
    return render_template("workouts.html", workouts=workouts, user=user)


# GET WORKOUTS AND SEARCH RESULTS
@app.route("/user/<int:user_id>/workouts/term/<string:term>")
def workouts_and_results(user_id, term):
    reset_error_message()
    workouts = get_all_workouts(user_id)
    user = get_user_by_id(user_id)
    search = search_workouts(user_id, term)
    return render_template("workouts.html", workouts=workouts, user=user, search=search, term=term)


# SEARCH WORKOUTS
@app.route("/user/<int:user_id>/workouts/search", methods=["POST"])
def search_workout(user_id):
    term = request.form["term"]
    if check_name(term):
        return workouts_and_results(user_id, term)
    else:
        session["error"] = "Hakusana on virheellinen"
        session["error_shown"] = 1
    return workouts(user_id)


# GET NEW WORKOUT PAGE
@app.route("/user/<int:user_id>/workouts/new", methods=["GET"])
def see_new_workout_page(user_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    return render_template("new_workout.html", user=user)


# POST NEW WORKOUT
@app.route("/user/<int:user_id>/workouts/new", methods=["POST"])
def new_workout(user_id):
    name = request.form["name"]
    category = request.form["category"]
    comments = request.form["comments"]

    if check_name(name) and check_text(category) and len(comments) < 1000:
        workout_id = add_workout(user_id, name, category, comments)
        return see_workout(user_id, workout_id)
    else:
        if check_name(name) == False:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        if check_text(category) == False:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        if len(comments) >= 1000:
            session["error"] = "Lisätiedot on liian pitkä"
            session["error_shown"] = 1
    
    return see_new_workout_page(user_id)


# GET ONE WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>")
def see_workout(user_id, workout_id):
    reset_error_message()
    workout = get_one_workout(user_id, workout_id)
    user = get_user_by_id(user_id)
    moves = get_all_moves_by_workout(workout_id)
    all_moves = get_all_moves()
    
    return render_template("workout.html", user=user, workout=workout, moves=moves, all_moves=all_moves)


# POST MOVES TO WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/log_moves", methods=["POST"])
def log_moves(user_id, workout_id):
    error = ""
    moves = request.form.getlist("move_id")
    
    if not_empty(moves):
        for move_id in moves:
            sets = request.form["sets" + move_id]
            reps = request.form["reps" + move_id]
            load = request.form["load" + move_id]
            move = get_one_move(move_id)
            
            if check_number(sets) and check_number(reps) and check_number(load):
                add_move_to_workout(sets, reps, load, move_id, move.name, workout_id)
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
    return see_workout(user_id, workout_id)


# GET UPDATE WORKOUT PAGE
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/update", methods=["GET"])
def get_update_workout_page(user_id, workout_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    workout = get_one_workout(user_id, workout_id)
    moves = get_all_moves_by_workout(workout_id)
    return render_template("update_workout.html", user=user, workout=workout, moves=moves)


# UPDATE WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/update", methods=["POST"])
def update_workout(user_id, workout_id):
    user = get_user_by_id(user_id)
    workout = get_one_workout(user_id, workout_id)

    name = request.form["name"]
    time = request.form["time"]
    category = request.form["category"]
    comments = request.form["comments"]

    if check_name(name) and check_text(category) and not_empty(time) and check_text(comments):
        workout_id = change_workout_info(workout_id, name, time, category, comments)
        return see_workout(user_id, workout_id)
    else:
        if check_name(name):
            change_workout_name(workout_id, name)
        elif len(name) > 0:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        
        if check_text(category):
            change_workout_category(workout_id, category)
        elif len(category) > 0:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        
        if not_empty(time):
            change_workout_time(workout_id, time)
        
        if check_text(comments):
            change_workout_comments(workout_id, comments)
        elif len(comments) > 0:
            session["error"] = "Lisätiedot on virheellinen"
            session["error_shown"] = 1

    return get_update_workout_page(user_id, workout_id)


# DELETE MOVES FROM WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/delete_moves", methods=["POST"])
def delete_moves_from_workout(user_id, workout_id):
    moves = request.form.getlist("move_id")

    if not_empty(moves):
        for move_id in moves:
            print(move_id)
            print(workout_id)
            delete_move_from_workout(move_id, workout_id)
    else:
        session["error"] = "Yhtään liikettä ei valittu"
        session["error_shown"] = 1
    
    return get_update_workout_page(user_id, workout_id)


# DELETE WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/delete", methods=["POST"])
def delete_this_workout(user_id, workout_id):
    delete_workout(user_id, workout_id)
    return workouts(user_id, null)


# GET LOG ROUTINE LIST
@app.route("/user/<int:user_id>/workouts/new/log_routine", methods=["GET"])
def log_routine_list(user_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    routines = get_all_routines(user_id)
    return render_template("select_routine.html", user=user, routines=routines)


# GET LOG ROUTINE PAGE
@app.route("/user/<int:user_id>/workouts/new/log_routine/<int:routine_id>", methods=["GET"])
def log_routine_page(user_id, routine_id):
    reset_error_message()
    user = get_user_by_id(user_id)
    routine = get_one_routine(user_id, routine_id)
    moves = get_all_moves_by_routine(routine_id)
    return render_template("log_routine.html", user=user, routine=routine, moves=moves)
    

# POST ROUTINE TO NEW WORKOUT
@app.route("/user/<int:user_id>/workouts/new/log_routine/<int:routine_id>", methods=["POST"])
def log_routine(user_id, routine_id):
    moves = get_all_moves_by_routine(routine_id)
    
    name = request.form["name"]
    category = request.form["category"]
    comments = request.form["comments"]

    if check_name(name) and check_text(category) and len(comments) < 1000:
        workout_id = add_workout(user_id, name, category, comments)
        link_workout_to_routine(workout_id, routine_id)
        
        for move in moves:
            sets = move.sets
            reps = move.reps
            load = move.load
            move_id = move.move_id
            move_name = move.move_name
            add_move_to_workout(sets, reps, load, move_id, move_name, workout_id)

        return see_workout(user_id, workout_id)
    else:
        if check_name(name) == False:
            session["error"] = "Nimi on virheellinen"
            session["error_shown"] = 1
        if check_text(category) == False:
            session["error"] = "Kategoria on virheellinen"
            session["error_shown"] = 1
        if len(comments) >= 1000:
            session["error"] = "Lisätiedot on liian pitkä"
            session["error_shown"] = 1
    return log_routine_page(user_id)
    


# POST ROUTINE TO WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/log_routine/<int:routine_id>", methods=["POST"])
def post_routine_to_workout(user_id, workout_id, routine_id):
    moves = get_all_moves_by_routine(routine_id)
    link_workout_to_routine(workout_id, routine_id)

    for move in moves:
        sets = move.sets
        reps = move.reps
        load = move.load
        move_id = move.move_id
        add_move_to_workout(sets, reps, load, move_id, workout_id)

    return see_workout(user_id, workout_id)

