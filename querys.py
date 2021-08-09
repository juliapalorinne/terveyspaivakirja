from db import db

def get_all_workouts(user_id):
    sql = "SELECT id, name, time FROM workouts WHERE user ORDER BY id DESC"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list
    

def get_one_workout(user_id, workout_id):
    sql = "SELECT workout FROM workouts WHERE id=:workout_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id}, {"workout_id":workout_id})
    workout = result.fetchone()[0]
    return workout


def add_workout(user_id, name, instructions):
    sql = "INSERT INTO workouts (name, instructions, time, user) " 
    + "VALUES (:name, :instructions, NOW(), :user_id) RETURNING id"

    result = db.session.execute(sql, {"name":name, "instructions":instructions})
    workout_id = result.fetchone()[0]
    return workout_id