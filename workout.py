from app import app
from flask import redirect, render_template, request, session
from os import getenv
from querys import *
from user import user_id


# GET ALL WORKOUTS
@app.route("/user/<int:user_id>/workouts")
def workouts(user_id):
    list = get_all_workouts(user_id)
    length = count=len(list)
    user = get_user_by_id(user_id)
    return render_template("workouts.html", workouts=list, user=user)


# GET ONE WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>")
def see_workout(user_id, workout_id):
    workout = get_one_workout(user_id, workout_id)
    user = get_user_by_id(user_id)
    moves = get_all_moves_by_workout(user_id, workout_id)
    all_moves = get_all_moves()
    return render_template("workout.html", user=user, workout=workout, moves=moves, all_moves=all_moves)


# GET NEW WORKOUT PAGE
@app.route("/user/<int:user_id>/workouts/new", methods=["GET"])
def see_new_workout_page(user_id):
    user = get_user_by_id(user_id)
    return render_template("new_workout.html", user = user)


# POST NEW WORKOUT
@app.route("/user/<int:user_id>/workouts/new", methods=["POST"])
def new_workout(user_id):
    name = request.form["name"]
    category = request.form["category"]
    comments = request.form["comments"]
    workout_id = add_workout(user_id, name, category, comments)
    
    return redirect(see_workout(user_id, workout_id))


# POST ROUTINE TO NEW WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/log_routine/<int:routine_id>", methods=["POST"])
def log_routine(user_id, workout_id, routine_id):

    sql = "SELECT routine FROM routines WHERE id=:routine_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "routine_id":routine_id})
    routine = result.fetchone()[0]

    sql = "SELECT move_id FROM routine_moves WHERE routine_id=:routine_id"
    result = db.session.execute(sql, {"routine_id":routine_id})
    moves = result.fetchall()
    for move in moves:
        if move != "":
            request.form["sets"]
            request.form["reps"]
            request.form["load"]
            sql = "INSERT INTO workout_moves (workout_id, move_id, sets, reps, load) VALUES (:workout_id, :move_id, :sets, :reps, :load)"
            db.session.execute(sql, {"workout_id":workout_id, "move":move})
    db.session.commit()

    return redirect(see_workout(user_id, workout_id))
    

# POST MOVES TO WORKOUT
@app.route("/user/<int:user_id>/workouts/<int:workout_id>/log_moves", methods=["POST"])
def log_moves(user_id, workout_id):

    sql = "SELECT name FROM moves WHERE id=:routine_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id}, {"routine_id":routine_id})
    routine = result.fetchone()[0]

    moves = request.form.getlist("move")
    for move in moves:
        if move != "":
            request.form["sets"]
            request.form["reps"]
            request.form["load"]
            sql = "INSERT INTO workout_moves (workout_id, move_id, sets, reps, load) VALUES (:workout_id, :move_id, :sets, :reps, :load)"
            db.session.execute(sql, {"workout_id":workout_id, "move":move})
    db.session.commit()

    return redirect(see_workout(user_id, workout_id))

