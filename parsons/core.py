import inspect
from random import sample


class ParsonsProblem():

    def __init__(self, obj, tabs=4):
        self.obj_name, self.obj_module = obj.__name__, obj.__module__
        self.src = []

        # TODO: Handle exceptions!
        src = inspect.getsourcelines(obj)[0]

        for line_number, line in enumerate(src):
            self.src.append((line.strip(),
                             line_number,
                             (len(line.expandtabs(tabs)) - len(line.lstrip())) // tabs))


    def generate(self):
        return [line[0] for line in sample(self.src, len(self.src))]


    def solution(self):


    def __repr__(self):
        return '<{}: {}:{}>'.format(self.__class__.__name__, self.obj_module, self.obj_name)
