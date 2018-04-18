"""Appending the Movie"""

from movie_database import MOVIEGOERS

def movie_append(movie, moviegoer):
    """Append Movie"""

    MOVIEGOERS[moviegoer]["movies"].append(movie)
