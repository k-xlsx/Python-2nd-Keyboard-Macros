"""
Module containing the Macro object
"""


class Macro:
    """
    Macro stores the function corresponding to it, as well as its args, kwargs
    """

    def __init__(self, func=None, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


    def run(self):
        """
        Runs the stored function with the given args, kwargs and
        returns the result
        """

        if self.func:
            return self.func(*self.args, **self.kwargs)
