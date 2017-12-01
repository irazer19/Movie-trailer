import webbrowser


class Movie():
    """Creating class Movie as a blueprint for all the movies."""
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        """Method to initialize all the instance variables."""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Method used to open the movie trailer in a seperate
           window browser."""
        webbrowser.open(r"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
