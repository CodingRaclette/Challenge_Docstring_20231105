"""
Challenge Docstring du 11/02/2024

Exercice: créer une liste chainée
"""

class Cnode:

    def __init__(self, valeur:int|str, next_node=None):
        self.val = valeur
        self.next = next_node

    def __str__(self):
        if type(self.val) == str:
            return f"'{self.val}'"
        else:
            return str(self.val)


class Clist:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

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
        return self.length


    def append(self, val:int|str) -> None:
        self.length += 1
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
        self.length -= 1
        if self.length == 0:
            self.first = None
            self.last = None
        else:
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

        self.length += 1

        new_node = Cnode(value)
        if index == 0:
            new_node.next = self.first # Le node inséré reçoit l'actuel first en guise de n+1
            self.first = new_node # Le nouveau node devient alors le first
        elif index == len(self):
            self.append(value)
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

    def index_of(self, value:str|int) -> int:
        compteur = 0
        node = self.first
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
        if index >= len(self):
            raise IndexError(f"L'index {index} est trop élevé (Maximum: {len(self)}).")

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
        node = self.first
        while node:
            lcopy.insert(0, node.val)
            node = node.next
        self.first = lcopy.first
        self.last = lcopy.last


    def is_unique(self) -> bool:
        checklist=Clist()
        node = self.first
        while node:
            if checklist.contains(node.val):
                return False
            checklist.append(node.val)
            node = node.next
        return True