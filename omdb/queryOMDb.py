import requests
import app


class Wrapper:

	def queryOMDb_API(movie):

		# omdb = requests.get("http://www.omdbapi.com/?t=rick+and+morty&apikey=yourkeyhere!").json()		
		omdb = requests.get("http://www.omdbapi.com/?t=" + movie + "&apikey=yourkeyhere!").json()
		return omdb