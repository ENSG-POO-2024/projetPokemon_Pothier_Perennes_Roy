# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:09:17 2024

@author: Ordi
"""

from PyQt5 import QtGui

def set_up_inventory(window):
    n = window.team.len
    window.widget_1.hide()
    window.bp1.hide()
    window.widget_2.hide()
    window.bp2.hide()
    window.widget_3.hide()
    window.bp3.hide()
    window.widget_4.hide()
    window.bp4.hide()
    window.widget_5.hide()
    window.bp5.hide()
    window.widget_6.hide()
    window.bp6.hide()
    if n > 0:
        window.widget_1.show()
        window.bp1.show()
        put_in_inventory(window, window.team.list[window.team.bag[0]], 1)
        if n > 1:
            window.widget_2.show()
            window.bp2.show()
            put_in_inventory(window, window.team.list[window.team.bag[1]], 2)
            if n > 2:
                window.widget_3.show()
                window.bp3.show()
                put_in_inventory(window, window.team.list[window.team.bag[2]], 3)
                if n > 3:
                    window.widget_4.show()
                    window.bp4.show()
                    put_in_inventory(window, window.team.list[window.team.bag[3]], 4)
                    if n > 4:
                        window.widget_5.show()
                        window.bp5.show()
                        put_in_inventory(window, window.team.list[window.team.bag[4]], 5)
                        if n > 5:
                            window.widget_6.show()
                            window.bp6.show()
                            put_in_inventory(window, window.team.list[window.team.bag[5]], 6)

def put_in_inventory(window,pokemon,inventory_index):
    if inventory_index == 1:
        window.image1.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom1.setText(pokemon.name)
        window.pv1.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 2:
        window.image2.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom2.setText(pokemon.name)
        window.pv2.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 3:
        window.image3.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom3.setText(pokemon.name)
        window.pv3.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 4:
        window.image4.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom4.setText(pokemon.name)
        window.pv4.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 5:
        window.image5.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom5.setText(pokemon.name)
        window.pv5.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 6:
        window.image6.setPixmap(QtGui.QPixmap("images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.nom6.setText(pokemon.name)
        window.pv6.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))

def inventory_clicked(window):
    pass