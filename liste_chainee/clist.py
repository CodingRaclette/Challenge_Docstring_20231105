"""
Challenge Docstring du 11/02/2024

Exercice: créer une liste chainée
"""

from liste_chainee.cnode import Cnode

class Clist:

    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        pass

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        pass

    @property
    def length(self):
        return

    @length.setter
    def length(self, value):
        pass

    def __str__(self):
        chaine = ""
        if self._first:
            node = self._first
            while node:
                chaine += str(node)
                node = node.next
                if node: chaine+=", "
        return f"[{chaine}]"

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        return self.at_index(item)

    def _gestion_index(self, index, lastok=False):
        if not isinstance(index, int):
            raise IndexError(f"L'index doit être un entier. {index} n'en est pas un.")
        elif (not lastok and index >= len(self)) or (lastok and index > len(self)):
            raise IndexError(f"L'index {index} est trop élevé par rapport à la longueur de la liste: {len(self)}.")
        elif index < 0:
            if (index * -1) <= len(self):
                return len(self) + index
            else:
                raise IndexError(f"L'index {index * -1} est trop élevé par rapport à la longueur de la liste: {len(self)}.")
        else:
            return index

    def append(self, val:int|str) -> None:
        self._length += 1
        new_node = Cnode(val)
        if not self._last: # Pas encore de node donc on initialise first et last
            self._first = new_node
        else:
            self._last._next = new_node # Ajout du nouveau node au next du dernier présent
        self._last = new_node # Changement du last pour y mettre le nouveau node

    def remove_at(self, index:int) -> None:
        # Gestion d'input en index
        index = self._gestion_index(index)

        self._length -= 1
        if len(self) == 0:
            self._first = None
            self._last = None
        elif index == 0:
            # Si premier élément, on change juste le first au n+1
            self._first = self._first.next
        else:
            compteur = 0
            node = self._first
            while node:
                if compteur == index-1:
                    # Assimile le node n+2 au node n à la place du node n+1
                    # Si l'index pointe le dernier élément de la liste, n+1 = None
                    node._next = node.next.next if node.next.next else None
                    print(index, len(self))
                    if index == len(self):
                        self._last = node.next if node.next else node
                    break
                compteur += 1
                node = node.next

    def insert(self, index:int, value:str|int) -> None:
        # Gestion d'input en index
        index = self._gestion_index(index, lastok=True)

        self._length += 1

        new_node = Cnode(value)
        if index == 0:
            new_node._next = self._first # Le node inséré reçoit l'actuel first en guise de n+1
            self._first = new_node # Le nouveau node devient alors le first
        elif index == len(self):
            self.append(value)
        else:
            compteur = 0
            node = self._first
            while node:
                if compteur == index - 1:
                    new_node.next = node.next
                    node.next = new_node
                    break
                compteur+=1
                node = node.next

    def index_of(self, value:str|int) -> int:
        compteur = 0
        node = self._first
        while node:
            if value == node.val:
                return compteur
            compteur += 1
            node = node.next
        return -1

    def contains(self, value:str|int) -> bool:
        if self.index_of(value) == -1:
            return False
        else:
            return True

    def at_index(self, index:int) -> int|str:
        index = self._gestion_index(index)

        compteur = 0
        node = self.first
        while node:
            if compteur == index:
                return node.val
            compteur += 1
            node = node.next

    ## Déprecié
    # def reversed(self) -> None:
    #     length = self.length
    #     node = self.first
    #     compteur = 1
    #     while compteur<=length:
    #         self.insert(length, node.val)
    #         node = node.next
    #         compteur += 1
    #     self.first = node
    #     self.length = length

    def reversed(self) -> None:
        lcopy = Clist()
        node = self._first
        while node:
            lcopy.insert(0, node.val)
            node = node.next
        self._first = lcopy._first
        self._last = lcopy._last


    def is_unique(self) -> bool:
        checklist=Clist()
        node = self._first
        while node:
            if checklist.contains(node.val):
                return False
            checklist.append(node.val)
            node = node.next
        return True