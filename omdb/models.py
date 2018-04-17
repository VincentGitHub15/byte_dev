import sqlite3
import DAO

#this connection is for the first method that does not use DAO methodology
connection = sqlite3.connect('internal_omdb.db', check_same_thread=False)
cursor = connection.cursor()

class Movie:

	def get_movie_info(movie):
		cursor.execute('SELECT * FROM movies WHERE movie=?;', (movie,))
		movie_info = cursor.fetchall()
		return movie_info


	#DAO method
	def check_for_movie(movie):
		return DAO.Movies.return_movie(movie)

	#DAO method
	def add_movie_to_db(omdb_obj):
		print(omdb_obj["Title"], omdb_obj["Actors"])
		return DAO.Movies.add_movie(omdb_obj)


	# def get_all_info(movie):
	# 	cursor.execute('SELECT movie_id FROM movies_actors WHERE movie=?;', (movie,))
	# 	all_info = cursor.fetchall()
	# 	return all_info



# class Actor:

# class Director:

