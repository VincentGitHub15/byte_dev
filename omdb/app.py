from flask import Flask, jsonify, request
import queryOMDb, models


app = Flask(__name__)


@app.route('/search-movie/<movie>/<search_type>', methods=['GET'])
def search_movie(movie, search_type):
    
	if search_type=='1':
		'''
		Call on the models to retreive the movie title from db
		'''
		movie_info = jsonify(models.Movie.get_movie_info(movie))
		return movie_info

	elif search_type=='2':
		'''
		Call on queryOMDb to search for the movie title on OMDb API
		'''
		omdb = queryOMDb.Wrapper.queryOMDb_API(movie)
		
		if omdb["Error"]:
			omdb = jsonify(omdb["Error"])
			return omdb

		else:
			omdb = jsonify(omdb["Title"], omdb["Director"], omdb["Actors"])
			return omdb
		

	else:
		response = jsonify(error="choose 1 or 2 as search type")
		response.status_code = 404
		return response

@app.route('/add-movie/<movie>', methods=['GET'])
def add_movie(movie):
	if movie:
		#check if movie in internal db

		check_for_movie = models.Movie.check_for_movie(movie)
		
		if check_for_movie:
			omdb = jsonify(check_for_movie[0], "movie already in db!")
			return omdb
		
		else:
			#go to API
			omdb_obj = queryOMDb.Wrapper.queryOMDb_API(movie)
			movie_added = models.Movie.add_movie_to_db(omdb_obj)
			omdb = jsonify(omdb_obj["Title"] + " has been added to db")
			# api_obj = jsonify(omdb_obj["Title"], omdb_obj["Director"], omdb_obj["Actors"])
			return omdb
			# return



if __name__ == '__main__':
	app.run(debug=True)