# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:09:17 2024

@author: Ordi
"""

from PyQt5 import QtGui

def set_up_inventory(window):
    """
    Installe l'inventaire mais ne le load pas

    Parameters
    ----------
    window : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
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
        if window.team.main == window.team.bag[0]:
            window.couronne1.show()
        if n > 1:
            window.widget_2.show()
            window.bp2.show()
            put_in_inventory(window, window.team.list[window.team.bag[1]], 2)
            if window.team.main == window.team.bag[1]:
                window.couronne2.show()
            if n > 2:
                window.widget_3.show()
                window.bp3.show()
                put_in_inventory(window, window.team.list[window.team.bag[2]], 3)
                if window.team.main == window.team.bag[2]:
                    window.couronne3.show()
                if n > 3:
                    window.widget_4.show()
                    window.bp4.show()
                    put_in_inventory(window, window.team.list[window.team.bag[3]], 4)
                    if window.team.main == window.team.bag[3]:
                        window.couronne4.show()
                    if n > 4:
                        window.widget_5.show()
                        window.bp5.show()
                        put_in_inventory(window, window.team.list[window.team.bag[4]], 5)
                        if window.team.main == window.team.bag[4]:
                            window.couronne5.show()
                        if n > 5:
                            window.widget_6.show()
                            window.bp6.show()
                            put_in_inventory(window, window.team.list[window.team.bag[5]], 6)
                            if window.team.main == window.team.bag[5]:
                                window.couronne6.show()

def put_in_inventory(window,pokemon,inventory_index):
    """
    Met un pokemon dans l'inventaire

    Parameters
    ----------
    window : TYPE
        DESCRIPTION.
    pokemon : TYPE
        DESCRIPTION. pokemon à mettre dans l'inventaire
    inventory_index : TYPE
        DESCRIPTION. n° du slot de l'inventaire dans lequel il faut placer le pokemon

    Returns
    -------
    None.

    """
    if inventory_index == 1:
        window.image1.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image1.setScaledContents(True)
        window.nom1.setText(pokemon.name)
        window.pv1.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 2:
        window.image2.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image2.setScaledContents(True)
        window.nom2.setText(pokemon.name)
        window.pv2.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 3:
        window.image3.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image3.setScaledContents(True)
        window.nom3.setText(pokemon.name)
        window.pv3.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 4:
        window.image4.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image4.setScaledContents(True)
        window.nom4.setText(pokemon.name)
        window.pv4.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 5:
        window.image5.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image5.setScaledContents(True)
        window.nom5.setText(pokemon.name)
        window.pv5.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))
    elif inventory_index == 6:
        window.image6.setPixmap(QtGui.QPixmap("../data/images/pokemon/blanc/" + str(pokemon.id_pok - 1) + ".png"))
        window.image6.setScaledContents(True)
        window.nom6.setText(pokemon.name)
        window.pv6.setText(str(pokemon.hp) + "/" + str(pokemon.hp_max))