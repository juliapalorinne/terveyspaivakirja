from db import db

# USERS

def get_user(username):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    return user

def get_user_by_id(id):
    sql = "SELECT * FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    user = result.fetchone()
    return user

def add_user(username, hash_value):
    sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
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
    sql = "UPDATE users SET (username=:username, name=:name, "
    + "birth_date=:birth_date, height=:height, weight=:weight) WHERE id=:id"
    db.session.execute(sql, {"username":username, "name":name, "birth_date":birth_date, "height":height, "weight":weight, "id":id})
    db.session.commit()




# WORKOUTS


def get_all_workouts(user_id):
    sql = "SELECT id, name, time FROM workouts WHERE user_id=:user_id "
    + "ORDER BY id DESC"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list


def get_one_workout(user_id, workout_id):
    sql = "SELECT workout FROM workouts WHERE id=:workout_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id}, {"workout_id":workout_id})
    workout = result.fetchone()[0]
    return workout


def get_all_moves_by_workout(workout_id):
    sql = "SELECT * FROM workout_moves WHERE workout_id=:workout_id"
    result = db.session.execute(sql, {"workout_id":workout_id})
    list = result.fetchall()
    return list


def add_workout(user_id, name, category, comments):
    sql = "INSERT INTO workouts (name, category, comments, time, user) " 
    + "VALUES (:name, :category, :comments, NOW(), :user_id) RETURNING id"
    result = db.session.execute(sql, {"user_id":user_id, "name":name, "category":category, "comments":comments})
    workout_id = result.fetchone()[0]
    return workout_id


def change_workout_info(id, username, name, height, weight):
    sql = "UPDATE users SET (username=:usrename, name=:name, "
    + "height=:height, weight=:weight) WHERE id=:id"
    db.session.execute(sql, {"username":usrename, "name":name, "height":height, "weight":weight, "id":id})
    db.session.commit()


def delete_workout(user_id, workout_id):
    sql = "DELETE workout FROM workouts WHERE id=:workout_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "workout_id":workout_id})
    db.session.commit()

    sql = "DELETE move FROM workout_moves WHERE workout_id=:workout_id"
    result = db.session.execute(sql, {"workout_id":workout_id})
    db.session.commit()




# MOVES


def add_move(name, category, instructions):
    sql = "INSERT INTO moves (name, category, instructions) "
    + "VALUES (:name, :category, :instructions) RETURNING id"
    result = db.session.execute(sql, {"name":name, "category":category, "instructions":instructions})
    move_id = result.fetchone()[0]
    return move_id


def change_move(id, name, category, instructions):
    sql = "UPDATE moves SET (name=:name, category=:category, instructions=:instructions) WHERE id=:id"
    db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "id":id})
    db.session.commit()


def delete_move(move_id):
    sql = "DELETE move FROM workout_moves WHERE move_id=:move_id"
    result = db.session.execute(sql, {"move_id":move_id})
    db.session.commit()

    sql = "DELETE move FROM routine_moves WHERE move_id=:move_id"
    result = db.session.execute(sql, {"move_id":move_id})
    db.session.commit()
    
    sql = "DELETE move FROM moves WHERE id=:move_id"
    result = db.session.execute(sql, {"id":move_id})
    db.session.commit()

    


# ROUTINES


def get_all_routines(user_id):
    sql = "SELECT id, name, category FROM routines WHERE user_id=:user_id "
    + "ORDER BY id DESC"
    result = db.session.execute(sql)
    list = result.fetchall()
    return list


def get_one_routine(user_id, routine_id):
    sql = "SELECT routine FROM routines WHERE id=:routine_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id}, {"routine_id":routine_id})
    routine = result.fetchone()[0]
    return routine


def get_all_moves_by_routine(routine_id):
    sql = "SELECT * FROM routine_moves WHERE routine_id=:routine_id"
    result = db.session.execute(sql, {"routine_id":routine_id})
    list = result.fetchall()
    return list


def add_routine(name, category, instructions, user_id):
    sql = "INSERT INTO moves (name, category, instructions, user_id) "
    + "VALUES (:name, :category, :instructions, :user_id) RETURNING id"
    result = db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "user_id":user_id})
    routine_id = result.fetchone()[0]
    return routine_id


def change_routine(id, name, category, instructions):
    sql = "UPDATE routines SET (name=:name, category=:category, instructions=:instructions) WHERE id=:id"
    db.session.execute(sql, {"name":name, "category":category, "instructions":instructions, "id":id})
    db.session.commit()


def delete_routine(user_id, routine_id):
    sql = "DELETE move FROM routine_moves WHERE routine_id=:routine_id"
    result = db.session.execute(sql, {"routine_id":routine_id})
    db.session.commit()

    sql = "DELETE routine FROM routines WHERE id=:routine_id AND user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id, "routine_id":routine_id})
    db.session.commit()

    
