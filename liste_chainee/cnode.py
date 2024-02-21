
class Cnode:

    def __init__(self, valeur:int|str, next_node=None):
        self._val = valeur
        self._next = next_node

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        pass


    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        pass

    def __str__(self):
        if isinstance(self._val, str):
            return f"'{self._val}'"
        else:
            return str(self._val)

