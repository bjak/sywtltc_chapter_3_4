"""This code is for a Movie Ticketing System"""

from movie_database import MOVIE_DB

def remove_seat(movie):
    """Remove Seat from Movie Database"""

    MOVIE_DB[movie] = MOVIE_DB[movie] - 1
