from math import random


def generate_random_player(database):
    # search through database
    index = random.randrange(0, len(database))
    player = database.get(index)
    return player
