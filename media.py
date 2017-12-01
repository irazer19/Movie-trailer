import webbrowser

#Creating class Movie as a blueprint for all the movies.
class Movie():
    
    #Method to initialize all the instance variables.
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #Method used to open the movie trailer in a seperate window browser.
    def show_trailer(self):
        webbrowser.open(r"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
        

        
        
    
