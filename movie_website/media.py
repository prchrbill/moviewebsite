import webbrowser  # importing module to be used in our class


class Movie():  # creates way to store information about a movie,
                # particularly the title,storyline, poster image and trailer

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # This initializes the  Movie instance using the data provied by the
        # program that calls for this class to be used. That data is then
        # assigned to variables in that program(this time entertainment_center)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function will open the trailer for the self(movie). Have to import
    # the webbrowser module(begining of this file) for it to be used.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
