import sqlite3

connection = sqlite3.connect("internal_omdb.db")
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS movies""")
cursor.execute("""DROP TABLE IF EXISTS actors""")
cursor.execute("""DROP TABLE IF EXISTS directors""")
cursor.execute("""DROP TABLE IF EXISTS movies_actors""")
cursor.execute("""DROP TABLE IF EXISTS movies_directors""")



cursor.execute("""
	CREATE TABLE movies(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		movie VARCHAR(32)

	);
	""")

cursor.execute("""
	CREATE TABLE actors(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		actor VARCHAR(32),
		actor_id INTEGER,
		FOREIGN KEY(actor_id) REFERENCES actors(id)

	);
	""")

cursor.execute("""
	CREATE TABLE directors(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		director VARCHAR(32),
		director_id INTEGER,
		FOREIGN KEY(director_id) REFERENCES directors(id)

	);
	""")


cursor.execute("""
	CREATE TABLE movies_actors(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		movie_id INTEGER,
		actor_id INTEGER,
		FOREIGN KEY(movie_id) REFERENCES movies(id),
		FOREIGN KEY(actor_id) REFERENCES actors(actor_id)

	);
	""")

cursor.execute("""
	CREATE TABLE movies_directors(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		movie_id INTEGER,
		director_id INTEGER,
		FOREIGN KEY(movie_id) REFERENCES movies(id),
		FOREIGN KEY(director_id) REFERENCES directors(director_id)

	);
	""")


if __name__ == '__main__':


	cursor.execute('INSERT INTO movies(movie) VALUES(?);', ('movie1',))
	cursor.execute('INSERT INTO movies(movie) VALUES(?);', ('movie2',))
	cursor.execute('INSERT INTO movies(movie) VALUES(?);', ('movie3',))

	cursor.execute('INSERT INTO actors(actor, actor_id) VALUES(?,?);', ('actor1', 1))
	cursor.execute('INSERT INTO actors(actor, actor_id) VALUES(?,?);', ('actor2', 2))


	cursor.execute('INSERT INTO directors(director, director_id) VALUES(?,?);', ('director1', 1))
	cursor.execute('INSERT INTO directors(director, director_id) VALUES(?,?);', ('director2', 2))

	cursor.execute('INSERT INTO movies_actors(movie_id, actor_id) VALUES(?,?);', (1,1))
	cursor.execute('INSERT INTO movies_actors(movie_id, actor_id) VALUES(?,?);', (1,2))
	cursor.execute('INSERT INTO movies_actors(movie_id, actor_id) VALUES(?,?);', (2,1))
	cursor.execute('INSERT INTO movies_actors(movie_id, actor_id) VALUES(?,?);', (2,2))

	cursor.execute('INSERT INTO movies_directors(movie_id, director_id) VALUES(?,?);', (1,1))
	cursor.execute('INSERT INTO movies_directors(movie_id, director_id) VALUES(?,?);', (1,2))
	cursor.execute('INSERT INTO movies_directors(movie_id, director_id) VALUES(?,?);', (2,1))
	cursor.execute('INSERT INTO movies_directors(movie_id, director_id) VALUES(?,?);', (2,2))



	connection.commit()
	connection.close()









