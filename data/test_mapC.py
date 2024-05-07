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
#from fight_engine import fight
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt


class GameWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, wild, starting_pack, atk_lib, parent=None):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.load_map)
        self.inventory2.clicked.connect(self.load_inventary)
        self.pushButton_inv.clicked.connect(self.load_screen_title)
        self.inventory.clicked.connect(self.load_inventary)
        self.inventory2.clicked.connect(self.load_inventary)
        #self.bp1.clicked.connect(self.pushButton_2)
        self.bp1.clicked.connect(self.show_vertical_layout)
        self.bp2.clicked.connect(self.show_vertical_layout)
        self.bp3.clicked.connect(self.show_vertical_layout)
        self.bp4.clicked.connect(self.show_vertical_layout)
        self.bp5.clicked.connect(self.show_vertical_layout)
        self.bp6.clicked.connect(self.show_vertical_layout)
        
  
        self.pushButton_3.clicked.connect(self.hide_widget_inventraire)
        self.case = 1 
        self.pushButton_2.clicked.connect(self.hide_vertical_layout)
        self.pushButton_3.clicked.connect(self.hide_vertical_layout)
        
        self.load_screen_title()
        
        self.sachaX = 390
        self.sachaY = 580
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_dir = 1
        self.sacha_moves = [0,0,0,0]
        self.name = "down0"
        
        self.up_limit    = np.genfromtxt("bounds/up.txt"   , dtype = int, delimiter = ',')
        self.down_limit  = np.genfromtxt("bounds/down.txt" , dtype = int, delimiter = ',')
        self.left_limit  = np.genfromtxt("bounds/left.txt" , dtype = int, delimiter = ',')
        self.right_limit = np.genfromtxt("bounds/right.txt", dtype = int, delimiter = ',')
        
        self.wild = wild
        self.team = Team(starting_pack)
        self.atk_lib = atk_lib
        
    def show_vertical_layout(self):
        
        #self.verticalLayout.show()
        self.verticalLayoutWidget_inv.setVisible(True)
        sender = self.sender()  # Récupérer le widget qui a émis le signal
        if sender == self.bp1:
            self.verticalLayoutWidget_inv.move(400, 200)
            self.case = 1 
              
        elif sender == self.bp2:
            self.verticalLayoutWidget_inv.move( 600, 200)
            self.case = 2
            
        elif sender == self.bp3:
            self.verticalLayoutWidget_inv.move( 800, 200 )
            self.case = 3
            
        elif sender == self.bp4:
            self.verticalLayoutWidget_inv.move(400, 400)
            self.case = 4
            
        elif sender == self.bp5:
            self.verticalLayoutWidget_inv.move(600,400)
            self.case = 5
            
        elif sender == self.bp6:
            self.verticalLayoutWidget_inv.move(800,400)
            self.case = 6
            
    def hide_widget_inventraire(self):
        if self.case==1:
            self.image1.hide()
            self.nom1.hide()
            self.pv1.hide()
            
        if self.case==2:
            self.image2.hide()
            self.nom2.hide()
            self.pv2.hide()
            
        if self.case==3:
            self.image3.hide()
            self.nom3.hide()
            self.pv3.hide()
            
        if self.case==4:
            self.image4.hide()
            self.nom4.hide()
            self.pv4.hide()
            
        if self.case==5:
            self.image5.hide()
            self.nom5.hide()
            self.pv5.hide()
            
        if self.case==6:
            self.image6.hide()
            self.nom6.hide()
            self.pv6.hide()
            
            
            
        #self.verticalLayoutWidget_inv.setVisible(True)
          # Récupérer le widget qui a émis le signal

            
    
    def hide_vertical_layout(self):
        self.verticalLayoutWidget_inv.setVisible(False)

        
    
    
    def cache_em_all(self):
        self.coeur1.hide()
        self.coeur2.hide()
        self.coeur3.hide()
        self.inventory.hide()
        self.fond.hide()
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
        self.gridLayoutWidget.hide()
        self.verticalLayoutWidget.hide()
        self.widget.hide()
        self.inventairemarron.hide()
        self.fontgris.hide()
        self.widget_1.hide()
        self.widget_2.hide()
        self.widget_3.hide()
        self.widget_4.hide()
        self.widget_5.hide()
        self.widget_6.hide()
        self.comboBox.hide()
        self.verticalLayoutWidget_inv.hide()
        self.pushButton_inv.hide()
        
        
    
    def load_screen_title(self):
   
        self.cache_em_all()
        
        self.pushButton_inv.clicked.connect(self.load_screen_title)
        
        self.fond.show()
        self.gros_sacha.show()
        self.pokemon_sauvage.show()
        self.label.show()
        self.inventory2.show()
        self.play.show()
        
    
        self.sacha.setFocus()
    
    def load_map(self):

        self.cache_em_all()
        
        self.pushButton_inv.clicked.connect(self.load_map)
        
        self.fond.show()
        self.coeur1.show()
        self.coeur2.show()
        self.coeur3.show()
        self.inventory.show()
        self.sacha.show()
    
        self.sacha.setFocus()
        
    
    def load_fight(self):
      
        self.cache_em_all()
        
        self.pushButton_inv.clicked.connect(self.load_fight)
        
        self.fondcombat.show()
        self.vs.show()
        self.nompoke.show()
        self.nompokesauvage.show()
        self.progressBarpokesauvage.show()
        self.progressBar_notre.show()
        self.imagepokesauvage.show()
        self.impagepoke.show()
        self.verticalLayoutWidget.show()
        
    def load_inventary_combobox(self):
        self.cache_em_all()
        self.pushButton_3.show()
        self.inventairemarron.show()
        self.fontgris.show()
        self.widget_1.show()
        self.widget_2.show()
        self.widget_3.show()
        self.widget_4.show()
        self.widget_5.show()
        self.widget_6.show()
        self.comboBox.show()
        self.pushButton_inv.show()
        
    def load_inventary(self):
       
        self.cache_em_all()
        self.pushButton_3.hide()
        self.inventairemarron.show()
        self.fontgris.show()
        self.widget_1.show()
        self.widget_2.show()
        self.widget_3.show()
        self.widget_4.show()
        self.widget_5.show()
        self.widget_6.show()

        self.pushButton_inv.show()
        
    def inventaire(self):
         self.bp1.clicked.connect(self.load_map)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.set_dxdy(0)
        
        if event.key() == Qt.Key_Down:
            self.set_dxdy(1)
        
        if event.key() == Qt.Key_Left:
            self.set_dxdy(2)
        
        if event.key() == Qt.Key_Right:
            self.set_dxdy(3)
            
        if event.key() == Qt.Key_Return   :
            self.chek_maison()
            return
        
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
                if ((self.sacha_dy <= (self.sachaY - pos) <= 0) and
                    (start <= self.sachaX <= stop)):
                    self.sachaY = pos
                    break
        
        if self.sacha_dy > 0:
            for limit in self.down_limit:
                pos, start, stop = limit
                if ((self.sacha_dy >= (self.sachaY - pos) >= 0) and
                    (start <= self.sachaX <= stop)):
                    self.sachaY = pos
                    break
        
        if self.sacha_dx < 0:
            for limit in self.left_limit:
                pos, start, stop = limit
                if ((self.sacha_dx <= (self.sachaX - pos) <= 0) and
                    (start <= self.sachaY <= stop)):
                    self.sachaX = pos
                    break
        if self.sacha_dx > 0:
            for limit in self.right_limit:
                pos, start, stop = limit
                if ((self.sacha_dx >= (self.sachaX - pos) >= 0) and
                    (start <= self.sachaY <= stop)):
                    self.sachaX = pos
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
        for pokemon in self.wild:
            dx = pokemon[1] - self.sachaX
            dy = pokemon[2] - self.sachaY
            if (-35 < dx < 35) and (-36 < dy < 29):
                self.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon[0].id_pok - 1) + ".png"))
                self.pokemon_sauvage.setGeometry(QtCore.QRect(pokemon[1], pokemon[2], 25, 26))
                self.pokemon_sauvage.show()
    
    
    def check_fight(self):
        for pokemon in self.wild:
            dx = pokemon[1] - self.sachaX
            dy = pokemon[2] - self.sachaY
            if (-25 < dx < 25) and (-26 < dy < 19):
                dead = fight(self,pokemon[0])
                if dead:
                    self.wild.remove(pokemon)
                self.load_map()
    
    
    def update_position(self):
        self.sachaX += self.sacha_dx
        self.sachaY += self.sacha_dy
        self.check_position()
        self.check_pokemon()
        self.check_fight()
        
        
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
        
        
    def chek_maison(self):
        dx= 390 -self.sachaX
        dy = 520- self.sachaY
        if (-20 < dx < 20) and (-26 < dy < 19):
            self.load_inventary_combobox()

        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow(wild, starting_pack, atk_lib)
    window.show()
    window.sacha.setFocus()
    sys.exit(app.exec_())