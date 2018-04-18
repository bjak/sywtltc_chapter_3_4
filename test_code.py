"""Tests for Code.py"""

import purchase_ticket
import movie_database
#from revised_code import purchase_ticket, refund_ticket

def test_purchase_ticket():
    """Test Purchase Function"""

    purchase_ticket.purchase_ticket("Xmen 8: The Xmennening", "Ricci")

    assert movie_database.MOVIE_DB["Xmen 8: The Xmennening"] == 10
    assert movie_database.MOVIEGOERS["Ricci"]["cash"] == 4.0
    assert movie_database.MOVIEGOERS["Ricci"]["tickets"] == 0

    purchase_ticket.purchase_ticket("The Bromance", "Cary")

    assert movie_database.MOVIE_DB["The Bromance"] == 19
    assert movie_database.MOVIEGOERS["Cary"]["cash"] == 115.0
    assert movie_database.MOVIEGOERS["Cary"]["tickets"] == 1

    purchase_ticket.purchase_ticket("Gigli: The Play: The Book: The movie", "Bob")

    assert movie_database.MOVIE_DB["Gigli: The Play: The Book: The movie"] == 101
    assert movie_database.MOVIEGOERS["Bob"]["cash"] == 95.0
    assert movie_database.MOVIEGOERS["Bob"]["tickets"] == 1
