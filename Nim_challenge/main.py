"""

## 🔶 Jeu de Nim
Mais qui va tomber sur le dernier ?

👉 Le but de ce challenge est de développer le jeu de [Nim](https://fr.wikipedia.org/wiki/Jeux_de_Nim), chaque joueur prend entre 1 et 3 bâtonnets à son tour, celui qui obtient le dernier à perdu.

🔹 **Étapes**
1. Afficher n bâtonnets sur une seule ligne
2. Gérer le jeu entre le joueur et le choix aléatoire de l'ordinateur.
**Bonus** : Développer une *IA* pour faire gagner l'ordinateur à tous les coups (en modifiant la fonction aléatoire)

"""

import random
import time



class Joueur:

    def __init__(self, nom="Billy", ia=False):
        self.nom = nom
        self.choix = self._choix_ia if ia else self._choix_humain


    @staticmethod
    def _choix_ia(nbmax, nb_bat):
        # choix = random.choice(range(1,nbmax+1))
        # Nooby est trop naze, il faut l'évoluer
        # La stratégie gagnante selon Wiki, est de toujours laisser un nombre congru à 1 modulo 4
        # Donc (nb_batonnets - choix - 1) % 4 = 0
        for i in range(1,nbmax+1):
            print(i, (nb_bat-i-1)%4)
            if (nb_bat - i - 1) % 4 == 0:
                return i
        return 1
    @staticmethod
    def _choix_humain(nbmax, *args):
        while True:
            choix = int(input(f"Combien de batonnets voulez-vous prendre (1 à {nbmax}) ? "))
            if choix in range(1, nbmax+1):
                print(choix)
                return choix
            # else:
            #     print(f"Il faut choisir entre 1 et {nbmax} batonnets")
            #     return self._choix_humain(nbmax, nb_bat)



class Partie:

    def __init__(self, joueurs:list):
        self.nbb = 20
        self.joueur=joueurs

    def affichage_batonnet(self):
        print(("".join(["# " * self.nbb])+"\n")*3)

    def tour(self, joueur_actuel):
        nbmax = self.nbb if self.nbb < 3 else 3
        ch = joueur_actuel.choix(nbmax, self.nbb)
        print(ch)
        print("Choix: ", ch, "batonnets")
        self.nbb -= ch

    def game(self):
        print(f"Début du jeu !")

        ntour = 0
        while True:
            j = self.joueur[ntour%2]
            time.sleep(1)
            print(f"\n=== Tour de {j.nom} ===\n")
            print(f"Il y a {self.nbb} batonnets:")
            self.affichage_batonnet()
            self.tour(j)
            if self.nbb < 1:
                print(f"{j.nom} a perdu !\nFin de la partie !")
                return
            ntour+=1



if __name__ == '__main__':
    nom_joueur = input("Quel est votre nom: ")
    listejoueurs = [Joueur(nom_joueur), Joueur("Nooby", ia=True)]
    partie = Partie(listejoueurs)
    partie.game()