# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:22:39 2024

@author: Ordi
"""
from time import time
import numpy  as np
import random as rd
from pokemon3 import Individu
from fight_engine import set_up_fight
from initialisation import liste_pokemon
from PyQt5 import QtCore, QtGui

house_x = 673
house_y = 1057


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
            if window.sacha.y() > window.height() - window.sacha.height() - window.offset:
                window.sacha.move(window.sacha.x(), window.height() - window.sacha.height() - window.offset)
            window.fond.move(window.fond.x(), window.fond.y() + window.speed)
        elif window.sacha.y() + window.sacha.height() < window.height() / 2:
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
        elif window.sacha.x() + window.sacha.width() < window.width() / 2:
            window.sacha.move(window.sacha.x() + window.speed, window.sacha.y())
            window.fond.move(window.fond.x() + window.speed, window.fond.y())

def check_pokemon(window):
    for pokemon in window.wild:
        if (window.sacha.x() - window.fond.x() < pokemon[1] + 48 - 1 + 26 and
            window.sacha.x() + window.sacha.width() - 1 - window.fond.x() + 26 > pokemon[1] and
            window.sacha.y() - window.fond.y() < pokemon[2] + 48 - 1 + 26 and
            window.sacha.y() + window.sacha.height() - 1 - window.fond.y() + 26 > pokemon[2]):
            window.pokemon_sauvage.setGeometry(QtCore.QRect(pokemon[1] + window.fond.x() , pokemon[2] + window.fond.y(), 48, 48))
            window.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon[0].id_pok - 1) + ".png"))
            window.pokemon_sauvage.show()
            return True, pokemon
    window.pokemon_sauvage.hide()
    return False, None

def check_fight(window,pokemon):
    if (window.sacha.x() - window.fond.x() < pokemon[1] + 48 - 1 and
        window.sacha.x() + window.sacha.width() - 1 - window.fond.x() > pokemon[1] and
        window.sacha.y() - window.fond.y() < pokemon[2] + 48 - 1 and
        window.sacha.y() + window.sacha.height() - 1 - window.fond.y() > pokemon[2]):
        window.enemy = pokemon[0]
        window.enemy_with_position = pokemon
        window.notre_pokemon = window.team.list[window.team.main]
        window.escape_attempts = 0
        set_up_fight(window)

def check_zone(window):
    for zone in window.zones:
        if (window.sacha.x() - window.fond.x(), window.sacha.y() - window.fond.y(), window.sacha.width(), window.sacha.height()) in zone:
            if rd.random() < zone.p:
                zone.p = 0.1
                level = rd.randint(zone.level_min, zone.level_max)
                index_pokemon = zone.id_pok()
                if index_pokemon == 128:
                    enemy = Individu(liste_pokemon[index_pokemon],[window.atk_lib[-1]],1)
                else:
                    enemy = Individu(liste_pokemon[index_pokemon],[window.atk_lib[0]],1)
                enemy.receve_xp(Individu.xp_total(level),True)
                window.enemy = enemy
                window.notre_pokemon = window.team.list[window.team.main]
                window.escape_attempts = 0
                set_up_fight(window)
            else:
                zone.p += (1 - zone.p) / 20
            break

def check_house(window):
    if (window.sacha.x() - window.fond.x() < house_x + window.maison.width()  and
        window.sacha.x() - window.fond.x() + window.sacha.width() > house_x   and
        window.sacha.y() - window.fond.y() < house_y + window.maison.height() and
        window.sacha.y() - window.fond.y() + window.sacha.height() > + house_y):
        window.maison.show()
        return True
    else:
        window.maison.hide()
        return False

def check_colision(window):
    if window.dir == 1:
        y = window.sacha.y() - window.fond.y()
        x = window.sacha.x() - window.fond.x()
        for y_limit in range(y - window.speed, y):
            for start,stop in up_limit[y_limit]:
                if x <= stop and (x + window.sacha.width() - 1) >= start:
                    window.speed = y - y_limit - 1
    
    elif window.dir == 2:
        y = window.sacha.y() + window.sacha.height() - 1 - window.fond.y()
        x = window.sacha.x() - window.fond.x()
        for y_limit in range(y + window.speed, y, -1):
            for start,stop in down_limit[y_limit]:
                if x <= stop and (x + window.sacha.width() - 1) >= start:
                    window.speed = y_limit - y - 1
    
    elif window.dir == 3:
        x = window.sacha.x() - window.fond.x()
        y = window.sacha.y() - window.fond.y()
        for x_limit in range(x - window.speed, x):
            for start,stop in left_limit[x_limit]:
                if y <= stop and (y + window.sacha.height() - 1) >= start:
                    window.speed = x - x_limit - 1
    
    elif window.dir == 4:
        x = window.sacha.x() + window.sacha.width() - 1 - window.fond.x()
        y = window.sacha.y() - window.fond.y()
        for x_limit in range(x + window.speed, x, -1):
            for start,stop in right_limit[x_limit]:
                if y <= stop and (y + window.sacha.width() - 1) >= start:
                    window.speed = x_limit - x - 1
    



def update_position(window):
    check_colision(window)
    check_position(window)
    
    
    
    
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
    window.maison.move(window.fond.x() + house_x, window.fond.y() + house_y)
    
    
    check_house(window)
    if window.speed:
        check_zone(window)
    p1, p2 = check_pokemon(window)
    if p1:
        check_fight(window, p2)
    
    window.speed = 12
    window.time = time()



up_limit    = [[] for _ in range(1920)]
down_limit  = [[] for _ in range(1920)]
left_limit  = [[] for _ in range(2880)]
right_limit = [[] for _ in range(2880)]

up_db    = np.genfromtxt("bounds/up.txt"   , dtype = int, delimiter = ',')
down_db  = np.genfromtxt("bounds/down.txt" , dtype = int, delimiter = ',')
left_db  = np.genfromtxt("bounds/left.txt" , dtype = int, delimiter = ',')
right_db = np.genfromtxt("bounds/right.txt", dtype = int, delimiter = ',')

for position,start,stop in up_db:
    up_limit[position].append((start,stop))
for position,start,stop in down_db:
    down_limit[position].append((start,stop))
for position,start,stop in left_db:
    left_limit[position].append((start,stop))
for position,start,stop in right_db:
    right_limit[position].append((start,stop))
