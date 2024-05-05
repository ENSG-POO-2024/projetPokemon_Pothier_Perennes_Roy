# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:00:24 2024

@author: 33695
"""

import numpy as np
import sys
from map_poke1 import Ui_MainWindow
from pokemon3 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt


class XXXXWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, poke_list, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.sachaX = 310
        self.sachaY = 510
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_dir = 1
        self.sacha_moves = [0,0,0,0]
        self.name = "down0"
        
        self.up_limit = np.genfromtxt("up.txt", dtype = int, delimiter = ',')
        
        self.poke_list = poke_list
    
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
        if self.sacha_dy < 0:
            for limit in self.up_limit:
                pos, start, stop = limit
                #print(pos,start,stop,self.sachaX)
                if ((self.sacha_dy <= (self.sachaY - pos) <= 0) and
                    (start < self.sachaX < stop)):
                    self.sachaY = pos
                    break
        # if self.sachaX < 0:
        #     self.sachaX = 0
        # if self.sachaX > 1071:
        #     self.sachaX = 1071
        # if self.sachaY < 0:
        #     self.sachaY = 0
        # if self.sachaY > 696:
        #     self.sachaY = 696
    
    def check_pokemon(self):
        for pokemon in self.poke_list:
            dx = pokemon[1] - self.sachaX
            dy = pokemon[2] - self.sachaY
            if (0 < dx < 25) and (0 < dy < 19):
                self.label_p.show()
                
    
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
        
        self.label_2.setPixmap(QtGui.QPixmap("animation/" + self.name + ".png"))
        self.label_2.setGeometry(QtCore.QRect(self.sachaX, self.sachaY, 19, 25))
        
        
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = XXXXWindow(l_pika)
        mainWin.show()
        app.exec_()
    run_app()