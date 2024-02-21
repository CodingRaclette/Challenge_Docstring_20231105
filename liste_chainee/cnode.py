import inspect

def check_caller():
    return str(inspect.stack()[2].filename.split("\\")[-1]) == "clist.py"


class Cnode:

    def __init__(self, valeur:int|str, next_node=None):
        self._val = valeur
        self._next = next_node

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        if check_caller():
            self._val = value


    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if check_caller():
            self._next = value

    def __str__(self):
        if isinstance(self._val, str):
            return f"'{self._val}'"
        else:
            return str(self._val)

