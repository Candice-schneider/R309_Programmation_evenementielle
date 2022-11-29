import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        Lab = QLabel("Entrez votre prénom")
        self.recup = QLineEdit()
        ok = QPushButton("ok")
        self.res = QLabel()
        quitter = QPushButton("quitter")

        # Ajout des composants au grid layout
        grid.addWidget(Lab, 0, 0)
        grid.addWidget(self.recup, 0, 1)
        grid.addWidget(ok, 1, 0)
        grid.addWidget(self.res, 2, 0)
        grid.addWidget(quitter, 3, 0)

        ok.clicked.connect(self.actionOk)
        quitter.clicked.connect(self.actionQuitter)

        self.setWindowTitle("Politesse")

    def actionOk(self):  # action de click sur ok
        envoi = self.recup.text()
        self.res.setText(f'Bonjour {envoi}.')


    def actionQuitter(self):  # Action de clicker sur "quitter"
        QApplication.exit(0)


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    app.exec()
