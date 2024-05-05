# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:23:55 2024

@author: Formation
"""
import numpy  as np
import pandas as pd
import random as rd

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
                   "Ground":14, "Ghost":15, "Dark":16, "Flying":17, np.nan:None}
    
    def __init__(self,info):
        self.id_pok     = info[0]
        self.name       = info[1]
        self.type1      = Pokemon.attribution[info[2]]
        self.type2      = Pokemon.attribution[info[3]]
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
    def __init__(self,power,special = False, typ = None):
        self.power = power
        self.type = typ
        self.special = special

class Individu(Pokemon):
    n = 0
    
    def __init__(self,info,attacks):
        super().__init__(info)
        self.hp = self.hp_max
        self.level = 1
        self.list_atk = attacks
        self.id = Individu.n
        Individu.n += 1
    
    def subir(self,pok,attack):
        self.hp -= Individu.damage_calculator(pok, self, attack)
        
        if self.hp < 0:
            self.hp = 0
    
    def hit(self,enemy,id_atk):
        enemy.hp -= Individu.damage_calculator(self, enemy, self.list_atk[id_atk])
        
        if enemy.hp < 0:
            enemy.hp = 0
    
    @staticmethod
    def efficacity(type_attack,type_defense):
        if type_attack is None or type_defense is None:
            return 1
        else:
            return Pokemon.types[type_attack,type_defense]
    
    @staticmethod
    def CM(attacker,target,attack):
        CM = 1
        
        #STAB
        if attack.type is not None:
            if ((attack.type == attacker.type1) or
                (attack.type == attacker.type2)):
                CM *= 1.5
        
        #efficacity
        CM *= Individu.efficacity(attack.type, target.type1)
        CM *= Individu.efficacity(attack.type, target.type2)
        
        #critical
        if rd.random() > 0.8:
            CM *= 2
        
        #alea
        CM *= rd.uniform(0.85,1)
        
        
        return CM
    
    @staticmethod
    def damage_calculator(attacker,target,attack):
        CM = Individu.CM(attacker,target,attack)
        
        #damage calcul
        damage = int(attacker.level * 0.4 + 2)
        
        
        if attack.special:
            damage = int(damage * attacker.spatk  * attack.power / target.spdef  )
        else:
            damage = int(damage * attacker.attack * attack.power / target.defense)
        
        damage = int(damage / 50) + 2
        
        damage = int(damage * CM)
        
        return damage
            

if True:
#if __name__ == "__main__":
    liste_pokemon = pd.read_csv('pokemon_first_gen.csv',sep = ',').to_numpy()
    charge = Attack(40)
    feuille = Attack(40,typ = 10)
    feu = Attack(40, typ = 5)
    eau = Attack(40, typ = 3)
    bulbi = Individu(liste_pokemon[0],[charge,feuille])
    sala  = Individu(liste_pokemon[3],[charge,feu])
    cara  = Individu(liste_pokemon[6],[charge,eau])
    
    pika = Individu(liste_pokemon[24],[charge])
    l_pika = [[pika, 210,520]]