# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:22:39 2024

@author: Ordi
"""
from time import time
import random as rd
from pokemon3 import Individu
from fight_engine import set_up_fight
from initialisation import liste_pokemon
from PyQt5 import QtCore, QtGui


def check_position(window):
    if window.dir == 1:
        if window.fond.y() > - window.speed:
            window.sacha.move(window.sacha.x(), window.sacha.y() - window.speed)
            if window.sacha.y() < 0:
                window.sacha.move(window.sacha.x(), 0)
            window.fond.move(window.fond.x(), window.fond.y() - window.speed)
        elif window.sacha.y() > window.height() / 2:
            window.sacha.move(window.sacha.x(), window.sacha.y() - window.speed)
            window.fond.move(window.fond.x(), window.fond.y() - window.speed)
    if window.dir == 2:
        if window.fond.y() + window.fond.height() < window.height() + window.speed:
            window.sacha.move(window.sacha.x(), window.sacha.y() + window.speed)
            if window.sacha.y() > window.height() - window.sacha.height():
                window.sacha.move(window.sacha.x(), window.height() - window.sacha.height())
            window.fond.move(window.fond.x(), window.fond.y() + window.speed)
        elif window.sacha.y() < window.height() / 2:
            window.sacha.move(window.sacha.x(), window.sacha.y() + window.speed)
            window.fond.move(window.fond.x(), window.fond.y() + window.speed)
    if window.dir == 3:
        if window.fond.x() > - window.speed:
            window.sacha.move(window.sacha.x() - window.speed, window.sacha.y())
            if window.sacha.x() < 0:
                window.sacha.move(0, window.sacha.y())
            window.fond.move(window.fond.x() - window.speed, window.fond.y())
        elif window.sacha.x() > window.width() / 2:
            window.sacha.move(window.sacha.x() - window.speed, window.sacha.y())
            window.fond.move(window.fond.x() - window.speed, window.fond.y())
    if window.dir == 4:
        if window.fond.x() + window.fond.width() < window.width() + window.speed:
            window.sacha.move(window.sacha.x() + window.speed, window.sacha.y())
            if window.sacha.x() > window.width() - window.sacha.width():
                window.sacha.move(window.width() - window.sacha.width(), window.sacha.y())
            window.fond.move(window.fond.x() + window.speed, window.fond.y())
        elif window.sacha.x() < window.width() / 2:
            window.sacha.move(window.sacha.x() + window.speed, window.sacha.y())
            window.fond.move(window.fond.x() + window.speed, window.fond.y())

def check_pokemon(window):
    for pokemon in window.wild:
        if (window.sacha.x() < pokemon[1] + 25 + 10 and
            window.sacha.x() + window.sacha.width() + 10 > pokemon[1] and
            window.sacha.y() < pokemon[2] + 26 + 10 and
            window.sacha.y() + window.sacha.height() + 10 > pokemon[2]):
            window.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon[0].id_pok - 1) + ".png"))
            window.pokemon_sauvage.setGeometry(QtCore.QRect(pokemon[1], pokemon[2], 25, 26))
            window.pokemon_sauvage.show()
            return True, pokemon
    return False, None

def check_fight(window,pokemon):
    if (window.sacha.x() < pokemon[1] + 25 and
        window.sacha.x() + window.sacha.width() > pokemon[1] and
        window.sacha.y() < pokemon[2] + 26 and
        window.sacha.y() + window.sacha.height() > pokemon[2]):
        window.enemy = pokemon[0]
        window.enemy_with_position = pokemon
        window.notre_pokemon = window.team.list[window.team.main]
        set_up_fight(window)

def check_zone(window):
    for zone in window.zones:
        if window.sacha in zone:
            if rd.random() < zone.p:
                enemy = Individu(liste_pokemon[zone.id_pok()],[window.atk_lib[0]])
                window.enemy = enemy
                window.notre_pokemon = window.team.list[window.team.main]
                set_up_fight(window)
            break

def check_house(window):
    if (window.sacha.x() < window.maison.x() + window.maison.width()  and
        window.sacha.x() + window.sacha.width() > window.maison.x()   and
        window.sacha.y() < window.maison.y() + window.maison.height() and
        window.sacha.y() + window.sacha.height() > window.maison.y()):
        window.maison.show()
        return True
    else:
        window.maison.hide()
        return False

















def update_position(window):
    check_position(window)
    # p1, p2 = check_pokemon(window)
    # if p1:
    #     check_fight(window, p2)
    # check_zone(window)
    # check_house(window)
    
    
    
    
    name = {1:"up", 2:"down", 3:"left", 4:"right", 0:"down"}[window.dir]
    dx = {0:0, 1:0, 2: 0, 3:1, 4:-1}[window.dir] * window.speed
    dy = {0:0, 1:1, 2:-1, 3:0, 4: 0}[window.dir] * window.speed
    
    if time() - window.time < 0.5:
    
        if (window.moves % 6) == 4:
            window.name = name + "0"
        elif (window.moves % 12) == 1:
            window.name = name + "1"
        elif (window.moves % 12) == 7:
            window.name = name + "2"
        window.moves += 1
    
    else:
        window.moves = 0
        window.name = name + "0"

    window.sacha.setPixmap(QtGui.QPixmap("images/animation/" + window.name + ".png"))
    window.fond.move(window.fond.x() + dx, window.fond.y() + dy)
    
    window.time = time()