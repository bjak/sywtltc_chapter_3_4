"""This code is for a Movie Ticketing System"""

from movie_database import MOVIEGOERS

import refund_cash
import movie_remove
import add_seat
import refund_ticket

def refund(movie, moviegoer):
    """Refund Ticket"""

    if MOVIEGOERS[moviegoer]["tickets"] > 0:

        refund_cash.refund_cash(moviegoer)
        movie_remove.movie_remove(movie, moviegoer)
        add_seat.add_seat(movie)
        refund_ticket.refund_ticket(moviegoer)
