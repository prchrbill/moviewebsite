import fresh_tomatoes   # importing to call it to build movie trailer website #
import media            # contains the class, constructor, instance variables #

# very entertaining - even though critics hated it #
justice_league = media.Movie(
    "Justice League", "Batman builds a team",
    "https://upload.wikimedia.org/wikipedia/commons/8/8b/Justice_League_2017_film_logo.jpg",  # NOQA
    "https://www.youtube.com/watch?v=r9-DM9uBtVI"
    )

# best marvel movie - great challenge to the spiderman movie#
thor_ragnarok = media.Movie(
    "Thor Ragnarok", "Thor has to stop his Sister",
    "https://upload.wikimedia.org/wikipedia/commons/4/44/Thor_Ragnarok.jpg",
    "https://www.youtube.com/watch?v=ue80QwXMRHg")

# best Wolverine movie ever#
logan = media.Movie(
    "Logan", "A mutant on the run tries to save his daughter.",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=gbug3zTm3Ws"
    )

# the wedding singer takes me back to relive my highschool years in music#
wedding_singer = media.Movie(
    "The Wedding Singer", "Man wants to get married.",
    "https://upload.wikimedia.org/wikipedia/en/8/84/The_Wedding_Singer_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=_bhU3NsCIDs"
    )

# deadpool breaks the fourth wall and gives reynolds a good superhero movie #
deadpool = media.Movie(
    "Deadpool", "A mutant seeks revenge and to crack jokes",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
    "https://www.youtube.com/watch?v=gtTfd6tISfw"
    )

# the lego batman movie was hysterical#
lego_batman = media.Movie(
    "The Lego Batman Movie", "A millionare crime fighter learns"
    "he needs people.",
    "https://upload.wikimedia.org/wikipedia/en/6/61/The_Lego_Batman_Movie_PromotionalPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=rGQUKzSDhrg"
    )


movies = [justice_league, thor_ragnarok, logan, wedding_singer, deadpool,
          lego_batman]
fresh_tomatoes.open_movies_page(movies)
