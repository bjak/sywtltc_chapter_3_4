"""This code is for a Movie Ticketing System"""

from movie_database import MOVIEGOERS

def refund_cash(moviegoer):
    """Refund Cash Function"""

    MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] + 5.0
