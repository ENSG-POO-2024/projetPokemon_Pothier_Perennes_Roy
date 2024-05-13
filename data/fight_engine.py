# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:39:43 2024

@author: Ordi
"""
from time import sleep
import random as rd
from pokemon3 import Individu
from PyQt5 import QtGui, QtCore



def set_up_fight(window):
    upload_pokemon(window, window.team.main)
    window.nompokesauvage.setText(window.enemy.name)
    window.progressBarpokesauvage.setMaximum(window.enemy.hp_max)
    window.progressBarpokesauvage.setProperty("value", window.enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"))
    window.load_fight()

def upload_pokemon(window,index_team):
    pokemon = window.team.list[index_team]
    window.notre_pokemon = pokemon
    window.nompoke.setText(pokemon.name)
    color = color_health(pokemon)
    window.progressBar_notre.setMaximum(pokemon.hp_max)
    window.progressBar_notre.setProperty("value", pokemon.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")
    window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/blanc/miroir/" + str(pokemon.id_pok - 1) + ".png"))
    window.attaque1.hide()
    window.attaque2.hide()
    window.attaque3.hide()
    window.attaque4.hide()
    
    attacks = pokemon.list_atk
    n = len(attacks)
    if n > 0:
        window.attaque1.setText(attacks[0].name)
        window.attaque1.show()
        if n > 1:
            window.attaque2.setText(attacks[1].name)
            window.attaque2.show()
            if n > 2:
                window.attaque3.setText(attacks[2].name)
                window.attaque3.show()
                if n > 3:
                    window.attaque4.setText(attacks[3].name)
                    window.attaque4.show()


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
    window.progressBarpokesauvage.setProperty("value", window.enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")

def animation_enemy(window):
    window.imagepokesauvage.setGeometry(QtCore.QRect(643, 323, 331, 211))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/rouge/" + str(window.enemy.id_pok - 1) + ".png"))
    sleep(1)
    window.imagepokesauvage.setGeometry(QtCore.QRect(640, 320, 331, 211))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"))

def animation_notre_pokemon(window):
    sleep(1)

def choose_attack(window):
    window.attaque1.clicked.connect(window.attack_1_button)
    window.attaque2.clicked.connect(window.attack_2_button)
    window.attaque3.clicked.connect(window.attack_3_button)
    window.attaque4.clicked.connect(window.attack_4_button)
    window.gridLayoutWidget.show()

def attack1_selected(window):
    run_attack(window, 0)

def attack2_selected(window):
    run_attack(window, 1)

def attack3_selected(window):
    run_attack(window, 2)

def attack4_selected(window):
    run_attack(window, 3)

def first_player(window):
    sp1, sp2 = window.notre_pokemon.speed, window.enemy.speed
    if sp1 == sp2:
        return rd.randint(0, 1)
    else:
        return sp1 > sp2

def hit_someone(window,order,id_atk = None):
    if order:
        window.notre_pokemon.hit(window.enemy,id_atk)
        update_fight(window)
        animation_enemy(window)
    else:
        window.enemy.hit(window.notre_pokemon,rd.randint(0,len(window.enemy.list_atk) - 1))
        update_fight(window)
        animation_notre_pokemon

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
        window.team.add(window.enemy)
        window.comboBox.addItem(QtGui.QIcon("images/pokemon/blanc/" + str(window.enemy.id_pok - 1) + ".png"), window.enemy.name + " lvl." + str(window.enemy.level))
        if window.enemy_with_position is not None:
            window.wild.remove(window.enemy_with_position)
            window.enemy_with_position = None
        window.enemy.heal()
        window.load_map()
        return False
    return True

def check_living(window):
    if window.notre_pokemon.hp == 0:
        window.phase = "pokemon ko"
        change_pokemon(window)
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

def escape(window):
    if window.enemy_with_position is not None:
        window.enemy.heal()
        #window.enemy_with_position[1:] = [rd.randint(0,1042),rd.randint(0,686)]
        dx = {0:0, 1: 0, 2:4, 3:-4}[window.sacha_dir]
        dy = {0:4, 1:-4, 2:0, 3: 0}[window.sacha_dir]
        window.sacha_dx = dx
        window.sacha_dy = dy
        
        window.load_map()
        window.update_position()
    else:
        window.load_map()

def run_escape(window):
    window.verticalLayoutWidget.hide()
    
    if first_player(window):
        escape(window)
    else:
        hit_someone(window, 0)
        escape(window)
        


        