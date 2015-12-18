
from random import random
from functools import wraps


class Pysenbugger(object):

    def __init__(self, unbugged_function, *bug_args, **bug_kwargs):
        """ Initialize a Pysenbugger instance for managing state related
        to pysenbugs.

        Pysenbugger instances may be created with custom probability functions.
        - These functions may optionally accept `prob_args` and `prob_kwargs`.
        - The function should return a boolean when called.
        - If the return value of calling `probability_function` is True, the
        function decorated by `pysenbug` will return this instance's
        `return_value` attribute; if False, it will act normally.
        """
        self.unbugged_function = unbugged_function
        self.chance = 0.5
        self.return_value = None
        self.prob_args = []
        self.prob_kwargs = {}
        self.probability_function = self.default_probability_function

        # This permits optionally overwriting any Pysenbugger attribute.
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

def pysenbug(*bug_args, **bug_kwargs):

    """ Decorate a function with another function intended to modify the
    reliability of the decorated function by changing whether or not the base
    function is called when the decorated function is called, or altering what
    is returned by the decorated function.

    This outer-level decorator catches and handles arguments intended to modify
    the behavior of Pysenbugger instances, which manage state related to the
    actual replacement of the base function.
    """

    no_bug_args = False

    if len(bug_args) == 1 and not bug_kwargs and callable(bug_args[0]):
        unbugged_function = bug_args[0]
        no_bug_args = True

    def _pysenbug_wrapper(unbugged_function):
        """ Return a function bugged with a Pysenbugger substitution method
        without calling it.
        """

        # This intermediate level function wrapping is required due to the need
        # to distinguish between a decorator used with arguments and one
        # without, combined with the necessity of accepting a separate set of
        # arguments when the bugged function itself is called.
        @wraps(unbugged_function)
        def actual_bugged_function_injector(*args, **kwargs):
            """ Set up a Pysenbugger instance to handle state related to method
            substitution, and return the result of calling that instance's
            substitution method with all variables passed to this method.
            """
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
        return _pysenbug_wrapper(unbugged_function)

    # If the decorator is called with parameters,
    # then it doesn't also need to be called here.
    return _pysenbug_wrapper
