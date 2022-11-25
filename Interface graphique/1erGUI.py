import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
root = QWidget()  # Création fenêtre
root.resize(250, 250)  # taille fenêtre
root.setWindowTitle("Test")  # Nom fenêtre
root.show()  # Ouverture de la fenêtre

if __name__ == '__main__':
    sys.exit(app.exec_())
