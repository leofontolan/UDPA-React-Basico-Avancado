class Video:

    """ This class works to take advantage of the information that
    is always repeated in all movies"""
    def __init__(self, title, duration, image_url, trailer_url, info):
        self.title = title
        self.duration = duration
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url
        self.info = info
        pass

    # Function to show the title and duration of movie
    def show_info(self):
        print ("Title - " + self.title)
        print ("Duration - " + self.duration)
