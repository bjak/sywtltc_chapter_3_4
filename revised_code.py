"""This code is for a Movie Ticketing System"""

from movie_database import MOVIE_DB, MOVIEGOERS, CASH

def check_cash(moviegoer):
    """Check to see if moviegoer has enough cash"""

    if MOVIEGOERS[moviegoer]["cash"] > 5.0:

        return True

    else:

        print("You do not have enough cash")

def take_cash(moviegoer):
    """Take Cash for Movie from Moviegoer"""

    if check_cash(moviegoer) == True:

        MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] - 5.0

def movie_append(moviegoer, movie):
    """Append Movie"""

    if check_cash() == True:

        MOVIEGOERS[moviegoer]["movies"].append(movie)

def remove_seat(movie):
    """Remove Seat from Movie Database"""

    if check_cash() == True:

        MOVIE_DB[movie] = MOVIE_DB[movie] - 1

def give_ticket(moviegoer):
    """Remove Seat from Movie database"""

    if check_cash() == True:

        MOVIEGOERS[moviegoer]["tickets"] = MOVIEGOERS[moveigoer]["tickets"] + 1

def check_ticket(moviegoer):
    """Check if moviegoer has ticket before refund"""

    if MOVIEGOERS[moviegoer]["tickets"] > 0:

        return True

def refund_cash(moviegoer):
    """Refund Cash Function"""

    if check_ticket == True:

        MOVIEGOERS[moviegoer]["cash"] = MOVIEGOERS[moviegoer]["cash"] + 5.0

def movie_remove(movie, moviegoer):
    """Remove Movie"""

    if check_ticket == True:

        MOVIEGOERS[moviegoer]["movies"].remove(movie)

def add_seat(movie):
    """Add Seat back to Movie database"""

    if check_ticket == True:

        MOVIE_DB[movie] = MOVIE_DB[movie] + 1

def refund_ticket():
    """Take Ticket back from Moviegoer"""

    if check_ticket == True:

        MOVIEGOERS[moviegoer]["tickets"] = MOVIERGOERS[moviegoer]["tickets"] - 1

def purchase_ticket(movie, moviegoer):
    """Purchase Ticker Function"""

    check_cash(moviegoer)
    take_cash(moviegoer)
    movie_append(movie, moviegoer)
    remove_seat(movie)
    give_ticket(moviegoer)

def refund(movie, moviegoer):

    check_ticket(moviegoer)
    refund_cash(moviegoer)
    movie_remove(movie, moviegoer)
    add_seat(movie)
    refund_ticket(moviegoer)
