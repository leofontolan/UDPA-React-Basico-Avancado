from video import Video


class TvShow(Video):

    # Constructor using movie inheritance
    def __init__(self, title, duration, image_url, trailer_url,
                 info, season, episode, tv_station):
        Video.__init__(self, title, duration, image_url, trailer_url, info)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        pass
