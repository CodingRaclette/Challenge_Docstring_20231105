"""
Script déployant une interface graphique afin d'intégrer la trie dans un input utilisateur
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtCore import QSize, QPoint
from main import Trie

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.line.textChanged.connect(self.actutrie)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def actutrie(self):
        if len(self.line.text()) > 2:
            if trie.contains(self.line.text()):
                print(trie.give_word(self.line.text(), 10))

if __name__ == "__main__":

    print("Initialisation Trie")
    trie = Trie()
    with open('liste_francais.txt', 'r', encoding='utf-8') as f:
        for word in [x.strip('\n') for x in f.readlines()]:
            trie.add(word)
        print("Trie initialisée")
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )