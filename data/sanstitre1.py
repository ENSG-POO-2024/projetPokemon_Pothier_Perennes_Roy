# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:19:49 2024

@author: 33695
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clignotement d'image")
        self.setGeometry(100, 100, 300, 300)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 200)

        # Chargez les deux images à clignoter
        self.image1 = QPixmap("images/pokemon/blanc/6.png")
        self.image2 = QPixmap("images/pokemon/rouge/6.png")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.toggle_image)
        self.interval = 200  # Intervalle de temps entre chaque changement d'image en millisecondes
        self.duration = 2000  # Durée totale du clignotement en millisecondes
        self.total_time_elapsed = 0
        self.is_image1 = True  # Commencez avec la première image affichée

    def start_blinking(self):
        self.timer.start(self.interval)

    def toggle_image(self):
        # Alterner entre les deux images
        if self.is_image1:
            self.label.setPixmap(self.image2)
            
        else:
            self.label.setPixmap(self.image1)
        self.is_image1 = not self.is_image1

        # Vérifiez si la durée totale du clignotement est écoulée
        self.total_time_elapsed += self.interval
        if self.total_time_elapsed >= self.duration:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start_blinking()
    sys.exit(app.exec_())
