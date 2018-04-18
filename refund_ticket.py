"""This code is for a Movie Ticketing System"""

from movie_database import MOVIEGOERS

def refund_ticket(moviegoer):
    """Take Ticket back from Moviegoer"""

    MOVIEGOERS[moviegoer]["tickets"] = MOVIEGOERS[moviegoer]["tickets"] - 1
