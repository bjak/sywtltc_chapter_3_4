"""This code is for a Movie Ticketing System"""

from movie_database import MOVIEGOERS

def take_cash(moviegoer):
    """Take Cash for Movie from Moviegoer"""

    MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] - 5.0
