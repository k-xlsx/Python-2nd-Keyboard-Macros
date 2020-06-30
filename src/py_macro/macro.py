
class Macro:
    def __init__(self, func=None, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


    def run(self):
        if self.func:
            return self.func(*self.args, **self.kwargs)
