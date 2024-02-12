"""
Challenge Docstring du 11/02/2024

Exercice: créer une liste chainée
"""

class Cnode:

    def __init__(self, valeur, next_node=None):
        self.val = valeur
        self.next = next_node

class Clist:

    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        chaine = "["
        if self.first:
            node = self.first
            while True:
                chaine += str(node.val)
                if node.next: node = node.next
                else: break
                chaine+=", "
        return chaine + "]"

    def __len__(self):
        compteur = 0
        if self.first:
            node = self.first
            while True:
                compteur += 1
                if node.next: node = node.next
                else: break
        return compteur

    def append(self, val:int|str) -> None:
        new_node = Cnode(val)
        if not self.last: # Pas encore de node donc on initialise first et last
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node # Ajout du nouveau node au next du dernier présent
            self.last = new_node # Changement du last pour y mettre le nouveau node

    def remove_at(self, index:int) -> None:
        if index >= self.__len__():
            raise IndexError()
        compteur = 0
        node = self.first
        while True:
            if compteur == index-1:
                node.next = node.next.next # Assimile le next du prochain à la place du prochain
                break
            else:
                compteur += 1
                node = node.next


