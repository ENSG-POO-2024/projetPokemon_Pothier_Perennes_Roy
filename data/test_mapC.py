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
        self.retour.clicked.connect(self.return_button)
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
        
        self.comboBox.currentIndexChanged.connect(self.add_to_bag)
        
        
        self.case = 1
        self.send_to_fight.clicked.connect(self.run_send_to_fight_button)
        self.select_main_button.clicked.connect(self.run_select_main_button)
        self.see_the_attacks.clicked.connect(self.run_see_the_attacks_button)
        self.select_remove_button.clicked.connect(self.run_select_remove_button)
        
        self.buttonBox.button(self.buttonBox.Yes).clicked.connect(self.run_yes)
        self.buttonBox.button(self.buttonBox.No).clicked.connect(self.run_no)
        
        self.enemy_with_position = None
        
        
        
        self.sachaX = 535
        self.sachaY = 358
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_dir = 1
        self.sacha_moves = [0,0,0,0]
        self.name = "down0"
        
        self.speed = 12
        self.time = time()
        self.name = "down0"
        self.moves = 0
        
        # self.up_limit    = np.genfromtxt("bounds/up.txt"   , dtype = int, delimiter = ',')
        # self.down_limit  = np.genfromtxt("bounds/down.txt" , dtype = int, delimiter = ',')
        # self.left_limit  = np.genfromtxt("bounds/left.txt" , dtype = int, delimiter = ',')
        # self.right_limit = np.genfromtxt("bounds/right.txt", dtype = int, delimiter = ',')
        
        self.wild = wild
        self.team = Team(starting_pack)
        self.atk_lib = atk_lib
        self.zones = zones
        
        self.run_select_main_button()
        # set_up_inventory(self)
        self.load_screen_title()
        
        for individu in starting_pack:
           self.comboBox.addItem(QtGui.QIcon("images/pokemon/blanc/" + str(individu.id_pok-1) + ".png"), individu.name + " lvl." + str(individu.level))
        
        self.lives = 3
        
    def show_vertical_layout(self):
        self.verticalLayoutWidget_inv.show()
        # self.verticalLayoutWidget_inv.setVisible(True)
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
        if self.team.len < 2:
            self.verticalLayoutWidget_inv.hide()
            return
        
        if self.case==1:
            self.widget_1.hide()
            
        if self.case==2:
            self.widget_2.hide()
            
        if self.case==3:
            self.widget_3.hide()
            
        if self.case==4:
            self.widget_4.hide()
            
        if self.case==5:
            self.widget_5.hide()
            
        if self.case==6:
            self.widget_6.hide()
        
        if self.team.main == self.team.bag[self.case - 1]:
            self.team.set_main(self.team.bag[0])
        self.team.put_out(self.team.bag[self.case - 1])
        
        self.verticalLayoutWidget_inv.hide()
        self.load_inventory_combobox()
            
            
            
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
        self.level_notre_poke.hide()
        self.level_poke_sauvage.hide()
        self.gridLayoutWidget.hide()
        self.verticalLayoutWidget.hide()
        self.widget.hide()
        self.infos_combat.hide()
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
        self.phase = "screen title"
        
        #self.retour.clicked.connect(self.load_screen_title)
        
        self.fond.show()
        self.gros_sacha.show()
        self.pokemon_sauvage.show()
        self.label.show()
        self.inventory2.show()
        self.play.show()
        
    
        self.sacha.setFocus()
    
    def load_map(self):
        self.cache_em_all()
        self.phase = "map"
        
        #self.retour.clicked.connect(self.load_map)
        
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
        self.phase = "fight"
        
        #self.retour.clicked.connect(self.load_fight)
        
        self.fondcombat.show()
        self.vs.show()
        self.nompoke.show()
        self.nompokesauvage.show()
        self.progressBarpokesauvage.show()
        self.progressBar_notre.show()
        self.imagepokesauvage.show()
        self.impagepoke.show()
        self.level_notre_poke.show()
        self.level_poke_sauvage.show()
        self.verticalLayoutWidget.show()
    
    def return_button(self):
        if self.phase == "screen title":
            self.load_screen_title()
        elif self.phase == "map":
            self.load_map()
        else:
            self.load_fight()
        
    def load_inventory_combobox(self):
        self.load_inventory()
        for index_team in self.team.bag:
            pokemon = self.team.list[index_team]
            self.comboBox.setItemText(index_team + 1, pokemon.name + " lvl." + str(pokemon.level))
        self.comboBox.show()
        self.select_main_button.show()
        self.see_the_attacks.show()
        self.select_remove_button.show()
        self.retour.show()
        
    def load_inventory(self):
        
        self.cache_em_all()
        self.couronne1.hide()
        self.couronne2.hide()
        self.couronne3.hide()
        self.couronne4.hide()
        self.couronne5.hide()
        self.couronne6.hide()
        self.inventairemarron.show()
        self.fontgris.show()
        set_up_inventory(self)
        
        self.send_to_fight.hide()
        self.select_main_button.hide()
        self.see_the_attacks.hide()
        self.select_remove_button.hide()
     
    def inventory_clicked(self):
        self.load_inventory()
        self.select_main_button.show()
        self.see_the_attacks.show()
        self.retour.show()

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
        window.phase = "change pokemon"
        change_pokemon(self)
    
    def run_send_to_fight_button(self):
        if self.team.list[self.team.bag[self.case - 1]].hp == 0:
            self.verticalLayoutWidget_inv.hide()
        else:
            if self.phase == "change pokemon":
                run_pokemon_changement(self)
            elif self.phase == "pokemon ko":
                upload_pokemon(self, self.case - 1)
                self.load_fight()
    
    def escape_button(self):
        window.areyousure.setText("Are you sure\nyou want to escape ?")
        window.widget.show()
    
    def run_select_main_button(self):
        if self.team.list[self.team.bag[self.case - 1]].hp <= 0:
            self.verticalLayoutWidget_inv.hide()
            return
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
        
        colors = {0:"#60A2B9",1:"#FF8100",2:"#4F60E2",3:"#2481EF",4:"#FAC100",5:"#E72324",6:"#EF70EF", 
                       7:"#3DD9FF",8:"#92A212",9:"#A0A2A0",10:"#3DA224",11:"#923FCC",12:"#EF3F7A",
                       13:"#B0AA82",14:"#92501B",15:"#703F70",16:"#4F3F3D",17:"#82BAEF"}
        
        if window.phase != "fight":
            pokemon = self.team.list[self.team.bag[self.case - 1]]
        else:
            pokemon = self.notre_pokemon
        
        attacks = pokemon.list_atk
        n = len(attacks)
        if n > 0:
            self.attaque1.setText(attacks[0].name)
            self.attaque1.setStyleSheet("QPushButton {background-color: " + colors[attacks[0].type] + "}")
            self.attaque1.show()
            if n > 1:
                self.attaque2.setText(attacks[1].name)
                self.attaque2.setStyleSheet("QPushButton {background-color: " + colors[attacks[1].type] + "}")
                self.attaque2.show()
                if n > 2:
                    self.attaque3.setText(attacks[2].name)
                    self.attaque3.setStyleSheet("QPushButton {background-color: " + colors[attacks[2].type] + "}")
                    self.attaque3.show()
                    if n > 3:
                        self.attaque4.setText(attacks[3].name)
                        self.attaque4.setStyleSheet("QPushButton {background-color: " + colors[attacks[3].type] + "}")
                        self.attaque4.show()
        
        if window.phase != "fight":
            self.gridLayoutWidget.show()
            self.verticalLayoutWidget_inv.hide()
    
    def run_yes(self):
        yes_button(self)
    
    def run_no(self):
        no_button(self)
    
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
        elif event.key() == Qt.Key_P:
            self.speed = 24
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_M:
            self.speed = 1
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_E:
            self.coinx = self.sacha.x() - self.fond.x()
            self.coiny = self.sacha.y() - self.fond.y()
            print(self.coinx, self.coiny)
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_F:
            x2 = self.sacha.x() + self.sacha.width()  - 1 - self.fond.x() - self.coinx
            y2 = self.sacha.y() + self.sacha.height() - 1 - self.fond.y() - self.coiny
            
            zonage = r"zones.txt"
            with open(zonage, "a") as f:
                f.write(f"infos = [{self.coinx},{self.coiny},{x2},{y2}]\n")
                f.write(f"zones.append(Sous_Zone(info{self.num_zone} + infos))\n")
            print(f"infos = [{self.coinx},{self.coiny},{x2},{y2}]")
            print(f"zones.append(Sous_Zone(info{self.num_zone} + infos))")
            print("")
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_C:
            zonage = r"zones.txt"
            with open(zonage, "a") as f:
                f.write("\n")
            
            try:
                self.num_zone += 1
            except:
                self.num_zone = 0
            print(f"Vous êtes dans la zone {self.num_zone}")
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_U:
            print("Direction des barrières : up")
            self.file = 1
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_D:
            print("Direction des barrières : down")
            self.file = 2
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_L:
            print("Direction des barrières : left")
            self.file = 3
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_R:
            print("Direction des barrières : right")
            self.file = 4
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_W:
            self.startx = self.sacha.x() - self.fond.x()
            self.starty = self.sacha.y() - self.fond.y()
            self.dir = 0
            self.moves = 0
        elif event.key() == Qt.Key_X:
            stopx = self.sacha.x() + self.sacha.width()  - 1 - self.fond.x()
            stopy = self.sacha.y() + self.sacha.height() - 1 - self.fond.y()
            if self.file == 1:
                limit = r"bounds/up.txt"
                with open(limit, "a") as f:
                    f.write(f"{self.starty - 1},{self.startx},{stopx}\n")
            elif self.file == 2:
                limit = r"bounds/down.txt"
                with open(limit, "a") as f:
                    f.write(f"{self.starty + self.sacha.height()},{self.startx},{stopx}\n")
            elif self.file == 3:
                limit = r"bounds/left.txt"
                with open(limit, "a") as f:
                    f.write(f"{self.startx - 1},{self.starty},{stopy}\n")
            elif self.file == 4:
                limit = r"bounds/right.txt"
                with open(limit, "a") as f:
                    f.write(f"{self.startx + self.sacha.width()},{self.starty},{stopy}\n")
            
            self.dir = 0
            self.moves = 0
        else:
            return
        if self.phase == "map" and self.dir:
            moving.update_position(self)
    
    def add_to_bag(self,index_combo):
        index_team = index_combo - 1
        if index_team != -1 and (not index_team in self.team.bag):
            self.team.put_in(index_team)
        self.load_inventory_combobox()
    
    def update_escape(self):
        moving.update_position(self)
    
    # def keyReleaseEvent(self, event):
        
    #     if event.key() == Qt.Key_Up:
    #         self.sacha_dy = 0
        
    #     if event.key() == Qt.Key_Down:
    #         self.sacha_dy = 0
        
    #     if event.key() == Qt.Key_Left:
    #         self.sacha_dx = 0
        
    #     if event.key() == Qt.Key_Right:
    #         self.sacha_dx = 0
    
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