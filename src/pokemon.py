# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:23:55 2024

@author: Formation
"""
import numpy  as np
import pandas as pd
import random as rd

import PyQt5

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
        self.hp_base    = info[5]
        self.attack     = info[6]
        self.defense    = info[7]
        self.spatk      = info[8]
        self.spdef      = info[9]
        self.speed      = info[10]
        self.generation = info[11]
        self.legendary  = info[12]


class Attack():
    def __init__(self,name,power, typ = None, special = False):
        self.name = name
        self.power = power
        self.type = typ
        self.special = special
    
    def __str__(self):
        s_name    = self.name
        s_power   = str(self.power)
        s_type    = str(self.type)
        s_special = str(self.special)
        text = 'Attack("'
        text += s_name    + '",'
        text += s_power   + ','
        text += s_type    + ','
        text += s_special + ')'
        return text

class Individu(Pokemon):
    n = 0
    
    def __init__(self,info,attacks,level = 1):
        super().__init__(info)
        self.xp = 100
        self.level = level
        self.hp_max = int(self.hp_base * level / 50) + level + 10
        self.hp = self.hp_max
        self.list_atk = attacks
        self.range = None
        self.id = Individu.n
        Individu.n += 1
    
    def __str__(self):
        s_id_pok = str(self.id_pok - 1)
        s_level = str(self.level)
        s_xp = str(self.xp)
        s_range = str(self.range)
        s_atk = '['
        for atk in self.list_atk:
            s_atk += str(atk) + ','
        #On enlève la dernière virgule
        s_atk = s_atk[:-1]
        s_atk += ']'
        
        text = 'pokemon = Individu(liste_pokemon[' + s_id_pok + '],'
        text += s_atk + ','
        text += s_level + ')\n'
        text += 'pokemon.xp = ' + s_xp + '\n'
        text += 'pokemon.range = ' + s_range
        
        return text
        
    
    
    def heal(self):
        """
        Soigne le pokemon

        Returns
        -------
        None.

        """
        self.hp = self.hp_max
    
    def receive_xp(self,xp,sauvage = False):
        """
        Fait recevoir de l'xp à un pokemon.
        Le fait level up si besoin.

        Parameters
        ----------
        xp : int
            quantité d'xp à donner au pokemon
        sauvage : bool, optional
            True si le pokemon est sauvage et False sinon. The default is False.

        Returns
        -------
        None.

        """
        #Le niveau max est 100
        if self.level >= 100:
            self.xp = np.inf
        #L'xp correspond à la quantité d'xp manquante pour passer au prochain niveau
        self.xp -= xp
        while self.xp <= 0:
            self.level += 1
            #Fonction d'xp affine
            self.xp += 90 + self.level * 10
            self.level_up(sauvage)
    
    def level_up(self,sauvage):
        """
        Applique le level up
        Vérifie si le pokemon doit apprendre une nouvelle attaque ou s'il doit évoluer.

        Parameters
        ----------
        sauvage : bool
            True si le pokemon est sauvage et False sinon.

        Returns
        -------
        None.

        """
        self.check_attack()
        if not sauvage:
            self.check_evolution()
        self.hp_max = int(self.hp_base * self.level / 50) + self.level + 10
        self.heal()
    
    def check_attack(self):
        """
        Vérifie si le pokemon doit apprendre une nouvelle attaque.
        Si tel est le cas, lui fait apprendre une nouvelle attaque.

        Returns
        -------
        None.

        """
        #Exeption pour Magicarpe
        if self.id_pok == 129:
            if self.level == 15:
                self.list_atk.append(atk_lib[0])
            return
        
        
        if self.level in [5,15,30,50]:
            attack = self.list_atk[0]
            
            while attack in self.list_atk:
                if self.type2 is None:
                    type_attack = self.type1
                else:
                    type_attack = [self.type1,self.type2][rd.randint(0,1)]
                den = self.attack + self.spatk
                fort = (self.level + 1) % 2
                b = rd.choices([fort + 1, fort + 3],[self.attack / den, self.spatk / den])[0]
                a = 4
                index_attack = a * type_attack + b
                attack = atk_lib[index_attack]
            self.list_atk.append(attack)
            
        if self.level == 50:
            self.list_atk.pop(0)
    
    def check_evolution(self):
        """
        Vérifie si un pokemon doit évoluer.
        Si tel est le cas, le fait évoluer.

        Returns
        -------
        None.

        """
        liste_evolution = [16,32,0,16,36,0,16,36,0,7,10,0,7,10,0,18,36,0,20,0,20,0,22,0,25,
                           0,22,0,16,33,0,16,33,0,25,0,25,0,25,0,22,0,21,35,0,24,0,31,0,26,
                           0,28,0,33,0,28,0,25,0,25,40,0,16,40,0,28,40,0,21,35,0,30,0,25,40,
                           0,40,0,37,0,30,0,0,31,0,34,0,38,0,25,0,25,40,0,0,26,0,28,0,30,0,
                           25,0,28,0,0,0,0,35,0,42,0,0,0,0,32,0,33,0,25,0,0,0,0,0,0,0,0,20,
                           0,0,0,25,0,0,0,0,40,0,40,0,0,0,0,0,0,30,55,0,0,0]
        level_required = liste_evolution[self.id_pok - 1]
        if self.level == level_required:
            #Exception pour Evoli
            if self.id_pok == 133:
                evolution = rd.randint(0,2)
                new_pokemon = Individu(liste_pokemon[self.id_pok + evolution],self.list_atk, self.level)
            else:
                new_pokemon = Individu(liste_pokemon[self.id_pok],self.list_atk, self.level)
            self.become(new_pokemon)
    
    def become(self,new_pokemon):
        """
        Transforme self en new_pokemon

        Parameters
        ----------
        new_pokemon : Pokemon
            pokemon à faire devenir

        Returns
        -------
        None.

        """
        self.id_pok     = new_pokemon.id_pok
        self.name       = new_pokemon.name
        self.type1      = new_pokemon.type1
        self.type2      = new_pokemon.type2
        self.total      = new_pokemon.total
        self.hp_base    = new_pokemon.hp_base
        self.attack     = new_pokemon.attack
        self.defense    = new_pokemon.defense
        self.spatk      = new_pokemon.spatk
        self.spdef      = new_pokemon.spdef
        self.speed      = new_pokemon.speed
        self.generation = new_pokemon.generation
        self.legendary  = new_pokemon.legendary
    
    @staticmethod
    def efficacity(type_attack,type_defense):
        """
        Calcul l'efficacité d'une attaque

        Parameters
        ----------
        type_attack : Attack
            attaque
        type_defense : int
            type du pokemon défenseur

        Returns
        -------
        float
            coefficient d'efficacité

        """
        if type_attack is None or type_defense is None:
            return 1
        else:
            return Pokemon.types[type_attack,type_defense]
    
    @staticmethod
    def CM(attacker,target,attack):
        """
        Calcul le coefficient multiplicateur

        Parameters
        ----------
        attacker : Individu
            pokemon attaquant
        target : Individu
            pokemon defenseur
        attack : Attack
            attaque

        Returns
        -------
        CM : float
            Coefficient Multiplicateur
        critical : bool
            True si le coup est critique et False sinon
        efficacity : float
            coefficient d'efficacité

        """
        CM = 1
        critical = False
        
        #STAB
        if attack.type is not None:
            if ((attack.type == attacker.type1) or
                (attack.type == attacker.type2)):
                CM *= 1.5
        
        #efficacity
        efficacity = Individu.efficacity(attack.type, target.type1)
        efficacity *= Individu.efficacity(attack.type, target.type2)
        CM *= efficacity
        
        #critical
        if rd.random() > 0.85:
            CM *= 1.5
            critical = True
        
        #alea
        CM *= rd.uniform(0.85,1)
        
        
        return CM, critical, efficacity
    
    @staticmethod
    def damage_calculator(attacker,target,attack):
        """
        Calcul des dégats

        Parameters
        ----------
        attacker : Individu
            pokemon attaquant
        target : Individu
            pokemon defenseur
        attack : Attack
            attaque

        Returns
        -------
        damage : int
            quantité de dégat
        critical : bool
            True si le coup est critique et False sinon
        efficacity : float
            coefficient d'efficacité
        attack : Attack
            attaque

        """
        CM, critical, efficacity = Individu.CM(attacker,target,attack)
        
        #damage calcul
        damage = int(attacker.level * 0.4 + 2)
        
        
        if attack.special:
            spatk = int(attacker.spatk * attacker.level / 50) + 5
            spdef = int(target.spdef   * target.level   / 50) + 5
            damage = int(damage * spatk  * attack.power / spdef)
        else:
            atk     = int(attacker.attack * attacker.level / 50) + 5
            dfns = int(target.defense  * target.level   / 50) + 5
            damage = int(damage * atk * attack.power / dfns)
        
        damage = int(damage / 50) + 2
        
        damage = int(damage * CM)
        
        return damage, critical, efficacity, attack
    
    @staticmethod
    def xp_total(level):
        """
        Calcul la quantité d'xp necessaire pour passer au niveau n

        Parameters
        ----------
        level : int
            niveau jusqu'où aller i.e. n

        Returns
        -------
        int
            quantité d'xp necessaire pour passer au niveau n

        """
        n = level - 1
        return n * 90 + round(n * level / 2) * 10
    
class Team():
    def __init__(self,team):
        self.list = team
        self.main = 0
        self.bag = [i for i in range(len(team))]
        self.len = len(self.bag)
    
    def __str__(self):
        s_main = str(self.main)
        s_bag  = str(self.bag)
        text = 'team = []\n'
        for pokemon in self.list:
            text += str(pokemon) + '\n'
            text += 'team.append(pokemon)\n'
        text += 'saved_team = Team(team)\n'
        text += 'saved_team.main = ' + s_main + '\n'
        text += 'saved_team.bag = ' + s_bag   + '\n'
        text += 'saved_team.len = len(saved_team.bag)'
        
        return text
    
    def set_main(self,main):
        """
        Définie le pokemon d'indice main comme étant le main pokemon

        Parameters
        ----------
        main : int
            indice du pokemon à définir comme étant le main

        Returns
        -------
        None.

        """
        self.main = main
    
    def __len__(self):
        """
        Renvoie la taille du sac

        Returns
        -------
        int
            nombre de pokemon dans le sac

        """
        return self.len
    
    def add(self,pokemon):
        """
        Ajoute un pokemon dans l'équipe

        Parameters
        ----------
        pokemon : Individu
            pokemon à ajouter

        Returns
        -------
        None.

        """
        pokemon.range = len(self.list)
        self.list.append(pokemon)
        if self.len < 6:
            self.put_in(pokemon.range)
    
    def put_out(self,index_team):
        """
        Retire un pokemon du sac

        Parameters
        ----------
        index_team : int
            indice du pokemon à retirer du sac

        Returns
        -------
        None.

        """
        self.bag.remove(index_team)
        self.len -= 1
        if self.main == index_team:
            self.set_main(self.bag[0])
    
    def put_in(self,index_team):
        """
        Ajoute un pokemon dans le sac

        Parameters
        ----------
        index_team : int
            indice du pokemon à ajouter dans le sac

        Returns
        -------
        None.

        """
        if self.len < 6:
            self.bag.append(index_team)
            self.len += 1
    
    def all_ko(self):
        """
        Vérifie si tous les pokemons du sac sont K.O.

        Returns
        -------
        bool
            True si tous les pokemons sont K.O. et False sinon

        """
        for index_team in self.bag:
            if self.list[index_team].hp != 0:
                return False
        return True

class Zone():
    def __init__(self,info):
        self.id         = info[0]
        self.p          = info[1]
        self.level_min  = info[2]
        self.level_max  = info[3]
        self.population = info[4]
        self.weights    = info[5]
    
    def id_pok(self):
        """
        Génere un pokemon aléatoirement selon la zone

        Returns
        -------
        int
            identifiant du pokemon généré

        """
        return rd.choices(self.population,self.weights)[0]

class Sous_Zone(Zone):
    def __init__(self,info):
        super().__init__(info[:6])
        self.x      = info[6]
        self.y      = info[7]
        self.width  = info[8]
        self.height = info[9]
    
    def __contains__(self,sacha):
        """
        Vérifie si sacha est dans la zone

        Parameters
        ----------
        sacha : PyQt5.QtWidgets.QLabel, list, tuple
            label de sacha ou objet contenant[x,y,width,height] de sacha

        Returns
        -------
        bool
            True si sacha touche la zone et False sinon

        """
        if isinstance(sacha, PyQt5.QtWidgets.QLabel):
            return ((sacha.x() < self.x + self.width)    and
                    (sacha.x() + sacha.width() > self.x) and
                    (sacha.y() < self.y + self.height)   and
                    (sacha.y() + sacha.height() > self.y))
        elif isinstance(sacha, (list,tuple)):
            return ((sacha[0] < self.x + self.width)  and
                    (sacha[0] + sacha[2] > self.x)    and
                    (sacha[1] < self.y + self.height) and
                    (sacha[1] + sacha[3] > self.y))
        
            


liste_pokemon = pd.read_csv('../data/pokemon_first_gen.csv',sep = ',').to_numpy()

atk_lib = []
atk_lib.append(Attack("Tackle",40,9))
atk_lib.append(Attack("Iron Claw",50,0))
atk_lib.append(Attack("Iron Tail",100,0))
atk_lib.append(Attack("Mirror Shot",65,0,True))
atk_lib.append(Attack("Flash Cannon",80,0,True))
atk_lib.append(Attack("Mach Punch",40,1))
atk_lib.append(Attack("Close Combat",120,1))
atk_lib.append(Attack("Vaccuum Wave",40,1,True))
atk_lib.append(Attack("Focus Blast",120,1,True))
atk_lib.append(Attack("Dual Chop",40,2))
atk_lib.append(Attack("Outrage",120,2))
atk_lib.append(Attack("Dragon Breath",60,2,True))
atk_lib.append(Attack("Draco Meteor",130,2,True))
atk_lib.append(Attack("Aqua Jet",40,3))
atk_lib.append(Attack("Hydro Tail",90,3))
atk_lib.append(Attack("Water Gun",40,3,True))
atk_lib.append(Attack("Hydro Pump",110,3,True))
atk_lib.append(Attack("Nuzzle",20,4))
atk_lib.append(Attack("Volt Tackle",120,4))
atk_lib.append(Attack("Thunder Shock",40,4,True))
atk_lib.append(Attack("Thunderbolt",90,4,True))
atk_lib.append(Attack("Flame Charge",50,5))
atk_lib.append(Attack("Sacred Fire",100,5))
atk_lib.append(Attack("Ember",40,5,True))
atk_lib.append(Attack("Flamethrower",90,5,True))
atk_lib.append(Attack("Spirit Break",75,6))
atk_lib.append(Attack("Play Rough",90,6))
atk_lib.append(Attack("Fairy Wind",40,6,True))
atk_lib.append(Attack("Moonblast",95,6,True))
atk_lib.append(Attack("Ice Shard",40,7))
atk_lib.append(Attack("Ice Hammer",100,7))
atk_lib.append(Attack("Powder Snow",40,7,True))
atk_lib.append(Attack("Ice Beam",90,7,True))
atk_lib.append(Attack("Fury Cutter",40,8))
atk_lib.append(Attack("X-Scissor",80,8))
atk_lib.append(Attack("Struggle Bug",50,8,True))
atk_lib.append(Attack("Bug Buzz",90,8,True))
atk_lib.append(Attack("Pound",40,9))
atk_lib.append(Attack("Giga Impact",150,9))
atk_lib.append(Attack("Echoed Voice",40,9,True))
atk_lib.append(Attack("Ultra Beam",150,9,True))
atk_lib.append(Attack("Vine Whip",45,10))
atk_lib.append(Attack("Power Whip",120,10))
atk_lib.append(Attack("Mega Drain",40,10,True))
atk_lib.append(Attack("Energy Ball",90,10,True))
atk_lib.append(Attack("Poison Fang",50,11))
atk_lib.append(Attack("Poison Jab",80,11))
atk_lib.append(Attack("Acid",40,11,True))
atk_lib.append(Attack("Sludge Bomb",90,11,True))
atk_lib.append(Attack("Heart Stamp",60,12))
atk_lib.append(Attack("Zen Headbutt",80,12))
atk_lib.append(Attack("Confusion",50,12,True))
atk_lib.append(Attack("Psychic",90,12,True))
atk_lib.append(Attack("Rock Throw",50,13))
atk_lib.append(Attack("Stone Edge",100,13))
atk_lib.append(Attack("Ancient Power",60,13,True))
atk_lib.append(Attack("Power Gem",80,13,True))
atk_lib.append(Attack("Stomping Tantrum",60,14))
atk_lib.append(Attack("Earthquake",100,14))
atk_lib.append(Attack("Mud-Slap",20,14,True))
atk_lib.append(Attack("Earth Power",90,14,True))
atk_lib.append(Attack("Astonish",30,15))
atk_lib.append(Attack("Phantom Force",90,15))
atk_lib.append(Attack("Ominous Wind",60,15,True))
atk_lib.append(Attack("Shadow Ball",80,15,True))
atk_lib.append(Attack("Payback",50,16))
atk_lib.append(Attack("Foul Play",95,16))
atk_lib.append(Attack("Snarl",55,16,True))
atk_lib.append(Attack("Night Daze",85,16,True))
atk_lib.append(Attack("Acrobatics",55,17))
atk_lib.append(Attack("Fly",90,17))
atk_lib.append(Attack("Gust",40,17,True))
atk_lib.append(Attack("Aero Blast",100,17,True))
atk_lib.append(Attack("Splash",0,9))

if __name__ == "__name__":
    charge = Attack("charge",40)
    feuille = Attack("feuille",40,typ = 10)
    feu = Attack("feu", 40, typ = 5)
    eau = Attack("eau",40, typ = 3)
    bulbi = Individu(liste_pokemon[0],[charge,feuille])
    sala  = Individu(liste_pokemon[3],[charge,feu])
    cara  = Individu(liste_pokemon[6],[charge,eau])