"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""
import random

strategy_name = "start with random and use previous moves"

def move(my_history, their_history):
    pick = random.choice(["r", "p", "s"])



    # second move is always scissors
    if (len(their_history) == 0):
        return pick


    if (len(their_history) == 1):
        return "s"

    else:
        if their_history[-1] == "p":
            return "s"
        elif their_history[-1] == "r":
            return "p"
        else:
            return "r"
