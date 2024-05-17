# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:00:24 2024

@author: 33695
"""

#imports généraux
from time import time
import sys
#imports de nos fichiers
from gui import Ui_MainWindow
from pokemon import Team
from initialisation import wild, starting_pack, atk_lib, zones
from moving import update_position, check_house
from inventory import set_up_inventory
import fight
#imports de PyQt5
from PyQt5 import QtTest, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt


class GameWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, wild, starting_pack, atk_lib, zones, parent=None):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.load_map)
        self.new_game.clicked.connect(self.run_new_game_button)
        self.retour.clicked.connect(self.return_button)
        self.inventory.clicked.connect(self.inventory_clicked)
        self.inventory2.clicked.connect(self.inventory_clicked)
        self.save_button.clicked.connect(self.save)
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
        self.attack_connected = False
        
        self.buttonBox.button(self.buttonBox.Yes).clicked.connect(self.run_yes)
        self.buttonBox.button(self.buttonBox.No).clicked.connect(self.run_no)
        
        self.enemy_with_position = None
        
        
        
        self.speed = 10
        self.time = time()
        self.name = "down0"
        self.dir = 0
        self.moves = 0
        
        
        self.wild = wild
        self.team = Team(starting_pack)
        self.atk_lib = atk_lib
        self.zones = zones
        
        self.check_save()
        
        
        self.run_select_main_button()
        self.load_screen_title()
        
        for individu in starting_pack:
           self.comboBox.addItem(QtGui.QIcon("../data/images/pokemon/blanc/" + str(individu.id_pok-1) + ".png"), individu.name + " lvl." + str(individu.level))
        
        self.lives = 3
        
    
        

        
    
    
    def cache_em_all(self):
        """
        Cache tous les widgets

        Returns
        -------
        None.

        """
        self.coeur1.hide()
        self.coeur2.hide()
        self.coeur3.hide()
        self.gameover.hide()
        self.inventory.hide()
        self.save_button.hide()
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
        self.new_game.hide()
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
        """
        Load l'écran titre

        Returns
        -------
        None.

        """
        self.cache_em_all()
        self.phase = "screen title"
        
        self.fond.show()
        self.gros_sacha.show()
        self.pokemon_sauvage.show()
        self.label.show()
        self.inventory2.show()
        self.new_game.show()
        if self.save_found:
            self.play.show()
    
        self.sacha.setFocus()
    
    def load_map(self):
        """
        Load la map

        Returns
        -------
        None.

        """
        self.cache_em_all()
        self.phase = "map"
        
        self.fond.show()
        self.coeur1.show()
        self.coeur2.show()
        self.coeur3.show()
        self.inventory.show()
        self.save_button.show()
        self.sacha.show()
        
        if check_house(self):
            self.maison.show()
    
        self.sacha.setFocus()
        
    
    def load_fight(self):
        """
        Load le combat

        Returns
        -------
        None.

        """
        self.cache_em_all()
        self.phase = "fight"
        
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
    
        
    def load_inventory_combobox(self):
        """
        Branche les boutons pour l'inventaire depuis la maison

        Returns
        -------
        None.

        """
        self.load_inventory()
        for index_team in self.team.bag:
            pokemon = self.team.list[index_team]
            self.comboBox.setItemText(index_team + 1, pokemon.name + " lvl." + str(pokemon.level))
            self.comboBox.setItemIcon(index_team + 1, QtGui.QIcon("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        self.comboBox.show()
        self.select_main_button.show()
        self.see_the_attacks.show()
        self.select_remove_button.show()
        self.retour.show()
        
    def load_inventory(self):
        """
        Load l'inventaire

        Returns
        -------
        None.

        """
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
        
        #Cache tous les boutons
        self.send_to_fight.hide()
        self.select_main_button.hide()
        self.see_the_attacks.hide()
        self.select_remove_button.hide()
     
    def inventory_clicked(self):
        """
        Load l'inventaire depuis la map ou l'écran titre

        Returns
        -------
        None.

        """
        self.load_inventory()
        self.select_main_button.show()
        self.see_the_attacks.show()
        self.retour.show()
    
    def return_button(self):
        """
        Re-load la dernière interface

        Returns
        -------
        None.

        """
        if self.phase == "screen title":
            self.load_screen_title()
        elif self.phase == "map":
            self.load_map()
        else:
            self.load_fight()
    
    def choose_attack_button(self):
        """
        Affiche les attaques disponibles

        Returns
        -------
        None.

        """
        fight.choose_attack(self)
        window.phase = "attack"
    
    #Résoud le tour avec l'attaque choisie
    def attack_1_button(self):
        fight.attack1_selected(self)
    def attack_2_button(self):
        fight.attack2_selected(self)
    def attack_3_button(self):
        fight.attack3_selected(self)
    def attack_4_button(self):
        fight.attack4_selected(self)
    
    def change_pokemon_button(self):
        """
        Load l'inventaire pour choisir un pokemon à envoyer au combat

        Returns
        -------
        None.

        """
        window.phase = "change pokemon"
        fight.change_pokemon(self)
    
    def escape_button(self):
        """
        Affiche une boîte de dialogue pour demander au joueur s'il veut fuir'

        Returns
        -------
        None.

        """
        window.areyousure.setText("Are you sure\nyou want to escape ?")
        window.widget.show()
        window.gridLayoutWidget.hide()
    
    def run_send_to_fight_button(self):
        """
        Envoie le pokemon sélectioné au combat si celui-ci a au moins 1 hp
        Ne fait rien sinon

        Returns
        -------
        None.

        """
        if self.team.list[self.team.bag[self.case - 1]].hp == 0:
            self.verticalLayoutWidget_inv.hide()
        else:
            if self.phase == "change pokemon":
                fight.run_pokemon_changement(self)
            elif self.phase == "pokemon ko":
                fight.upload_pokemon(self, self.case - 1)
                self.load_fight()
    
    
    
    def show_vertical_layout(self):
        """
        Affiche les options disponibles dans l'inventire

        Returns
        -------
        None.

        """
        self.verticalLayoutWidget_inv.show()
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
        """
        Applique le retrait du pokemon sélectioné

        Returns
        -------
        None.

        """
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
    
    def run_select_main_button(self):
        """
        Rend le pokemon sélectioné comme étant le main pokemon
        Si le pokemon sélectioné a 0 hp, la fonction ne fait rien

        Returns
        -------
        None.

        """
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
        """
        Affiche les attaques du pokemon sélectioné

        Returns
        -------
        None.

        """
        fight.run_see_the_attacks(self)
    
    def run_yes(self):
        """
        Résout le bouton yes

        Returns
        -------
        None.

        """
        fight.yes_button(self)
    
    def run_no(self):
        """
        Résout le bouton no

        Returns
        -------
        None.

        """
        fight.no_button(self)
    
    def add_to_bag(self,index_combo):
        """
        Ajoute un pokemon de l'équipe dans le sac

        Parameters
        ----------
        index_combo : int
            indice du pokemon à mettre dans le sac

        Returns
        -------
        None.

        """
        index_team = index_combo - 1
        if index_team != -1 and (not index_team in self.team.bag):
            self.team.put_in(index_team)
        self.load_inventory_combobox()
    
    def update_escape(self):
        """
        Update la position après avoir fuit

        Returns
        -------
        None.

        """
        update_position(self)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up or event.key() == Qt.Key_Z:
            self.dir = 1
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            self.dir = 2
        elif event.key() == Qt.Key_Left or event.key() == Qt.Key_Q:
            self.dir = 3
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            self.dir = 4
        elif event.key() == Qt.Key_Return:
            if check_house(self):
                for index_team in self.team.bag:
                    self.team.list[index_team].heal()
                self.load_inventory_combobox()
            self.dir = 0
            self.moves = 0
        
        # =============================================================================
        #Interface pour implémenter les zones
        # =============================================================================
        
        # elif event.key() == Qt.Key_P:
        #     self.speed = 24
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_M:
        #     self.speed = 1
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_E:
        #     self.coinx = self.sacha.x() - self.fond.x()
        #     self.coiny = self.sacha.y() - self.fond.y()
        #     print(self.coinx, self.coiny)
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_F:
        #     x2 = self.sacha.x() + self.sacha.width()  - 1 - self.fond.x() - self.coinx
        #     y2 = self.sacha.y() + self.sacha.height() - 1 - self.fond.y() - self.coiny
            
        #     zonage = r"zones.txt"
        #     with open(zonage, "a") as f:
        #         f.write(f"infos = [{self.coinx},{self.coiny},{x2},{y2}]\n")
        #         f.write(f"zones.append(Sous_Zone(info{self.num_zone} + infos))\n")
        #     print(f"infos = [{self.coinx},{self.coiny},{x2},{y2}]")
        #     print(f"zones.append(Sous_Zone(info{self.num_zone} + infos))")
        #     print("")
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_C:
        #     zonage = r"zones.txt"
        #     with open(zonage, "a") as f:
        #         f.write("\n")
            
        #     try:
        #         self.num_zone += 1
        #     except:
        #         self.num_zone = 0
        #     print(f"Vous êtes dans la zone {self.num_zone}")
        #     self.dir = 0
        #     self.moves = 0
        
        
        # =============================================================================
        #Interface pour implementer les collisions    
        # =============================================================================
        
        # elif event.key() == Qt.Key_U:
        #     print("Direction des barrières : up")
        #     self.file = 1
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_D:
        #     print("Direction des barrières : down")
        #     self.file = 2
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_L:
        #     print("Direction des barrières : left")
        #     self.file = 3
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_R:
        #     print("Direction des barrières : right")
        #     self.file = 4
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_W:
        #     self.startx = self.sacha.x() - self.fond.x()
        #     self.starty = self.sacha.y() - self.fond.y()
        #     self.dir = 0
        #     self.moves = 0
        # elif event.key() == Qt.Key_X:
        #     stopx = self.sacha.x() + self.sacha.width()  - 1 - self.fond.x()
        #     stopy = self.sacha.y() + self.sacha.height() - 1 - self.fond.y()
        #     if self.file == 1:
        #         limit = r"bounds/up.txt"
        #         with open(limit, "a") as f:
        #             f.write(f"{self.starty - 1},{self.startx},{stopx}\n")
        #     elif self.file == 2:
        #         limit = r"bounds/down.txt"
        #         with open(limit, "a") as f:
        #             f.write(f"{self.starty + self.sacha.height()},{self.startx},{stopx}\n")
        #     elif self.file == 3:
        #         limit = r"bounds/left.txt"
        #         with open(limit, "a") as f:
        #             f.write(f"{self.startx - 1},{self.starty},{stopy}\n")
        #     elif self.file == 4:
        #         limit = r"bounds/right.txt"
        #         with open(limit, "a") as f:
        #             f.write(f"{self.startx + self.sacha.width()},{self.starty},{stopy}\n")
            
        #     self.dir = 0
        #     self.moves = 0
        elif event.key() == Qt.Key_I:
            if self.phase == "map" or self.phase == "screen title":
                self.inventory_clicked()
            self.dir = 0
            self.moves = 0
        else:
            return
        if self.phase == "map" and self.dir:
            update_position(self)

    #Fonction liées à la sauvegarde    

    def save(self):
        save = r'save.py'
        with open(save, 'w') as f:
            text = 'from pokemon import Attack,Individu,Team\n'
            text += 'from pokemon import liste_pokemon\n\n'
            text += str(self.team) + '\n'
            text += 'saved_wild = []\n'
            for pokemon in self.wild:
                text += str(pokemon[0]) + '\n'
                text += 'saved_wild.append([pokemon] + ' + str(pokemon[1:]) + ')\n'
            text += 'saved_sacha_x = ' + str(self.sacha.x()) + '\n'
            text += 'saved_sacha_y = ' + str(self.sacha.y()) + '\n'
            text += 'saved_fond_x = ' + str(self.fond.x()) + '\n'
            text += 'saved_fond_y = ' + str(self.fond.y()) + '\n'
            
            f.write(text)
        
        text = 'Game saved'
        self.infos_combat.setText("")
        self.infos_combat.show()
        QtTest.QTest.qWait(150)
        fight.display_in_label(self, text)
        QtTest.QTest.qWait(500)
        self.infos_combat.hide()
        self.sacha.setFocus()
        
    
    def check_save(self):
        try:
            import save
            self.wild = save.saved_wild
            self.team = save.saved_team
            self.sacha.move(save.saved_sacha_x, save.saved_sacha_y)
            self.fond.move(save.saved_fond_x, save.saved_fond_y)
            update_position(self)
            self.save_found = True
        except:
            self.save_found = False
    
    def run_new_game_button(self):
        self.wild = wild
        self.team = Team(starting_pack)
        self.sacha.move(540, 364)
        self.fond.move(-180,-860)
        self.load_map()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow(wild, starting_pack, atk_lib, zones)
    window.show()
    window.sacha.setFocus()
    sys.exit(app.exec_())