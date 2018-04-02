import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    #initializes object with variables,movie_title, poster_image and trailer_youtube
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #opens trailer in youtube for the object
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
