
from random import randint


class Pysenbugger(object):

    def __init__(self, unbugged_function):
        self.unbugged_function = unbugged_function

    def catbox(self, *args, **kwargs):
        schroedinger = randint(1, 100)
        if schroedinger < 50:
            return None
        else:
            return self.unbugged_function(*args, **kwargs)


def pysenbug(unbugged_function, *args, **kwargs):
    meddlesome_physicist = Pysenbugger(unbugged_function)
    bugged_func = meddlesome_physicist.catbox
    return bugged_func
