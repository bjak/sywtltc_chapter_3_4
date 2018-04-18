"""Purchasing the ticket - Driving function"""

from movie_database import MOVIEGOERS

import take_cash
import movie_append
import remove_seat
import give_ticket

def purchase_ticket(movie, moviegoer):
    """Purchase Ticket Function"""

    if MOVIEGOERS[moviegoer]["cash"] > 5.0: #checking cash of moviegoer

        remove_seat.remove_seat(movie)
        take_cash.take_cash(moviegoer)
        movie_append.movie_append(movie, moviegoer)
        give_ticket.give_ticket(moviegoer)
