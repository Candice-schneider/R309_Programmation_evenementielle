import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        Lab = QLabel("Entrez votre température:")
        self.recup = QLineEdit()
        self.unit = QLabel()
        ok = QPushButton("ok")
        self.res = QLabel()
        self.choix = QComboBox()
        self.choix.addItem("Kelvin en Celsius ")
        self.choix.addItem("Celsius en Kelvin")
        self.choix.currentIndexChanged.connect(self.selectionchange)
        aide = QPushButton("?")

        # Ajout des composants au grid layout
        grid.addWidget(Lab, 0, 0)
        grid.addWidget(self.recup, 0, 1)
        grid.addWidget(self.unit, 0, 2)
        grid.addWidget(ok, 1, 0)
        grid.addWidget(self.res, 2, 0)
        grid.addWidget(self.choix, 1, 1)
        grid.addWidget(aide, 3, 3)

        ok.clicked.connect(self.selectionchange)

        self.setWindowTitle("Convertisseur température")
        aide.clicked.connect(self.action)

    def selectionchange(self):
        if self.choix.currentText() == "Kelvin en Celsius ":
            try:e
                envoi = float(self.recup.text())
            except ValueError:
                QMessageBox(text="Mauvaises valeures").exec()
            else:
                self.res.setText(f'Le résultat est de {float(envoi) - 273.15} °C.')
                self.unit.setText(f'K')

        else:
            try:
                envoi = float(self.recup.text())
            except:
                ValueError != float
                QMessageBox(text="Mauvaises valeures").exec()
            else:
                self.res.setText(f'Le résultat est de {float(envoi) + 273.15} K.')
                self.unit.setText(f'°C')

    def action(self):  # action de click sur ok
        QMessageBox(text="CONVERSION").exec()


if __name__ == '__main__':  # Execution de la fenêtre
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
