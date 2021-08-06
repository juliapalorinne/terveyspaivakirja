from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def create_table_users():
    db.session.execute("CREATE TABLE users ( \
	    id SERIAL PRIMARY KEY, \
	    username TEXT UNIQUE, \
	    password TEXT, \
	    name TEXT, \
	    birth_date DATE, \
	    height INTEGER, \
	    weight INTEGER \
    );")


def create_table_moves():
    db.session.execute("CREATE TABLE moves ( \
	    id SERIAL PRIMARY KEY, \
	    name TEXT, \
	    category TEXT, \
	    instructions TEXT \
    );")


def create_table_routines():
    db.session.execute("CREATE TABLE routines ( \
	    id SERIAL PRIMARY KEY, \
	    name TEXT, \
	    category TEXT, \
	    instructions TEXT, \
	    user_id INTEGER REFERENCES users \
    );")


def create_table_workouts():
    db.session.execute("CREATE TABLE workouts( \
	    id SERIAL PRIMARY KEY, \
	    name TEXT, \
	    category TEXT, \
	    time TIMESTAMP, \
	    rating INTEGER, \
	    comments TEXT, \
	    user_id INTEGER REFERENCES users \
    );")


def create_table_routine_moves():
    db.session.execute("CREATE TABLE routine_moves ( \
	    id SERIAL PRIMARY KEY, \
	    routine_id INTEGER REFERENCES routines, \
	    move_id INTEGER REFERENCES moves, \
	    sets INTEGER, \
	    reps INTEGER, \
	    load FLOAT \
    );")


def create_table_workout_moves():
    db.session.execute("CREATE TABLE workout_moves ( \
	    id SERIAL PRIMARY KEY, \
	    workout_id INTEGER REFERENCES workouts, \
	    move_id INTEGER REFERENCES moves, \
	    sets INTEGER, \
	    reps INTEGER, \
	    load FLOAT \
    );")