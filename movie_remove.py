"""Removing appended movie"""

from movie_database import MOVIEGOERS

def movie_remove(movie, moviegoer):
    """Remove Movie"""

    MOVIEGOERS[moviegoer]["movies"].remove(movie)
