"""Adding a Seat to the database"""

from movie_database import MOVIE_DB

def add_seat(movie):
    """Add Seat back to Movie database"""

    MOVIE_DB[movie] = MOVIE_DB[movie] + 1
