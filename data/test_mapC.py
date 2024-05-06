# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:00:24 2024

@author: 33695
"""

import numpy as np
import sys
from gui import Ui_MainWindow
from pokemon3 import *
from initialisation import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt

    # def setupUi(self, MainWindow):
    #     # Code précédent...

    #     self.play.clicked.connect(self.remove_labels)

    # def remove_labels(self):
    #     self.gros_sacha.hide()
    #     self.pokemon_sauvage.hide()
    #     self.label.hide()
class GameWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, wild, starting_pack, atk_lib, parent=None):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.load_map)
        self.load_screen_title()
        
        self.sachaX = 390
        self.sachaY = 580
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_dir = 1
        self.sacha_moves = [0,0,0,0]
        self.name = "down0"
        
        #self.up_limit = np.genfromtxt("up.txt", dtype = int, delimiter = ',')
        
        self.wild = wild
        self.team = Team(starting_pack)
        self.atk_lib = atk_lib
    
    
    def hide_em_all(self):
        self.coeur1.hide()
        self.coeur2.hide()
        self.coeur3.hide()
        self.inventory.hide()
        self.sacha.hide()
        self.fondcombat.hide()
        self.vs.hide()
        self.nompoke.hide()
        self.nompokesauvage.hide()
        self.progressBarpokesauvage.hide()
        self.progressBar_notre.hide()
        self.imagepokesauvage.hide()
        self.impagepoke.hide()
        self.gros_sacha.hide()
        self.pokemon_sauvage.hide()
        self.label.hide()
        self.inventory2.hide()
        self.play.hide()
        
    
    def load_screen_title(self):
        self.hide_em_all()
        self.gros_sacha.show()
        self.pokemon_sauvage.show()
        self.label.show()
        self.inventory2.show()
        self.play.show()
        
    
        self.sacha.setFocus()
    
    def load_map(self):
        self.hide_em_all()
        self.coeur1.show()
        self.coeur2.show()
        self.coeur3.show()
        self.inventory.show()
        self.sacha.show()
    
        self.sacha.setFocus()
        
        
    
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.set_dxdy(0)
        
        if event.key() == Qt.Key_Down:
            self.set_dxdy(1)
        
        if event.key() == Qt.Key_Left:
            self.set_dxdy(2)
        
        if event.key() == Qt.Key_Right:
            self.set_dxdy(3)
        
        self.update_position()
    
    def keyReleaseEvent(self, event):
        
        if event.key() == Qt.Key_Up:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Down:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Left:
            self.sacha_dx = 0
        
        if event.key() == Qt.Key_Right:
            self.sacha_dx = 0
        
    
    def set_dxdy(self,direction):
        self.sacha_dir = direction
        dx = {0:self.sacha_dx, 1:self.sacha_dx, 2:-4, 3:4}[direction]
        dy = {0:-4, 1:4, 2:self.sacha_dy, 3:self.sacha_dy}[direction]
        
        if dx != 0 and dy != 0:
            self.sacha_dx = round(dx * 3/4)
            self.sacha_dy = round(dy * 3/4)
        else:
            self.sacha_dx = dx
            self.sacha_dy = dy
        
    
    def check_position(self):
        # if self.sacha_dy < 0:
        #     for limit in self.up_limit:
        #         pos, start, stop = limit
        #         #print(pos,start,stop,self.sachaX)
        #         if ((self.sacha_dy <= (self.sachaY - pos) <= 0) and
        #             (start < self.sachaX < stop)):
        #             self.sachaY = pos
        #             break
        if self.sachaX < 0:
            self.sachaX = 0
        if self.sachaX > 1071:
            self.sachaX = 1071
        if self.sachaY < 0:
            self.sachaY = 0
        if self.sachaY > 696:
            self.sachaY = 696
    
    def check_pokemon(self):
        for pokemon in self.wild:
            dx = pokemon[1] - self.sachaX
            dy = pokemon[2] - self.sachaY
            if (-25 < dx < 25) and (-26 < dy < 19):
                self.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon[0].id_pok - 1) + ".png"))
                self.pokemon_sauvage.setGeometry(QtCore.QRect(pokemon[1], pokemon[2], 25, 26))
                self.pokemon_sauvage.show()

    
    def update_position(self):
        self.sachaX += self.sacha_dx
        self.sachaY += self.sacha_dy
        self.check_position()
        self.check_pokemon()
        
        name = {0:"up", 1:"down", 2:"left", 3:"right"}[self.sacha_dir]
        order = self.sacha_moves[self.sacha_dir]
        if (order % 6) == 4:
            self.name = name + "0"
        elif (order % 12) == 1:
            self.name = name + "1"
        elif (order % 12) == 7:
            self.name = name + "2"
        
        self.sacha_moves[self.sacha_dir] += 1
        
        self.sacha.setPixmap(QtGui.QPixmap("images/animation/" + self.name + ".png"))
        self.sacha.setGeometry(QtCore.QRect(self.sachaX, self.sachaY, 19, 25))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow(wild, starting_pack, atk_lib)
    window.show()
    window.sacha.setFocus()
    sys.exit(app.exec_())
        
        
# if __name__ == "__main__":
#     window.label_2.setFocus()
#     def run_app():
#         app = QApplication(sys.argv)
#         mainWin = GameWindow(l_pika)
#         mainWin.show()
        
#         app.exec_()
#     run_app()