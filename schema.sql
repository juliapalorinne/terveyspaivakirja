CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) UNIQUE,
	password VARCHAR(50),
	name VARCHAR(100),
	birth_date DATE,
	height INTEGER,
	weight INTEGER
);


CREATE TABLE moves (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	category TEXT,
	instructions TEXT
);

CREATE TABLE routines (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	category TEXT,
	instructions TEXT,
	user_id INTEGER REFERENCES users
);

CREATE TABLE workouts(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	category TEXT,
	time TIMESTAMP,
	rating INTEGER,
	comments TEXT,
	user_id INTEGER REFERENCES users,
	routine_id INTEGER REFERENCES routines
);

CREATE TABLE routine_moves (
	id SERIAL PRIMARY KEY,
	routine_id INTEGER REFERENCES routines,
	move_id INTEGER REFERENCES moves,
	move_name VARCHAR(100),
	sets INTEGER,
	reps INTEGER,
	load FLOAT
);

CREATE TABLE workout_moves (
	id SERIAL PRIMARY KEY,
	workout_id INTEGER REFERENCES workouts,
	move_id INTEGER REFERENCES moves,
	move_name VARCHAR(100),
	sets INTEGER,
	reps INTEGER,
	load FLOAT
);


CREATE TABLE days (
	id SERIAL PRIMARY KEY,
	date DATE,
	workout_id1 INTEGER REFERENCES workouts,
	workout_id2 INTEGER REFERENCES workouts,
	workout_id3 INTEGER REFERENCES workouts,
	user_id INTEGER REFERENCES users
);
