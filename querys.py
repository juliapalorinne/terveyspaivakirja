from db import db

# USERS

def get_user(username):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    db.session.commit()
    user = result.fetchone()
    return user

def get_user_by_id(id):
    sql = "SELECT * FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    db.session.commit()
    user = result.fetchone()
    return user

def add_user(username, hash_value):
    sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def change_username(id, username):
    sql = "UPDATE users SET username=:username WHERE id=:id"
    db.session.execute(sql, {"username":username, "id":id})
    db.session.commit()

def change_password(id, hash_value):
    sql = "UPDATE users SET password=:password WHERE id=:id"
    db.session.execute(sql, {"password":hash_value, "id":id})
    db.session.commit()

def change_name(id, name):
    sql = "UPDATE users SET name=:name WHERE id=:id"
    db.session.execute(sql, {"name":name, "id":id})
    db.session.commit()

def change_birth_date(id, birth_date):
    sql = "UPDATE users SET birth_date=:birth_date WHERE id=:id"
    db.session.execute(sql, {"birth_date":birth_date, "id":id})
    db.session.commit()

def change_height(id, height):
    sql = "UPDATE users SET height=:height WHERE id=:id"
    db.session.execute(sql, {"height":height, "id":id})
    db.session.commit()

def change_weight(id, weight):
    sql = "UPDATE users SET weight=:weight WHERE id=:id"
    db.session.execute(sql, {"weight":weight, "id":id})
    db.session.commit()


def change_user_info(id, username, name, birth_date, height, weight):
    sql = "UPDATE users SET (username=:username, name=:name, birth_date=:birth_date, height=:height, weight=:weight) WHERE id=:id"
    db.session.execute(sql, {"username":username, "name":name, "birth_date":birth_date, "height":height, "weight":weight, "id":id})
    db.session.commit()


def delete_user(id):
    sql = "DELETE FROM users WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

    



# WORKOUTS


def get_all_workouts(user_id):
    sql = "SELECT * FROM workouts WHERE user_id=:user_id ORDER BY time DESC"
    result = db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
    list = result.fetchall()
    return list

def number_of_workouts(user_id):
    sql = "SELECT COUNT(id) FROM workouts WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    number = result.fetchone()[0]
    return number

def get_one_workout(user_id, workout_id):
    sql = "SELECT * FROM workouts WHERE id=:workout_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "workout_id":workout_id})
    workout = result.fetchone()
    return workout


def get_all_workouts_by_routine(routine_id):
    sql = "SELECT * FROM workouts WHERE routine_id=:routine_id ORDER BY time DESC"
    result = db.session.execute(sql, {"routine_id":routine_id})
    db.session.commit()
    list = result.fetchall()
    return list


def get_all_moves_by_workout(workout_id):
    sql = "SELECT * FROM workout_moves WHERE workout_id=:workout_id"
    result = db.session.execute(sql, {"workout_id":workout_id})
    db.session.commit()
    list = result.fetchall()
    return list


def get_workout_move(move_id, workout_id):
    sql = "SELECT * FROM workout_moves WHERE move_id=:move_id AND workout_id=:workout_id"
    result = db.session.execute(sql, {"move_id":move_id, "workout_id":workout_id})
    db.session.commit()
    workout_move = result.fetchone()
    return workout_move


def add_move_to_workout(sets, reps, load, move_id, move_name, workout_id):
    sql = "INSERT INTO workout_moves (sets, reps, load, move_id, move_name, workout_id) VALUES (:sets, :reps, :load, :move_id, :move_name, :workout_id)"
    db.session.execute(sql, {"sets":sets, "reps":reps, "load":load, "move_id":move_id, "move_name":move_name, "workout_id":workout_id})
    db.session.commit()


def add_workout(user_id, name, category, comments):
    sql = "INSERT INTO workouts (name, category, comments, time, user_id) VALUES (:name, :category, :comments, NOW(), :user_id) RETURNING id"
    result = db.session.execute(sql, {"user_id":user_id, "name":name, "category":category, "comments":comments})
    db.session.commit()
    workout_id = result.fetchone()[0]
    return workout_id

def link_workout_to_routine(workout_id, routine_id):
    sql = "UPDATE workouts SET routine_id=:routine_id WHERE id=:id"
    db.session.execute(sql, {"routine_id":routine_id, "id":workout_id})
    db.session.commit()


def change_workout_info(workout_id, name, time, category, comments):
    sql = "UPDATE workouts SET (name=:name, category=:category, comments=:comments, time=:time) WHERE id=:id"
    db.session.execute(sql, {"name":name, "category":category, "comments":comments, "time":time, "id":workout_id})
    db.session.commit()


def change_workout_name(workout_id, name):
    sql = "UPDATE workouts SET name=:name WHERE id=:id"
    db.session.execute(sql, {"name":name, "id":workout_id})
    db.session.commit()


def change_workout_time(workout_id, time):
    sql = "UPDATE workouts SET time=:time WHERE id=:id"
    db.session.execute(sql, {"time":time, "id":workout_id})
    db.session.commit()


def change_workout_category(workout_id, category):
    sql = "UPDATE workouts SET category=:category WHERE id=:id"
    db.session.execute(sql, {"category":category, "id":workout_id})
    db.session.commit()


def change_workout_comments(workout_id, comments):
    sql = "UPDATE workouts SET comments=:comments WHERE id=:id"
    db.session.execute(sql, {"comments":comments, "id":workout_id})
    db.session.commit()


def change_workout_routine(workout_id, routine_id):
    sql = "UPDATE workouts SET routine_id=:routine_id WHERE id=:id"
    db.session.execute(sql, {"routine_id":routine_id, "id":workout_id})
    db.session.commit()


