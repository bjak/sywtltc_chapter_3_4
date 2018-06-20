"""Print Database Function"""

from movie_database import MOVIE_DB
from movie_database import MOVIEGOERS
import pprint
movie = {"Xmen 8: The Xmennening", "The Bromance", "Gigli: The Play: The Book: The movie"}
customer = {"Bob", "Jim", "Cary"}

def print_db(movie, moviegoer):
    """Print Database Function"""
    customer = MOVIEGOERS[moviegoer]
    movies = MOVIE_DB[movie]

    pprint.pprint(customer)
    pprint.pprint(movie)
