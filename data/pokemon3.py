# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:23:55 2024

@author: Formation
"""
import numpy as np
import pandas as pd

class Pokemon:
    types = np.array([[ 0.5 ,  1  ,  1  , 0.5 , 0.5 , 0.5 ,  2  ,  2  ,  1  ,  1  ,  1  ,  1  ,  1  ,  2  ,  1  ,  1  ,  1  ,  1  ],
                      [  2  ,  1  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  2  , 0.5 ,  2  ,  1  , 0.5 , 0.5 ,  2  ,  1  ,  0  ,  2  , 0.5 ],
                      [ 0.5 ,  1  ,  2  ,  1  ,  1  ,  1  ,  0  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ],
                      [  1  ,  1  , 0.5 , 0.5 ,  1  ,  2  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  2  ,  2  ,  1  ,  1  ,  1  ],
                      [  1  ,  1  , 0.5 ,  2  , 0.5 ,  1  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  0  ,  1  ,  1  ,  2  ],
                      [  2  ,  1  , 0.5 , 0.5 ,  1  , 0.5 ,  1  ,  2  ,  2  ,  1  ,  2  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  1  ],
                      [ 0.5 ,  2  ,  2  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  1  ,  2  ,  1  ],
                      [ 0.5 ,  1  ,  2  , 0.5 ,  1  , 0.5 ,  1  , 0.5 ,  1  ,  1  ,  2  ,  1  ,  1  ,  1  ,  2  ,  1  ,  1  ,  2  ],
                      [ 0.5 , 0.5 ,  1  ,  1  ,  1  , 0.5 , 0.5 ,  1  ,  1  ,  1  ,  2  , 0.5 ,  2  ,  1  ,  1  , 0.5 ,  2  , 0.5 ],
                      [ 0.5 ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  0  ,  1  ,  1  ],
                      [ 0.5 ,  1  , 0.5 ,  2  ,  1  , 0.5 ,  1  ,  1  , 0.5 ,  1  , 0.5 , 0.5 ,  1  ,  2  ,  2  ,  1  ,  1  , 0.5 ],
                      [  0  ,  1  ,  1  ,  1  ,  1  ,  1  ,  2  ,  1  ,  1  ,  1  ,  2  , 0.5 ,  1  , 0.5 , 0.5 , 0.5 ,  1  ,  1  ],
                      [ 0.5 ,  2  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  2  , 0.5 ,  1  ,  1  ,  1  ,  0  ,  1  ],
                      [ 0.5 , 0.5 ,  1  ,  1  ,  1  ,  2  ,  1  ,  2  ,  2  ,  1  ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  2  ],
                      [  2  ,  1  ,  1  ,  1  ,  2  ,  2  ,  1  ,  1  , 0.5 ,  1  , 0.5 ,  2  ,  1  ,  2  ,  1  ,  1  ,  1  ,  0  ],
                      [  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  1  ,  0  ,  1  ,  1  ,  2  ,  1  ,  1  ,  2  , 0.5 ,  1  ],
                      [  1  , 0.5 ,  1  ,  1  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  1  ,  1  ,  2  ,  1  ,  1  ,  2  , 0.5 ,  1  ],
                      [ 0.5 ,  2  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  2  ,  1  ,  2  ,  1  ,  1  , 0.5 ,  1  ,  1  ,  1  ,  1  ]])
                      
    
    attribution = {"Steel":0,"Fighting":1, "Dragon":2, "Water":3, "Electric":4, "Fire":5, "Fairy":6, 
                   "Ice" :7, "Bug":8, "Normal":9, "Grass":10, "Poison":11, "Psychic":12, "Rock":13, 
                   "Ground":14, "Ghost":15, "Dark":16, "Flying":17}
    
    def __init__(self,info):
        self.id_pok     = info[0]
        self.name       = info[1]
        self.type1      = info[2]
        self.type2      = info[3]
        self.total      = info[4]
        self.hp_max     = info[5]
        self.attack     = info[6]
        self.defense    = info[7]
        self.spatk      = info[8]
        self.spdef      = info[9]
        self.speed      = info[10]
        self.generation = info[11]
        self.legendary  = info[12]


class Attack():
    def __init__(self,power, typ = None):
        self.power = power
        self.type = typ

class Individu(Pokemon):
    n = 0
    
    def __init__(self,info,attacks):
        super().__init__(info)
        self.hp = self.hp_max
        self.level = 1
        self.list_atk = attacks
        self.id = Individu.n
        Individu.n += 1
    
    def subir(self,pok,puissance,typ = None):
        if typ is None:
            self.hp -= (int(pok.attack * puissance * 0.4 / self.defense) + 2)
        elif self.type2 is np.nan:
            self.hp -= int((int(pok.attack * puissance * 0.4 / self.defense) + 2) * Pokemon.types[typ,Pokemon.attribution[self.type1]])
        else:
            self.hp -= int((int(pok.attack * puissance * 0.4 / self.defense) + 2) * Pokemon.types[typ, Pokemon.attribution[self.type1]] * Pokemon.types[typ, Pokemon.attribution[self.type2]])
        
        if self.hp < 0:
            self.hp = 0
    
    def hit(self,enemy,id_atk):
        if self.list_atk[id_atk].type is None:
            enemy.hp -= (int(self.attack * self.list_atk[id_atk].power * 0.4 / enemy.defense) + 2)
        elif enemy.type2 is np.nan:
            enemy.hp -= int((int(self.attack * self.list_atk[id_atk].power * 0.4 / enemy.defense) + 2) * Pokemon.types[self.list_atk[id_atk].type,Pokemon.attribution[enemy.type1]])
        else:
            enemy.hp -= int((int(self.attack * self.list_atk[id_atk].power * 0.4 / enemy.defense) + 2) * Pokemon.types[self.list_atk[id_atk].type,Pokemon.attribution[enemy.type1]] * Pokemon.types[self.list_atk[id_atk].type,Pokemon.attribution[enemy.type2]])
        
        if enemy.hp < 0:
            enemy.hp = 0

if True:
#if __name__ == "__main__":
    liste_pokemon = pd.read_csv('pokemon_first_gen.csv',sep = ',').to_numpy()
    charge = Attack(20)
    feuille = Attack(20,10)
    feu = Attack(20,5)
    eau = Attack(20,3)
    bulbi = Individu(liste_pokemon[0],[charge,feuille])
    sala  = Individu(liste_pokemon[3],[charge,feu])
    cara  = Individu(liste_pokemon[6],[charge,eau])
    
    pika = Individu(liste_pokemon[24],[charge])
    l_pika = [[pika, 210,400]]