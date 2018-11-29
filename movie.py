import webbrowser
from video import Video

class Movie(Video):

    """ This Class provides a way to store  movie related information"""

    #Constant to store the ratings of the movies
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #Constructor using movie inheritance
    def __init__(self, title, duration, image_url, trailer_url, info, year):
        Video.__init__(self, title, duration, image_url, trailer_url, info)
        self.year = year
        pass

    #Function to open the browser with Youtube URL
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
