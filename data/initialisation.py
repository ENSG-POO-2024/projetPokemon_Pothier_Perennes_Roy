# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:13:24 2024

@author: Ordi
"""
import numpy  as np
import pandas as pd
import random as rd

from pokemon3 import *

map_width  = 1071 - 25
map_height = 721  - 26


liste_pokemon = pd.read_csv('pokemon_first_gen.csv',sep = ',').to_numpy()
atk_lib = []
atk_lib.append(Attack("charge",80))
atk_lib.append(Attack("feuille",80,10))
atk_lib.append(Attack("feu",80,5))
atk_lib.append(Attack("eau",80,3))
atk_lib.append(Attack("lance flamme",80,5,True))



starting_pack = []
starting_pack.append(Individu(liste_pokemon[0], [atk_lib[0], atk_lib[1]]))
starting_pack.append(Individu(liste_pokemon[3], [atk_lib[0], atk_lib[2]]))
starting_pack.append(Individu(liste_pokemon[6], [atk_lib[0], atk_lib[3]]))



wild = []
wild.append([Individu(liste_pokemon[0], [atk_lib[0], atk_lib[1]])])
wild.append([Individu(liste_pokemon[3], [atk_lib[0], atk_lib[2]])])
wild.append([Individu(liste_pokemon[6], [atk_lib[0], atk_lib[3]])])

for i in range(len(wild)):
    x = rd.randint(0, map_width )
    y = rd.randint(0, map_height)
    wild[i].append(x)
    wild[i].append(y)

# wild[2][1] = 390
# wild[2][2] = 580
print(wild[0][1],wild[0][2])
print(wild[1][1],wild[1][2])
print(wild[2][1],wild[2][2])


info0 = [0,0.1,[9,12,15,84],[0.3,0.3,0.3,0.1]]
Zone0 = Zone(info0)
infos = [0,500,50,50]
zone0 = Sous_Zone(info0 + infos)
info1 = [1,0.8,[26,36,133],[0.33,0.33,0.33]]
Zone1 = Zone(info1)
infos = [700,0,100,600]
zone1 = Sous_Zone(info1 + infos)
zones = [zone0,zone1]