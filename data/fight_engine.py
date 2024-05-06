# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:39:43 2024

@author: Ordi
"""
from time import sleep
from PyQt5 import QtGui



def set_up_fight(window,enemy):
    notre_poke = window.team.list[window.team.main]
    window.nompoke.setText(notre_poke.name)
    window.nompokesauvage.setText(enemy.name)
    window.progressBar_notre.setMaximum(notre_poke.hp_max)
    window.progressBar_notre.setProperty("value", notre_poke.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
    window.progressBarpokesauvage.setMaximum(enemy.hp_max)
    window.progressBarpokesauvage.setProperty("value", enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
    window.impagepoke.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(notre_poke.id_pok - 1) + ".png"))
    window.imagepokesauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(enemy.id_pok - 1) + ".png"))

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
    
def update_fight(window,enemy):
    notre_poke = window.team.list[window.team.main]
    color = color_health(notre_poke)
    window.progressBar_notre.setProperty("value", notre_poke.hp)
    window.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")
    color = color_health(enemy)
    window.progressBarpokesauvage.setProperty("value", enemy.hp)
    window.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: " + color + ";\n""    width: 20px;\n""}")



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
    