"""
Jeu de tests unitaires pour vérification du challenge liste chainée
"""
import pytest
from liste_chainee.main import Clist, Cnode

class TestCase:
    @staticmethod
    def mock_list():
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        liste_test.append(30)
        return liste_test

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

    def test_append_str(self):
        liste_test = Clist()
        liste_test.append("lorem ipsum")
        assert str(liste_test) == "['lorem ipsum']"


    def test_append_two(self):
        liste_test = Clist()
        liste_test.append(3)
        liste_test.append(10)
        assert type(liste_test.first.next) == Cnode
        assert liste_test.first.next.val == 10
        assert liste_test.last.val == 10

    def test_append_multiple(self):
        liste_test = self.mock_list()
        assert str(liste_test) == "[3, 10, 30]"

    def test_len(self):
        liste_test = self.mock_list()
        assert len(liste_test) == 3

    def test_remove_at(self):
        liste_test = self.mock_list()
        assert str(liste_test) == "[3, 10, 30]"
        liste_test.remove_at(1)
        assert str(liste_test) == "[3, 30]"

    def test_remove_at_zero(self):
        liste_test = self.mock_list()
        assert str(liste_test) == "[3, 10, 30]"
        liste_test.remove_at(0)
        assert str(liste_test) == "[10, 30]"

    def test_remove_at_last(self):
        liste_test = self.mock_list()
        assert str(liste_test) == "[3, 10, 30]"
        liste_test.remove_at(2)
        assert str(liste_test) == "[3, 10]"

    def test_remove_only_val(self):
        liste_test = Clist()
        liste_test.append('3')
        liste_test.remove_at(0)
        assert liste_test.first is None
        assert liste_test.last is None



    def test_remove_at_OutOR(self):
        liste_test = self.mock_list()
        with pytest.raises(IndexError):
            liste_test.remove_at(3)

    def test_insert_0(self):
        liste_test = self.mock_list()
        liste_test.insert(0, 13)
        assert str(liste_test) == "[13, 3, 10, 30]"

    def test_insert_1(self):
        liste_test = self.mock_list()
        liste_test.insert( 1,13)
        assert str(liste_test) == "[3, 13, 10, 30]"

    def test_insert_2(self):
        liste_test = self.mock_list()
        liste_test.insert(2, 13)
        assert str(liste_test) == "[3, 10, 13, 30]"

    def test_insert_last(self):
        liste_test = self.mock_list()
        liste_test.insert(3, 13)
        assert str(liste_test) == "[3, 10, 30, 13]"

    def test_contains(self):
        liste_test = self.mock_list()
        assert liste_test.contains(3)
        assert liste_test.contains(10)
        assert liste_test.contains(30)
        assert not liste_test.contains(2)

    def test_index_of(self):
        liste_test = self.mock_list()
        assert liste_test.index_of(3) == 0
        assert liste_test.index_of(10) == 1
        assert liste_test.index_of(30) == 2
        assert liste_test.index_of(2) == -1

    def test_at_index(self):
        liste_test = self.mock_list()
        assert liste_test.at_index(0) == 3
        assert liste_test.at_index(1) == 10
        assert liste_test.at_index(2) == 30

    def test_reversed(self):
        liste_test = self.mock_list()
        liste_test.append(20)
        liste_test.append(100)
        liste_test.append(80)
        liste_test.reversed()
        assert str(liste_test) == "[80, 100, 20, 30, 10, 3]"
        assert liste_test.length == 6

    def test_is_unique(self):
        liste_test = self.mock_list()
        assert liste_test.is_unique() == True
        liste_test.append(3)
        assert liste_test.is_unique() == False