def delete_move_from_workout(move_id, workout_id):
    sql = "DELETE FROM workout_moves WHERE move_id=:move_id AND workout_id=:workout_id"
    result = db.session.execute(sql, {"move_id":move_id, "workout_id":workout_id})
    db.session.commit()
    

def delete_workout(user_id, workout_id):
    sql = "DELETE FROM workout_moves WHERE workout_id=:workout_id"
    db.session.execute(sql, {"workout_id":workout_id})
    db.session.commit()
    
    sql = "DELETE FROM workouts WHERE id=:workout_id AND user_id=:user_id"
    db.session.execute(sql, {"user_id":user_id, "workout_id":workout_id})
    db.session.commit()





# MOVES


def get_all_moves():
    sql = "SELECT * FROM moves ORDER BY category"
    result = db.session.execute(sql)
    db.session.commit()
    list = result.fetchall()
    return list

def get_one_move(move_id):
    sql = "SELECT * FROM moves WHERE id=:id"
    result = db.session.execute(sql, {"id":move_id})
    db.session.commit()
    move = result.fetchone()
    return move


def add_move(name, category, instructions):
    sql = "INSERT INTO moves (name, category, instructions) VALUES (:name, :category, :instructions) RETURNING id"
    db.session.execute(sql, {"name":name, "category":category, "instructions":instructions})
    db.session.commit()
    

def change_move(id, name, category, instructions):
    sql = "UPDATE moves SET (name=:name, category=:category, instructions=:instructions) WHERE id=:id"
    db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "id":id})
    db.session.commit()


def delete_move(move_id):
    sql = "DELETE FROM workout_moves WHERE move_id=:move_id"
    db.session.execute(sql, {"move_id":move_id})
    db.session.commit()

    sql = "DELETE FROM routine_moves WHERE move_id=:move_id"
    db.session.execute(sql, {"move_id":move_id})
    db.session.commit()
    
    sql = "DELETE FROM moves WHERE id=:move_id"
    db.session.execute(sql, {"id":move_id})
    db.session.commit()

    


# ROUTINES


def get_all_routines(user_id):
    sql = "SELECT * FROM routines WHERE user_id=:user_id ORDER BY category"
    result = db.session.execute(sql, {"user_id":user_id})
    db.session.commit()
    list = result.fetchall()
    return list


def number_of_routines(user_id):
    sql = "SELECT COUNT(id) FROM routines WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    number = result.fetchone()[0]
    return number


def get_one_routine(user_id, id):
    sql = "SELECT * FROM routines WHERE id=:id AND user_id=:user_id"
    result = db.session.execute(sql, {"id":id, "user_id":user_id})
    db.session.commit()
    routine = result.fetchone()
    return routine


def get_all_moves_by_routine(routine_id):
    sql = "SELECT * FROM routine_moves WHERE routine_id=:routine_id"
    result = db.session.execute(sql, {"routine_id":routine_id})
    db.session.commit()
    list = result.fetchall()
    return list


def get_routine_move(move_id, routine_id):
    sql = "SELECT * FROM routine_moves WHERE move_id=:move_id AND routine_id=:routine_id"
    result = db.session.execute(sql, {"move_id":move_id, "routine_id":routine_id})
    db.session.commit()
    routine_move = result.fetchone()
    return routine_move


def move_to_routine(sets, reps, load, move_id, move_name, routine_id):
    sql = "INSERT INTO routine_moves (sets, reps, load, move_id, move_name, routine_id) VALUES (:sets, :reps, :load, :move_id, :move_name, :routine_id)"
    db.session.execute(sql, {"sets":sets, "reps":reps, "load":load, "move_id":move_id, "move_name":move_name, "routine_id":routine_id})
    db.session.commit()


def add_routine(name, category, instructions, user_id):
    sql = "INSERT INTO routines (name, category, instructions, user_id) VALUES (:name, :category, :instructions, :user_id) RETURNING id"
    result = db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "user_id":user_id})
    db.session.commit()
    routine_id = result.fetchone()[0]
    return routine_id


def change_routine(id, name, category, instructions):
    sql = "UPDATE routines SET (name=:name, category=:category, instructions=:instructions) WHERE id=:id"
    db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "id":id})
    db.session.commit()

def change_routine_name(routine_id, name):
    sql = "UPDATE routine SET name=:name WHERE id=:id"
    db.session.execute(sql, {"name":name, "id":routine_id})
    db.session.commit()


def change_routine_category(routine_id, category):
    sql = "UPDATE routines SET category=:category WHERE id=:id"
    db.session.execute(sql, {"category":category, "id":routine_id})
    db.session.commit()


def change_routine_instructions(routine_id, instructions):
    sql = "UPDATE routines SET instructions=:instructions WHERE id=:id"
    db.session.execute(sql, {"instructions":instructions, "id":routine_id})
    db.session.commit()


def delete_move_from_routine(move_id, routine_id):
    sql = "DELETE FROM routine_moves WHERE move_id=:move_id AND routine_id=:routine_id"
    db.session.execute(sql, {"move_id":move_id, "routine_id":routine_id})
    db.session.commit()


def delete_routine(user_id, routine_id):
    sql = "DELETE FROM routine_moves WHERE routine_id=:routine_id"
    db.session.execute(sql, {"routine_id":routine_id})
    db.session.commit()

    sql = "DELETE FROM routines WHERE id=:routine_id AND user_id=:user_id"
    db.session.execute(sql, {"user_id":user_id, "routine_id":routine_id})
    db.session.commit()

    
