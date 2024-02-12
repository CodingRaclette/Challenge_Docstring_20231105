"""
Jeu de tests unitaires pour vérification du challenge liste chainée
"""
import pytest
from liste_chainee.main import Clist, Cnode

class TestCase:

    def test_creation_liste_vide(self):
        liste_test = Clist()
        assert str(liste_test) == "[]"

    def test_append_one(self):
        liste_test = Clist()
        liste_test.append(13)
        assert str(liste_test) == "[13]"
        assert liste_test.first.val == 13
        assert liste_test.first is liste_test.last
        assert liste_test.first.next is None

    def test_append_two(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        assert type(liste_test.first.next) == Cnode
        assert liste_test.first.next.val == 10
        assert liste_test.last.val == 10

    def test_append_multiple(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        liste_test.append(30)
        assert str(liste_test) == "[3, 10, 30]"

    def test_len(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        liste_test.append(30)
        assert len(liste_test) == 3

    def test_remove_at(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        liste_test.append(30)
        assert str(liste_test) == "[3, 10, 30]"
        liste_test.remove_at(1)
        assert str(liste_test) == "[3, 30]"

    def test_remove_at_OOR(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        liste_test.append(30)
        with pytest.raises(IndexError):
            liste_test.remove_at(4)