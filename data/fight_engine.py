# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:39:43 2024

@author: Ordi
"""
from time import sleep
import random as rd
from PyQt5 import QtGui, QtCore



def set_up_fight(window):
    upload_pokemon(window, window.team.main)
    window.nompokesauvage.setText(window.enemy[0].name)
    window.progressBarpokesauvage.setMaximum(window.enemy[0].hp_max)
    window.progressBarpokesauvage.setProperty("value", window.enemy[0].hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy[0].id_pok - 1) + ".png"))
    window.load_fight()

def upload_pokemon(window,index_team):
    pokemon = window.team.list[index_team]
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
    
    attacks = window.team.list[index_team].list_atk
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
    notre_poke = window.team.list[window.team.main]
    color = color_health(notre_poke)
    window.progressBar_notre.setProperty("value", notre_poke.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")
    color = color_health(window.enemy[0])
    window.progressBarpokesauvage.setProperty("value", window.enemy[0].hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")

def animation_enemy(window):
    window.imagepokesauvage.setGeometry(QtCore.QRect(643, 323, 331, 211))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/rouge/" + str(window.enemy[0].id_pok - 1) + ".png"))
    sleep(1)
    window.imagepokesauvage.setGeometry(QtCore.QRect(640, 320, 331, 211))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(window.enemy[0].id_pok - 1) + ".png"))

def choose_attack(window):
    window.gridLayoutWidget.show()

def attack1_selected(window):
    run_attack(window, 0)

def attack2_selected(window):
    run_attack(window, 1)

def attack3_selected(window):
    run_attack(window, 2)

def attack4_selected(window):
    run_attack(window, 3)

def set_up_invotory(window):
    n = window.team.len
    window.widget_1.hide()
    window.widget_2.hide()
    window.widget_3.hide()
    window.widget_4.hide()
    window.widget_5.hide()
    window.widget_6.hide()
    if n > 0:
        window.widget_1.show()
        put_in_inventory(window, window.team.list[window.team.bag[0]], 1)
        if n > 1:
            window.widget_2.show()
            put_in_inventory(window, window.team.list[window.team.bag[1]], 2)
            if n > 2:
                window.widget_3.show()
                put_in_inventory(window, window.team.list[window.team.bag[2]], 3)
                if n > 3:
                    window.widget_4.show()
                    put_in_inventory(window, window.team.list[window.team.bag[3]], 4)
                    if n > 4:
                        window.widget_5.show()
                        put_in_inventory(window, window.team.list[window.team.bag[4]], 5)
                        if n > 5:
                            window.widget_6.show()
                            put_in_inventory(window, window.team.list[window.team.bag[5]], 6)


def put_in_inventory(window,pokemon,inventory_index):
    if inventory_index == 1:
        window.image1.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom1.setText(pokemon.name)
        window.pv1.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 2:
        window.image2.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom2.setText(pokemon.name)
        window.pv2.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 3:
        window.image3.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom3.setText(pokemon.name)
        window.pv3.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 4:
        window.image4.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom4.setText(pokemon.name)
        window.pv4.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 5:
        window.image5.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom5.setText(pokemon.name)
        window.pv5.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 6:
        window.image6.setPixmap(QtGui.QPixmap("images/divers/" + str(pokemon.id_pok) + ".png"))
        window.nom6.setText(pokemon.name)
        window.pv6.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))


def change_pokemon(window):
    
    window.load_inventory()

def run_attack(window,id_atk):
    window.gridLayoutWidget.hide()
    index = window.team.main
    notre_pokemon = window.team.list[index]
    sp1, sp2 = notre_pokemon.speed, window.enemy[0].speed
    if sp1 == sp2:
        first_player = rd.randint(0,1)
    else:
        first_player = sp1 < sp2
    
    if first_player:
        notre_pokemon.hit(window.enemy[0],id_atk)
        update_fight(window)
        animation_enemy(window)
        sleep(2)
        if check_capture(window):
            window.enemy[0].hit(notre_pokemon,0)
            update_fight(window)
            check_living(window)
    else:
        window.enemy[0].hit(notre_pokemon,0)
        update_fight(window)
        sleep(2)
        if check_living(window):
            notre_pokemon.hit(window.enemy[0],id_atk)
            update_fight(window)
            animation_enemy(window)
            check_capture(window)

def check_capture(window):
    if window.enemy[0].hp == 0:
        window.team.add(window.enemy[0])
        window.wild.remove(window.enemy)
        window.load_map()
        return False
    return True

def check_living(window):
    return True
    return window.notre_pokemon.hp > 0
    if window.notre_pokemon.hp == 0:
        pass

def fight(window,enemy):
    set_up_fight(window, enemy)
    end = False
    i = 0
    while not end:
        sleep(0.2)
        enemy.hp -=1
        update_fight(window,enemy)
        
        if enemy.hp == 0:
            end = True
    return True
    