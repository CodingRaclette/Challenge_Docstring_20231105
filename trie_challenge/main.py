"""
Challenge Docstring du 05/11/2023
Proposition de DualRaclette
V1.1
Date de début: 05/11/2023 - 13h52
Date de dernière proposition: 11/11/2023 - 00h19


Description:
Le challenge de cette semaine porte sur un thème très important dans l'univers de l'algorithmie.
Il s'agit de créer une trie ou arbre préfixe en français.
Cela doit rester simple mais complet, incluant sa représentation et au minimum les fonctions add() et contains().
"""

class Noeud:
    """
    Classe permettant de définir un noeud d'une trie.
    Attributs:
        - lettre: lettre courante du noeud
        - fin_cle: booléen indiquant si ce noeud est la fin d'un mot
        - parent: stocke l'adresse du Noeud parent. Utilisé notamment pour la reconstruction d'une clé
        - enfants: stocke les noeuds enfants. Utilisé notamment pour l'ajout de nouveaux mots à la trie.
    """

    def __init__(self, lettre:str, parent):
        """
        Initialise un noeud.
        :param lettre: lettre du noeud courant
        :param parent: noeud parent du noeud courant
        """
        self.lettre = lettre
        self.fin_cle = False
        self.parent = parent
        self.enfants = {} # Dictionnaire de forme: {"lettre": Noeud}

    def __str__(self):
        return self.lettre



class Trie:
    """
    Classe contenant le point de départ de la trie ainsi que les fonctions permettant de manipuler l'arbre.
    """

    def __init__(self):
        """
        Initialise la racine de la trie par un noeud simple sans parent.
        """
        self.racine = Noeud("", None)


    def __str__(self):
        """
        Méthode spéciale permettant de définir la valeur de l'objet lorsqu'il est converti en string.
        :return: chaîne de caractères à afficher
        """
        str_base = "|\n"

        # Utilisation d'une méthode récursive pour construire la str à afficher
        for enfant_racine in self.racine.enfants.values():
            str_base = self._construction_affichage(str_base, enfant_racine)

        return str_base

    def _construction_affichage(self, affichage, noeud_courant):
        """
        Fonction récursive permettant de construire la chaine de caractères représentant la trie
        :param affichage: chaine de caractere à construire, celle qui va être affichée à la fin.
        :param noeud_courant: noeud à afficher.
        :return: string à afficher
        """

        # === Construction du prefixe de chaque ligne ===
        prefix = ""
        if noeud_courant.parent != self.racine:
            branche = [] # doit contenir tous les noeuds de la branche du noeud courant n, à l'exception de lui même.
            last_n = noeud_courant.parent # last_n est initialisé avec le noeud du premier "parent" du noeud courant.

            while last_n != self.racine:
                branche.append(last_n)
                last_n = last_n.parent
            branche.reverse() # -> ordre du plus proche de la racine au plus proche du noeud courant

            for node in branche:
                prefix += "|  " if len(node.parent.enfants.keys()) > 1 and node != list(node.parent.enfants.values())[-1] else "   "
        affichage+=prefix


        # Vérification: si c'est le dernier noeud du dico, affichage avec underscores, sinon tirets

        affichage += f"|__{noeud_courant.lettre}" if noeud_courant == list(noeud_courant.parent.enfants.values())[-1] else f"|--{noeud_courant.lettre}"

        # Si le booléen indiquant la fin d'un mot est True, alors affichage du mot à la suite du noeud
        affichage += f" *[{''.join(self._reconstruction_cle(noeud_courant))}]" if noeud_courant.fin_cle else ""

        # Fin d'une ligne
        affichage += "\n"

        # Récursivité si le noeud courant possède des noeuds enfants.
        if noeud_courant.enfants.items():
            for enf in noeud_courant.enfants.values():
                affichage = self._construction_affichage(affichage, enf)
        elif noeud_courant != list(noeud_courant.parent.enfants.values())[-1]:
            affichage+=prefix+"|\n"
        else:
            affichage+=prefix+"\n"
        return affichage

    def _reconstruction_cle(self, n):
        """
        Fonction permettant de reconstituer une clé à partir de son dernier noeud
        :param n: dernier noeud d'une clé
        :return: clé
        """
        liste_lettres_cles = [n.lettre]
        if n.parent != self.racine:
            dernier_n = n
            while dernier_n.parent != self.racine:
                dernier_n = dernier_n.parent
                liste_lettres_cles.insert(0, dernier_n.lettre)
        return "".join(liste_lettres_cles)



    def add(self, mot:str):
        """
        Fonction permettant d'ajouter un mot à la trie
        :param mot: chaine de caractère à ajouter
        :return: None
        """
        dernier_noeud = self.racine
        for lettre in mot:
            if lettre not in dernier_noeud.enfants.keys():
                dernier_noeud.enfants[lettre] = Noeud(lettre, dernier_noeud)
            dernier_noeud = dernier_noeud.enfants[lettre]
        # Une fois sorti de la boucle, dernier_noeud garde le noeud ajouté.
        dernier_noeud.fin_cle = True # Donc changement de la valeur à True pour indiquer une fin de mot


    def contains(self, cle:str):
        """
        Méthode permettant de savoir si une clé donnée est présente dans la trie.
        :param cle: chaine de caractère à tester.
        :return: booléen indiquant si la chaine est présente dans la trie.
        """
        dernier_noeud = self.racine
        for lettre in cle: # Pour chaque lettre dans la clé
            if lettre in dernier_noeud.enfants.keys(): # Si la lettre est présente parmis les enfants du noeud de la lettre courante
                dernier_noeud = dernier_noeud.enfants[lettre] # On passe au noeud suivant (le noeud enfant)
            else: # Sinon la fonction renvoit directement False (permet d'arrêter en cours de
                return False
        # Si boucle se termine, alors la clé est présente dans la trie et True est donc renvoyé
        return True

    def _find_node(self, start:str):
        node = self.racine
        for letter in start:
            if letter in node.enfants.keys():
                node = node.enfants[letter]
        return node

    def _get_all_words(self, node, liste):
        if node.fin_cle:
            liste.append(self._reconstruction_cle(node))
        if node.enfants.keys():
            for enf in node.enfants.values():
                liste = self._get_all_words(enf, liste)
        return liste

    def give_words(self, start:str):
        node = self._find_node(start)
        liste_mots = self._get_all_words(node, [])
        return liste_mots





if __name__ == '__main__':

    liste_mots_exemple= ["à", "arbre", "art", "artiste", "chape", "chapeau", "créatif", "création", "œuf", "zèbre"]

    trie = Trie()

    for word in liste_mots_exemple:
        trie.add(word)

    print(trie)


    print("Contient 'arbre' ? ", trie.contains("arbre"))
    print("Contient 'Arbre' ? ", trie.contains("Arbre"))
    print("Contient 'pinceau' ? ", trie.contains("pinceau"))

