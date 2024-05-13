# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:00:24 2024

@author: 33695
"""

import numpy  as np
import random as rd
from time import time
import sys
from gui import Ui_MainWindow
from pokemon3 import *
from initialisation import *
import moving
from fight_engine import *
from inventory import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt


class GameWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, wild, starting_pack, atk_lib, zones, parent=None):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.load_map)
        self.inventory2.clicked.connect(self.load_inventory)
        self.retour.clicked.connect(self.load_screen_title)
        self.inventory.clicked.connect(self.inventory_clicked)
        self.inventory2.clicked.connect(self.inventory_clicked)
        #self.bp1.clicked.connect(self.select_main_button)
        self.bp1.clicked.connect(self.show_vertical_layout)
        self.bp2.clicked.connect(self.show_vertical_layout)
        self.bp3.clicked.connect(self.show_vertical_layout)
        self.bp4.clicked.connect(self.show_vertical_layout)
        self.bp5.clicked.connect(self.show_vertical_layout)
        self.bp6.clicked.connect(self.show_vertical_layout)
        
        self.chooseattack.clicked.connect(self.choose_attack_button)
        
        self.changepokemon.clicked.connect(self.change_pokemon_button)
        
        self.escape.clicked.connect(self.escape_button)
        
        
        self.case = 1
        self.send_to_fight.clicked.connect(self.run_send_to_fight_button)
        self.select_main_button.clicked.connect(self.run_select_main_button)
        self.see_the_attacks.clicked.connect(self.run_see_the_attacks_button)
        self.select_remove_button.clicked.connect(self.run_select_remove_button)
        
        self.enemy_with_position = None
        
        
        
        self.sachaX = 390
        self.sachaY = 580
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_dir = 1
        self.sacha_moves = [0,0,0,0]
        self.name = "down0"
        
        self.speed = 4
        self.time = time()
        self.name = "down0"
        self.moves = 0
        
        self.up_limit    = np.genfromtxt("bounds/up.txt"   , dtype = int, delimiter = ',')
        self.down_limit  = np.genfromtxt("bounds/down.txt" , dtype = int, delimiter = ',')
        self.left_limit  = np.genfromtxt("bounds/left.txt" , dtype = int, delimiter = ',')
        self.right_limit = np.genfromtxt("bounds/right.txt", dtype = int, delimiter = ',')
        
        self.wild = wild
        self.team = Team(starting_pack)
        self.atk_lib = atk_lib
        self.zones = zones
        
        set_up_inventory(self)
        self.load_screen_title()
        
        for individu in starting_pack:
           self.comboBox.addItem(QtGui.QIcon("images/pokemon/blanc/" + str(individu.id_pok-1) + ".png"), individu.name + " lvl." + str(individu.level))
        
    def show_vertical_layout(self):
        
        #self.verticalLayout.show()
        self.verticalLayoutWidget_inv.setVisible(True)
        self.gridLayoutWidget.hide()
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
            
    def run_select_remove_button(self):
        if self.case==1:
            self.widget_1.hide()
            
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
        
        self.team.put_out(self.team.bag[self.case - 1])
        
        self.verticalLayoutWidget_inv.hide()
            
            
            
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
        self.maison.hide()
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
        self.retour.hide()
        
        
    
    
    
    def load_screen_title(self):
   
        self.cache_em_all()
        
        self.retour.clicked.connect(self.load_screen_title)
        
        self.fond.show()
        self.gros_sacha.show()
        self.pokemon_sauvage.show()
        self.label.show()
        self.inventory2.show()
        self.play.show()
        
    
        self.sacha.setFocus()
    
    def load_map(self):

        self.cache_em_all()
        
        self.retour.clicked.connect(self.load_map)
        
        self.fond.show()
        self.coeur1.show()
        self.coeur2.show()
        self.coeur3.show()
        self.inventory.show()
        self.sacha.show()
        if moving.check_house(self):
            self.maison.show()
    
        self.sacha.setFocus()
        
    
    def load_fight(self):
      
        self.cache_em_all()
        
        self.retour.clicked.connect(self.load_fight)
        
        self.fondcombat.show()
        self.vs.show()
        self.nompoke.show()
        self.nompokesauvage.show()
        self.progressBarpokesauvage.show()
        self.progressBar_notre.show()
        self.imagepokesauvage.show()
        self.impagepoke.show()
        self.verticalLayoutWidget.show()
        
    def load_inventory_combobox(self):
        self.load_inventory()
        self.comboBox.show()
        self.select_main_button.show()
        self.couronne1.show()
        self.couronne2.hide()
        self.couronne3.hide()
        self.couronne4.hide()
        self.couronne5.hide()
        self.couronne6.hide()
        self.see_the_attacks.show()
        self.select_remove_button.show()
        
    def load_inventory(self):
       
        self.cache_em_all()
        self.select_remove_button.hide()
        self.comboBox.show()
        self.inventairemarron.show()
        self.fontgris.show()
        set_up_inventory(self)
        self.couronne1.show()
        self.couronne2.hide()
        self.couronne3.hide()
        self.couronne4.hide()
        self.couronne5.hide()
        self.couronne6.hide()
        self.retour.show()
        
        self.send_to_fight.hide()
        self.select_main_button.hide()
        self.see_the_attacks.hide()
        self.select_remove_button.hide()
    
    def main_pokemon(self):
        pass
        
    def inventory_clicked(self):
        self.load_inventory()
        self.select_main_button.show()
        self.see_the_attacks.show()

    def set_main_1(self):
        self.team.main = self.team.bag[0]
    def set_main_2(self):
        self.team.main = self.team.bag[1]
    def set_main_3(self):
        self.team.main = self.team.bag[2]
    def set_main_4(self):
        self.team.main = self.team.bag[3]
    def set_main_5(self):
        self.team.main = self.team.bag[4]
    def set_main_6(self):
        self.team.main = self.team.bag[5]
    
    def choose_attack_button(self):
        choose_attack(self)
        window.phase = "attack"
    def attack_1_button(self):
        attack1_selected(self)
    def attack_2_button(self):
        attack2_selected(self)
    def attack_3_button(self):
        attack3_selected(self)
    def attack_4_button(self):
        attack4_selected(self)
    
    def change_pokemon_button(self):
        change_pokemon(self)
        window.phase = "change pokemon"
    
    def run_send_to_fight_button(self):
        if self.phase == "change pokemon":
            run_pokemon_changement(self)
        elif self.phase == "pokemon ko":
            upload_pokemon(self, self.case - 1)
            self.load_fight()
    
    def escape_button(self):
        run_escape(self)
    
    def run_select_main_button(self):
        self.team.set_main(self.team.bag[self.case - 1])
        self.verticalLayoutWidget_inv.hide()
        self.couronne1.hide()
        self.couronne2.hide()
        self.couronne3.hide()
        self.couronne4.hide()
        self.couronne5.hide()
        self.couronne6.hide()
        if self.case ==1:
            self.couronne1.show()
        if self.case == 2:
            self.couronne2.show()
        if self.case == 3:
            self.couronne3.show()
        if self.case == 4:
            self.couronne4.show()
        if self.case == 5:
            self.couronne5.show()
        if self.case == 6:
            self.couronne6.show()
        
        
    
    def run_see_the_attacks_button(self):
        self.attaque1.hide()
        self.attaque2.hide()
        self.attaque3.hide()
        self.attaque4.hide()
        
        attacks = self.team.list[self.team.bag[self.case - 1]].list_atk
        n = len(attacks)
        if n > 0:
            self.attaque1.setText(attacks[0].name)
            self.attaque1.show()
            if n > 1:
                self.attaque2.setText(attacks[1].name)
                self.attaque2.show()
                if n > 2:
                    self.attaque3.setText(attacks[2].name)
                    self.attaque3.show()
                    if n > 3:
                        self.attaque4.setText(attacks[3].name)
                        self.attaque4.show()
        
        self.gridLayoutWidget.show()
        self.verticalLayoutWidget_inv.hide()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.dir = 1
        elif event.key() == Qt.Key_Down:
            self.dir = 2
        elif event.key() == Qt.Key_Left:
            self.dir = 3
        elif event.key() == Qt.Key_Right:
            self.dir = 4
        elif event.key() == Qt.Key_Return:
            if moving.check_house(self):
                for index_team in self.team.bag:
                    self.team.list[index_team].heal()
                self.load_inventory_combobox()
            self.dir = 0
            self.moves = 0
        else:
            return
        moving.update_position(self)
    
    def keyReleaseEvent(self, event):
        
        if event.key() == Qt.Key_Up:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Down:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Left:
            self.sacha_dx = 0
        
        if event.key() == Qt.Key_Right:
            self.sacha_dx = 0
        
    
    # def set_dxdy(self,direction):
    #     self.sacha_dir = direction
    #     dx = {0:self.sacha_dx, 1:self.sacha_dx, 2:-4, 3:4}[direction]
    #     dy = {0:-4, 1:4, 2:self.sacha_dy, 3:self.sacha_dy}[direction]
        
    #     if dx != 0 and dy != 0:
    #         self.sacha_dx = round(dx * 3/4)
    #         self.sacha_dy = round(dy * 3/4)
    #     else:
    #         self.sacha_dx = dx
    #         self.sacha_dy = dy
        
    
    # def check_position(self):
    #     if self.sacha_dy < 0:
    #         for limit in self.up_limit:
    #             pos, start, stop = limit
    #             if ((self.sacha_dy <= (self.sachaY - pos) <= 0) and
    #                 (start <= self.sachaX <= stop)):
    #                 self.sachaY = pos
    #                 break
        
    #     if self.sacha_dy > 0:
    #         for limit in self.down_limit:
    #             pos, start, stop = limit
    #             if ((self.sacha_dy >= (self.sachaY - pos) >= 0) and
    #                 (start <= self.sachaX <= stop)):
    #                 self.sachaY = pos
    #                 break
        
    #     if self.sacha_dx < 0:
    #         for limit in self.left_limit:
    #             pos, start, stop = limit
    #             if ((self.sacha_dx <= (self.sachaX - pos) <= 0) and
    #                 (start <= self.sachaY <= stop)):
    #                 self.sachaX = pos
    #                 break
    #     if self.sacha_dx > 0:
    #         for limit in self.right_limit:
    #             pos, start, stop = limit
    #             if ((self.sacha_dx >= (self.sachaX - pos) >= 0) and
    #                 (start <= self.sachaY <= stop)):
    #                 self.sachaX = pos
    #                 break
        
    #     # if self.sachaX < 0:
    #     #     self.sachaX = 0
    #     # if self.sachaX > 1071:
    #     #     self.sachaX = 1071
    #     # if self.sachaY < 0:
    #     #     self.sachaY = 0
    #     # if self.sachaY > 696:
    #     #     self.sachaY = 696
    
    # def check_pokemon(self):
    #     for pokemon in self.wild:
    #         dx = pokemon[1] - self.sachaX
    #         dy = pokemon[2] - self.sachaY
    #         if (-35 < dx < 35) and (-36 < dy < 29):
    #             self.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon[0].id_pok - 1) + ".png"))
    #             self.pokemon_sauvage.setGeometry(QtCore.QRect(pokemon[1], pokemon[2], 25, 26))
    #             self.pokemon_sauvage.show()
    
    
    # def check_fight(self):
    #     for pokemon in self.wild:
    #         dx = pokemon[1] - self.sachaX
    #         dy = pokemon[2] - self.sachaY
    #         if (-25 < dx < 25) and (-26 < dy < 19):
    #             self.enemy = pokemon[0]
    #             self.enemy_with_position = pokemon
    #             self.notre_pokemon = self.team.list[self.team.main]
    #             set_up_fight(self)
    
    
    # def update_position(self):
    #     self.sachaX += self.sacha_dx
    #     self.sachaY += self.sacha_dy
    #     self.check_position()
    #     self.check_pokemon()
    #     self.check_fight()
    #     self.check_zone()
    #     if self.check_maison():
    #         self.maison.show()
    #     else:
    #         self.maison.hide()
        
        
    #     name = {0:"up", 1:"down", 2:"left", 3:"right"}[self.sacha_dir]
    #     order = self.sacha_moves[self.sacha_dir]
    #     if (order % 6) == 4:
    #         self.name = name + "0"
    #     elif (order % 12) == 1:
    #         self.name = name + "1"
    #     elif (order % 12) == 7:
    #         self.name = name + "2"
        
    #     self.sacha_moves[self.sacha_dir] += 1
        
    #     self.sacha.setPixmap(QtGui.QPixmap("images/animation/" + self.name + ".png"))
    #     self.sacha.setGeometry(QtCore.QRect(self.sachaX, self.sachaY, 19, 25))
        
        
    # def check_maison(self):
    #     dx= 390 -self.sachaX
    #     dy = 520- self.sachaY
    #     if (-20 < dx < 20) and (-26 < dy < 19):
    #         return True
    #     return False
    
    # def check_zone(self):
    #     for zone in self.zones:
    #         if self.sacha in zone:
    #             if rd.random() < zone.p:
    #                 enemy = Individu(liste_pokemon[zone.id_pok()],[self.atk_lib[0]])
    #                 self.enemy = enemy
    #                 self.notre_pokemon = self.team.list[self.team.main]
    #                 set_up_fight(self)
    #             break

        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow(wild, starting_pack, atk_lib, zones)
    window.show()
    window.sacha.setFocus()
    sys.exit(app.exec_())