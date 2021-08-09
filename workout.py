from app import app
from flask import render_template
from os import getenv


# GET ALL WORKOUTS
@app.route("/<int:user_id>/workouts")
def workouts(user_id):
    list = get_all_workouts(user_id)
    return render_template(str(user_id) + "workouts.html", workouts = list, count=len(list))


# GET ONE WORKOUT
@app.route("/<int:user_id>/workouts/<int:workout_id>")
def see_workout(user_id, workout_id):
    workout = get_one_workout(user_id, workout_id)
    return render_template(str(user_id) + "workout.html", user_id = user_id, moves = moves)


# POST NEW WORKOUT
@app.route("/<int:user_id>/workouts/new", methods=["POST"])
def new_workout(user_id):
    name = request.form["name"]
    instructions = request.form["instructions"]    
    workout_id = add_workout(user_id, name, instructions)
    
    return redirect(str(user_id) + "/workouts" + str(workout_id)


# POST ROUTINE TO NEW WORKOUT
@app.route("/<int:user_id>/workouts/<int:workout_id>/log_routine/<int:routine_id>", methods=["POST"]))
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

    return redirect(str(user_id) + "/workouts/" + str(workout_id))
    

# POST MOVES TO WORKOUT
@app.route("/<int:user_id>/workouts/<int:workout_id>/log_moves", methods=["POST"])
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


    return redirect(str(user_id) + "/workouts" + str(workout_id))

