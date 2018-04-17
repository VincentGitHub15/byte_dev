import sqlite3



class DataBase:

	def our_execute(movie, statement, params):

		connection = sqlite3.connect('internal_omdb.db', check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute(statement, params)
		results = cursor.fetchall()
		connection.commit()
		connection.close()

		return results


class Movies(DataBase):

	def return_movie(movie):
		params = (movie,)
		statement = """
			SELECT * FROM movies WHERE movie=?;

		"""
		movie_query = DataBase.our_execute(movie, statement, params)
		return movie_query


	def add_movie(omdb_obj):
		title = omdb_obj["Title"]
		params = (omdb_obj["Title"],)
		statement = """
			INSERT INTO movies (movie) VALUES(?);

			"""
		DataBase.our_execute(title, statement, params)
		return title








