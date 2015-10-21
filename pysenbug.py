
from random import random
from functools import wraps
import sys


class Pysenbugger(object):

    def __init__(self, unbugged_function, *bug_args, **bug_kwargs):
        self.unbugged_function = unbugged_function
        self.chance = 0.5
        self.return_value = None
        self.prob_args = []
        self.prob_kwargs = {}

        # pysenbugs may be created with custom probability functions.
        # This function may optionally accept prob_args and prob_kwargs.
        # The function should return a boolean when called.
        # If the return value of self.probability_function is True, the
        # function decorated by pysenbug will return self.return_value;
        # if False, it will act normally.
        self.probability_function = self.default_probability_function

        for each_key in bug_kwargs:
            self.__dict__[each_key] = bug_kwargs[each_key]

    def default_probability_function(self, *prob_args, **prob_kwargs):
        return (random() > self.chance)

    def catbox(self, *args, **kwargs):
        if self.probability_function(*self.prob_args, **self.prob_kwargs):
            return self.return_value
        else:
            return self.unbugged_function(*args, **kwargs)


# To permit this decorator to be used either with
# or without parameters, we'll infer which mode
# it's being used in by checking its parameters.
# Reference:
#     https://www.stackoverflow.com/17119145/python-decorator-optional-argument

# This outer-level decorator catches arguments intended
# to modify the behavior of Pysenbugger instances.
def pysenbug(*bug_args, **bug_kwargs):

    no_bug_args = False

    if len(bug_args) == 1 and not bug_kwargs and callable(bug_args[0]):
        unbugged_function = bug_args[0]
        no_bug_args = True

    # This is the function factory that governs
    # which form of internal function is returned,
    # to permit decoration either with or without
    # actually calling the decorator:
    def pysenbug_wrapper(unbugged_function):

        # This is the function that sets up the Pysenbugger
        # instance used to dynamically bug the victim's function.
        @wraps(unbugged_function)
        def actual_bugged_function_injector(*args, **kwargs):
            meddlesome_physicist = Pysenbugger(unbugged_function,
                                               *bug_args, **bug_kwargs)
            bugged_func = meddlesome_physicist.catbox

            # Unlike in v. Nuclear Kitten, the optional
            # decorator needs support for partial args
            # via @functools.wraps. One consequence of
            # this is that actual_bugged_function_injector
            # needs to return the called version of catbox.
            return bugged_func(*args, **kwargs)

        return actual_bugged_function_injector

    if no_bug_args:
        return pysenbug_wrapper(unbugged_function)

    # If the decorator is called with parameters,
    # then it doesn't also need to be called here.
    return pysenbug_wrapper
