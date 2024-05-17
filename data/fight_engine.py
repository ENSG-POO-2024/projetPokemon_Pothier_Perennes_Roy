# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:39:43 2024

@author: Ordi
"""
from time import sleep
from time import time
import random as rd
from pokemon3 import Individu
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtTest
import sys


def set_up_fight(window):
    window.fighters = set()
    upload_pokemon(window, window.team.main)
    window.nompokesauvage.setText(window.enemy.name)
    window.progressBarpokesauvage.setMaximum(window.enemy.hp_max)
    window.progressBarpokesauvage.setProperty("value", window.enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"))
    window.imagepokesauvage.setScaledContents(True)
    window.level_poke_sauvage.setText("lvl. " + str(window.enemy.level))
    window.load_fight()

def upload_pokemon(window,index_team):
    pokemon = window.team.list[index_team]
    window.notre_pokemon = pokemon
    window.nompoke.setText(pokemon.name)
    color = color_health(pokemon)
    window.fighters.add(index_team)
    window.phase = "fight"
    
    window.progressBar_notre.setMaximum(pokemon.hp_max)
    window.progressBar_notre.setProperty("value", pokemon.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")
    window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/blanc/miroir/" + str(pokemon.id_pok - 1) + ".png"))
    window.impagepoke.setScaledContents(True)
    window.level_notre_poke.setText("lvl. " + str(pokemon.level))
    window.run_see_the_attacks_button()
    
    # window.attaque1.hide()
    # window.attaque2.hide()
    # window.attaque3.hide()
    # window.attaque4.hide()
    
    # attacks = pokemon.list_atk
    # n = len(attacks)
    # if n > 0:
    #     window.attaque1.setText(attacks[0].name)
    #     window.attaque1.show()
    #     if n > 1:
    #         window.attaque2.setText(attacks[1].name)
    #         window.attaque2.show()
    #         if n > 2:
    #             window.attaque3.setText(attacks[2].name)
    #             window.attaque3.show()
    #             if n > 3:
    #                 window.attaque4.setText(attacks[3].name)
    #                 window.attaque4.show()


def color_health(pokemon):
    colors = {0:"red", 1:"yellow", 2:"green"}
    ratio = pokemon.hp / pokemon.hp_max
    if ratio < 0.2:
        c = 0
    elif ratio < 0.5:
        c = 1
    else:
        c = 2
    
    return colors[c]
    
def update_fight(window):
    notre_poke = window.notre_pokemon
    color = color_health(notre_poke)
    window.progressBar_notre.setProperty("value", notre_poke.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")
    color = color_health(window.enemy)
    window.progressBarpokesauvage.setValue(window.enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")

def culotte(interval):
    t = time()
    while time() - t < interval:
        None

def animation_enemy(window, damage, critical, efficacity, attack):
    window.infos_combat.setText("")
    window.infos_combat.show()
    text = window.notre_pokemon.name
    text += " used "
    text += attack.name
    text += " !"
    display_in_label(window, text)
    QtTest.QTest.qWait(1000)
    
    if critical:
        text = "Critical !"
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
    
    text = {0:"It doesn't affect " + window.enemy.name + "...",0.25:"It's not very effective...",0.5:"It's not very effective...",
            1:False, 2:"It's super effective!", 4:"It's super effective!"}[efficacity]
    if text:
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
    
    for i in range(damage):
        QtTest.QTest.qWait(200)
        window.enemy.hp -= 1
        if window.enemy.hp < 0:
            window.enemy.hp = 0
            break
        update_fight(window)
        category = ["blanc/", "rouge/"][(i)%2]
        window.imagepokesauvage.setGeometry(QtCore.QRect(640 + (i%2) * 4, 320 + (i%2) * 4, 331, 211))
        window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/" + category + str(window.enemy.id_pok - 1) + ".png"))
    window.imagepokesauvage.setGeometry(QtCore.QRect(640, 320, 331, 211))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"))
    
    if window.enemy.hp == 0:
        text = window.enemy.name + " is K.O."
        display_in_label(window, text)
    QtTest.QTest.qWait(1000)
    window.infos_combat.hide()
    
    
    
    pass
    
#     window.imagepokesauvage.setGeometry(QtCore.QRect(643, 323, 331, 211))
#     window.image1 = QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png")
#     window.imagepokesauvage.setGeometry(QtCore.QRect(643, 323, 331, 211))
#     window.image2 = QPixmap("images/pokemon/rouge/" + str(window.enemy.id_pok - 1) + ".png")

#     window.timer = QTimer(window)
#     window.timer.timeout.connect(window.toggle_image)
#     window.interval = 200  # Intervalle de temps entre chaque changement d'image en millisecondes
#     window.duration = 2000  # Durée totale du clignotement en millisecondes
#     window.total_time_elapsed = 0
#     window.is_image1 = True 
    
# def start_blinking(self):
#     self.timer.start(self.interval)

# def toggle_image(self):
#         # Alterner entre les deux images
#     if self.is_image1:
#         self.label.setPixmap(self.image2)
            
#     else:
#         self.label.setPixmap(self.image1)
#     self.is_image1 = not self.is_image1

#         # Vérifiez si la durée totale du clignotement est écoulée
#     self.total_time_elapsed += self.interval
#     if self.total_time_elapsed >= self.duration:
#         self.timer.stop()
    
#     # window.imagepokesauvage.setGeometry(QtCore.QRect(643, 323, 331, 211))
#     # window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/rouge/" + str(window.enemy.id_pok - 1) + ".png"))
#     # sleep(1)
#     # window.imagepokesauvage.setGeometry(QtCore.QRect(640, 320, 331, 211))
#     # window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"))

def animation_notre_pokemon(window, damage, critical, efficacity, attack):
    window.infos_combat.setText("")
    window.infos_combat.show()
    text = window.enemy.name
    text += " used "
    text += attack.name
    text += " !"
    display_in_label(window, text)
    QtTest.QTest.qWait(1000)
    
    if critical:
        text = "Critical !"
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
    
    text = {0:"It doesn't affect " + window.notre_pokemon.name + "...",0.25:"It's not very effective...",0.5:"It's not very effective...",
            1:False, 2:"It's super effective!", 4:"It's super effective!"}[efficacity]
    if text:
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
    
    for i in range(damage):
        interval = 5000 / damage
        QtTest.QTest.qWait(200)
        window.notre_pokemon.hp -= 1
        if window.notre_pokemon.hp < 0:
            window.notre_pokemon.hp = 0
            break
        update_fight(window)
        category = ["blanc/", "rouge/"][(i)%2]
        window.impagepoke.setGeometry(QtCore.QRect(160 + (i%2) * 4, 320 + (i%2) * 4, 331, 211))
        window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/" + category + "miroir/" + str(window.notre_pokemon.id_pok - 1) + ".png"))
    window.impagepoke.setGeometry(QtCore.QRect(160, 320, 331, 211))
    window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/blanc/miroir/" + str(window.notre_pokemon.id_pok - 1) + ".png"))
    
    if window.enemy.hp == 0:
        text = window.notre_pokemon.name + " is K.O."
        display_in_label(window, text)
    QtTest.QTest.qWait(1000)
    window.infos_combat.hide()
    
def display_in_label(window,text):
    for i in range(len(text) + 1):
        window.infos_combat.setText(text[:i])
        QtTest.QTest.qWait(20)

def choose_attack(window):
    window.attaque1.clicked.connect(window.attack_1_button)
    window.attaque2.clicked.connect(window.attack_2_button)
    window.attaque3.clicked.connect(window.attack_3_button)
    window.attaque4.clicked.connect(window.attack_4_button)
    window.gridLayoutWidget.show()

def attack1_selected(window):
    window.case = 1
    run_attack(window, 0)

def attack2_selected(window):
    window.case = 2
    run_attack(window, 1)

def attack3_selected(window):
    window.case = 3
    run_attack(window, 2)

def attack4_selected(window):
    window.case = 4
    run_attack(window, 3)

def first_player(window):
    sp1, sp2 = window.notre_pokemon.speed, window.enemy.speed
    sp1 = int(sp1 * window.notre_pokemon.level / 50) + 5
    sp2 = int(sp2 * window.enemy.level         / 50) + 5
    if sp1 == sp2:
        return rd.randint(0, 1)
    else:
        return sp1 > sp2

def hit_someone(window,first,id_atk = None):
    if first:
        damage, critical, efficacity, attack = Individu.damage_calculator(window.notre_pokemon, window.enemy, window.notre_pokemon.list_atk[id_atk])
        animation_enemy(window,damage,critical,efficacity,attack)
    else:
        damage, critical, efficacity, attack = Individu.damage_calculator(window.enemy, window.notre_pokemon, window.enemy.list_atk[rd.randint(0,len(window.enemy.list_atk) - 1)])
        animation_notre_pokemon(window,damage,critical,efficacity,attack)

def run_attack(window,id_atk):
    window.gridLayoutWidget.hide()
    window.verticalLayoutWidget.hide()
    notre_pokemon = window.notre_pokemon
    go_on = True
    
    if first_player(window):
        hit_someone(window, 1, id_atk)
        if check_capture(window):
            hit_someone(window, 0)
            go_on = check_living(window)
        else:
            go_on = False
    else:
        hit_someone(window, 0)
        if check_living(window):
            hit_someone(window, 1, id_atk)
            go_on = check_capture(window)
        else:
            go_on = False
    
    if go_on:
        window.verticalLayoutWidget.show()
    
    window.attaque1.clicked.disconnect(window.attack_1_button)
    window.attaque2.clicked.disconnect(window.attack_2_button)
    window.attaque3.clicked.disconnect(window.attack_3_button)
    window.attaque4.clicked.disconnect(window.attack_4_button)
    


def check_capture(window):
    if window.enemy.hp == 0:
        window.phase = "capture"
        window.areyousure.setText("Do you want this pokemon\nto join your team ?")
        # window.team.add(window.enemy)
        # window.comboBox.addItem(QtGui.QIcon("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"), window.enemy.name + " lvl." + str(window.enemy.level))
        # if window.enemy_with_position is not None:
        #     window.wild.remove(window.enemy_with_position)
        #     window.enemy_with_position = None
        # window.enemy.heal()
        xp = 100 + 5 * window.enemy.level
        for index_team in window.fighters:
            pokemon = window.team.list[index_team]
            name = pokemon.name
            pokemon.receve_xp(xp)
            if pokemon.name != name:
                window.infos_combat.show()
                text = "What!? " + name + " is evolving!"
                display_in_label(window, text)
                QtTest.QTest.qWait(500)
                for i in range(12):
                    window.impagepoke.setGeometry(QtCore.QRect(160 + (i%2) * 4, 320 + (i%2) * 4, 331, 211))
                    window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/blanc/miroir/" + str(pokemon.id_pok - 2 + (i//6)) + ".png"))
                    QtTest.QTest.qWait(100)
                window.impagepoke.setGeometry(QtCore.QRect(160, 320, 331, 211))
                window.infos_combat.hide()
        
        window.widget.show()
        return False
    return True

def check_living(window):
    if window.team.all_ko():
        if window.lives == 3:
            window.coeur3.setPixmap(QtGui.QPixmap("images/divers/coeur_g.png"))
        elif window.lives == 2:
            window.coeur2.setPixmap(QtGui.QPixmap("images/divers/coeur_g.png"))
        elif window.lives == 1:
            window.close()
        
        window.lives -= 1
        
        for index_team in window.team.bag:
            window.team.list[index_team].heal()
        window.sacha.setGeometry(QtCore.QRect(window.width() / 2, window.height() / 2, 19 * window.scale, 25 * window.scale))
        window.fond.setGeometry(QtCore.QRect(-180,-860,1920 * window.scale,1280 * window.scale))
        window.load_map()
        return False
    
    if window.notre_pokemon.hp == 0:
        window.phase = "pokemon ko"
        window.areyousure.setText("Do you want\nto escape ?")
        window.widget.show()
        # change_pokemon(window)
        for index_team in window.team.bag:
            if window.team.list[index_team].hp != 0:
                window.team.set_main(index_team)
                break
        return False
    return True

# def fight(window,enemy):
#     set_up_fight(window, enemy)
#     end = False
#     i = 0
#     while not end:
#         sleep(0.2)
#         enemy.hp -=1
#         update_fight(window,enemy)
        
#         if enemy.hp == 0:
#             end = True
#     return True

def run_pokemon_changement(window):
    window.load_fight()
    window.verticalLayoutWidget.hide()
    go_on = True
    
    if first_player(window):
        upload_pokemon(window, window.team.bag[window.case - 1])
        hit_someone(window, 0)
        go_on = check_living(window)
    else:
        hit_someone(window, 0)
        upload_pokemon(window, window.team.bag[window.case - 1])
    
    if go_on:
        window.verticalLayoutWidget.show()

def change_pokemon(window):
    window.load_inventory()
    window.send_to_fight.show()
    window.see_the_attacks.show()
    if window.phase == "change pokemon":
        window.retour.show()

def escape(window):
    if window.enemy_with_position is not None:
        window.enemy.heal()
        #window.enemy_with_position[1:] = [rd.randint(0,1042),rd.randint(0,686)]
        window.dir = {1:2,2:1,3:4,4:3}[window.dir]
        
        window.load_map()
        window.update_escape()
    else:
        window.load_map()

def run_escape(window):
    window.verticalLayoutWidget.hide()
    
    sp1, sp2 = window.notre_pokemon.speed, window.enemy.speed
    sp1 = int(sp1 * window.notre_pokemon.level / 50) + 5
    sp2 = int(sp2 * window.enemy.level         / 50) + 5
    f = (sp1 * 32 / (int(sp2 / 4) % 255)) + (30 * window.escape_attempts)
    if rd.randint(0, 255) < f:
        window.infos_combat.show()
        text = "You fled like a coward..."
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
        window.infos_combat.hide()
        escape(window)
    else:
        window.infos_combat.show()
        text = "You even didn't manage to escape !"
        display_in_label(window, text)
        QtTest.QTest.qWait(1000)
        window.infos_combat.hide()
        
        window.escape_attempts += 1
        hit_someone(window, 0)
        if check_living(window):
            window.verticalLayoutWidget.show()
        
def yes_button(window):
    if window.phase == "capture":
        window.team.add(window.enemy)
        window.comboBox.addItem(QtGui.QIcon("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"), window.enemy.name + " lvl." + str(window.enemy.level))
        if window.enemy_with_position is not None:
            window.wild.remove(window.enemy_with_position)
            window.enemy_with_position = None
        window.enemy.heal()
        
        window.load_map()
    elif window.phase == "pokemon ko":
        escape(window)
    else:
        window.widget.hide()
        run_escape(window)

def no_button(window):
    if window.phase == "capture":
        if window.enemy_with_position is not None:
            window.wild.remove(window.enemy_with_position)
            window.enemy_with_position = None
        window.load_map()
    elif window.phase == "pokemon ko":
        change_pokemon(window)
    else:
        window.widget.hide()

        