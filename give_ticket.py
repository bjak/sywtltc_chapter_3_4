"""This code is for a Movie Ticketing System"""

from movie_database import MOVIEGOERS

def give_ticket(moviegoer):
    """Remove Seat from Movie database"""

    MOVIEGOERS[moviegoer]["tickets"] = MOVIEGOERS[moviegoer]["tickets"] + 1
