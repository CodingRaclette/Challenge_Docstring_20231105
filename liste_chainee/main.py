"""
Challenge Docstring du 11/02/2024

Exercice: créer une liste chainée
"""

class Cnode:

    def __init__(self, valeur:int|str, next_node=None):
        self.val = valeur
        self.next = next_node

    def __str__(self):
        return str(self.val)


class Clist:

    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def __str__(self):
        chaine = ""
        if self.first:
            node = self.first
            while node:
                chaine += str(node)
                node = node.next
                if node: chaine+=", "
        return f"[{chaine}]"

    def __len__(self):
        return self.lenght


    def append(self, val:int|str) -> None:
        self.lenght += 1
        new_node = Cnode(val)
        if not self.last: # Pas encore de node donc on initialise first et last
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node # Ajout du nouveau node au next du dernier présent
            self.last = new_node # Changement du last pour y mettre le nouveau node

    def remove_at(self, index:int) -> None:
        # Gestion d'input en index
        if index >= len(self):
            raise IndexError(f"L'index {index} est trop élevé.")
        self.lenght -= 1

        if index == 0:
            # Si premier élément, on change juste le first au n+1
            self.first = self.first.next
        else:
            compteur = 0
            node = self.first
            while node:
                if compteur == index-1:
                    # Assimile le node n+2 au node n à la place du node n+1
                    # Si l'index pointe le dernier élément de la liste, n+1 = None
                    node.next = node.next.next if node.next.next else None
                    break
                compteur += 1
                node = node.next

    def insert(self, index:int, value:str|int) -> None:
        # Gestion d'input en index
        if index > len(self):
            raise IndexError(f"L'index {index} est trop élevé.")

        self.lenght += 1

        new_node = Cnode(value)
        if index == 0:
            new_node.next = self.first # Le node inséré reçoit l'actuel first en guise de n+1
            self.first = new_node # Le nouveau node devient alors le first
        else:
            compteur = 0
            node = self.first
            while node:
                if compteur == index - 1:
                    new_node.next = node.next
                    node.next = new_node
                    break
                compteur+=1
                node = node.next

    def contains(self, value:str|int) -> bool:
        compteur = 0
        node = self.first
        while node:
            if value == node.val:
                return True
            compteur += 1
            node = node.next
        return False

    def index_of(self, value:str|int) -> int:
        compteur = 0
        node = self.first
        while node:
            if value == node.val:
                return compteur
            compteur += 1
            node = node.next
        return -1

    def at_index(self, index:int) -> int|str:
        if index >= len(self):
            raise IndexError(f"L'index {index} est trop élevé.")

        compteur = 0
        node = self.first
        while node:
            if compteur == index:
                return node.val
            compteur += 1
            node = node.next

    def reversed(self):
        lenght = self.lenght
        node = self.first
        compteur = 1
        while compteur<=lenght:
            self.insert(lenght, node.val)
            node = node.next
            compteur += 1
        self.first = node
