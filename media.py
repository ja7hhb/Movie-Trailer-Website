import webbrowser

class Movie():
	""" This class provides a way to store movie related information """

	def __init__(self,movie_title,movie_released_year,movie_genre,movie_running_time,poster_image, trailer_youtube):
		self.title = movie_title
		self.released_year = movie_released_year
		self.genre = movie_genre
		self.running_time = movie_running_time
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_traiter(self):
		""" Opens trailer in a web browser """
		webbrowser.open(self.trailer_youtube_url)

