# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:13:24 2024

@author: Ordi
"""
import numpy  as np
import pandas as pd
import random as rd

from pokemon import Individu, Attack, Zone, Sous_Zone
from pokemon import atk_lib



liste_pokemon = pd.read_csv('../data/pokemon_first_gen.csv',sep = ',').to_numpy()




starting_pack = []
starting_pack.append(Individu(liste_pokemon[0], [atk_lib[0], atk_lib[43]],15))
starting_pack[-1].range = 0
starting_pack.append(Individu(liste_pokemon[4], [atk_lib[0], atk_lib[23]],35))
starting_pack[-1].range = 1
starting_pack.append(Individu(liste_pokemon[6], [atk_lib[0], atk_lib[15]],5))
starting_pack[-1].range = 2
# starting_pack.append(Individu(liste_pokemon[149], [atk_lib[4], atk_lib[-2], atk_lib[32]],100))
# starting_pack[-1].range = 3



wild = []
wild.append([Individu(liste_pokemon[53], [atk_lib[0]]),1656,864])
wild[-1][0].receive_xp(Individu.xp_total(25), True)
wild.append([Individu(liste_pokemon[53], [atk_lib[0]]),1656,912])
wild[-1][0].receive_xp(Individu.xp_total(25), True)
wild.append([Individu(liste_pokemon[53], [atk_lib[0]]),1656,960])
wild[-1][0].receive_xp(Individu.xp_total(25), True)
wild.append([Individu(liste_pokemon[142], [atk_lib[0]]),1872,1344])
wild[-1][0].receive_xp(Individu.xp_total(40), True)
wild.append([Individu(liste_pokemon[143], [atk_lib[0]]),2592,1416])
wild[-1][0].receive_xp(Individu.xp_total(80), True)
wild.append([Individu(liste_pokemon[144], [atk_lib[0]]),1800,456])
wild[-1][0].receive_xp(Individu.xp_total(80), True)
wild.append([Individu(liste_pokemon[145], [atk_lib[0]]),1452,528])
wild[-1][0].receive_xp(Individu.xp_total(80), True)
wild.append([Individu(liste_pokemon[149], [atk_lib[0]]),2112,384])
wild[-1][0].receive_xp(Individu.xp_total(80), True)
wild.append([Individu(liste_pokemon[150], [atk_lib[0]]),1980,1850])
wild[-1][0].receive_xp(Individu.xp_total(100), True)



zones = []
info0 = [0,0.05,2,5,[0,3,6,9,12],[0.1,0.1,0.1,0.35,0.35]]
info1 = [1,0.05,4,7,[15,18,20,28,31],[0.3,0.3,0.2,0.1,0.1]]
info2 = [2,0.05,5,8,[22,24,26,53,55],[0.25,0.1,0.25,0.2,0.2]]
info3 = [3,0.05,7,10,[34,38,40,45,73],[0.05,0.15,0.4,0.1,0.3]]
info4 = [4,0.05,9,13,[36,42,51,57,68],[0.2,0.2,0.2,0.2,0.2]]
info5 = [5,0.05,11,14,[62,65,91,95,103],[0.2,0.2,0.2,0.2,0.2]]
info6 = [6,0.05,13,16,[10,13,49,76,80],[0.1,0.1,0.3,0.2,0.3]]
info7 = [7,0.05,14,18,[1,4,7,19,132],[0.25,0.25,0.25,0.15,0.1]]
info8 = [8,0.05,17,20,[16,29,32,97,110],[0.25,0.2,0.2,0.2,0.15]]
info9 = [9,0.05,19,23,[83,87,101,107,108],[0.2,0.2,0.3,0.1,0.2]]
info10 = [10,0.05,22,25,[11,14,43,69,99],[0.05,0.05,0.3,0.3,0.3]]
info11 = [11,0.05,24,28,[23,27,94,112,113],[0.3,0.3,0.1,0.05,0.25]]
info12 = [12,0.05,25,29,[46,47,52,63,131],[0.15,0.3,0.2,0.3,0.05]]
info13 = [13,0.05,28,31,[35,41,66,74,82],[0.05,0.35,0.2,0.3,0.1]]
info14 = [14,0.05,30,33,[21,25,78,137,139],[0.2,0.2,0.2,0.2,0.2]]
info15 = [15,0.05,32,35,[54,92,122,126,136],[0.4,0.3,0.1,0.1,0.1]]
info16 = [16,0.05,34,37,[37,39,58,124,125],[0.3,0.2,0.3,0.1,0.1]]
info17 = [17,0.05,38,41,[50,56,104,121,123],[0.2,0.3,0.3,0.1,0.1]]
info18 = [18,0.05,40,43,[17,48,100,127],[0.3,0.25,0.25,0.2]]
info19 = [19,0.05,42,45,[44,70,98,102],[0.25,0.25,0.25,0.25]]
info20 = [20,0.05,43,46,[77,79,81,84],[0.25,0.25,0.25,0.25]]
info21 = [21,0.05,45,49,[88,96,109,114],[0.3,0.3,0.3,0.1]]
info22 = [22,0.05,48,51,[30,33,105,106,142],[0.35,0.35,0.1,0.1,0.1]]
info23 = [23,0.05,50,53,[111,133,134,135,141],[0.3,0.2,0.2,0.2,0.1]]
info24 = [24,0.05,52,57,[2,5,8,138,140],[0.2,0.2,0.2,0.2,0.2]]
info25 = [25,0.05,55,60,[64,67,75,93,148],[0.24,0.24,0.24,0.24,0.04]]
infoaqua0 = [26,0.05,10,15,[59,71,85,117,128],[0.2,0.2,0.1,0.2,0.3]]
infoaqua1 = [27,0.05,25,30,[60,89,115,119,146],[0.15,0.25,0.3,0.25,0.05]]
infoaqua2 = [28,0.05,35,40,[72,86,116,118,147],[0.3,0.2,0.25,0.2,0.05]]
infoaqua3 = [29,0.05,50,55,[61,90,120,129,130],[0.3,0.3,0.2,0.1,0.1]]

infos = [1056,1176,23,23]
zones.append(Sous_Zone(info0 + infos))
infos = [1080,1152,71,47]
zones.append(Sous_Zone(info0 + infos))
infos = [1104,1200,71,143]
zones.append(Sous_Zone(info0 + infos))
infos = [1176,1200,23,119]
zones.append(Sous_Zone(info0 + infos))
infos = [1200,1224,23,95]
zones.append(Sous_Zone(info0 + infos))
infos = [1224,1248,23,71]
zones.append(Sous_Zone(info0 + infos))

infos = [1704,1176,23,47]
zones.append(Sous_Zone(info1 + infos))
infos = [1728,1176,23,71]
zones.append(Sous_Zone(info1 + infos))
infos = [1752,1176,71,95]
zones.append(Sous_Zone(info1 + infos))
infos = [1800,1272,23,23]
zones.append(Sous_Zone(info1 + infos))
infos = [1800,1152,71,95]
zones.append(Sous_Zone(info1 + infos))

infos = [1056,1680,71,71]
zones.append(Sous_Zone(info2 + infos))
infos = [1104,1632,95,95]
zones.append(Sous_Zone(info2 + infos))
infos = [1200,1608,23,95]
zones.append(Sous_Zone(info2 + infos))
infos = [1224,1608,23,71]
zones.append(Sous_Zone(info2 + infos))
infos = [1248,1608,23,47]
zones.append(Sous_Zone(info2 + infos))

infos = [1488,1608,71,23]
zones.append(Sous_Zone(info3 + infos))
infos = [1440,1632,143,143]
zones.append(Sous_Zone(info3 + infos))
infos = [1416,1680,23,71]
zones.append(Sous_Zone(info3 + infos))
infos = [1488,1776,95,23]
zones.append(Sous_Zone(info3 + infos))
infos = [1584,1656,23,119]
zones.append(Sous_Zone(info3 + infos))
infos = [1608,1680,23,95]
zones.append(Sous_Zone(info3 + infos))

infos = [816,1776,47,23]
zones.append(Sous_Zone(info4 + infos))
infos = [720,1680,95,143]
zones.append(Sous_Zone(info4 + infos))
infos = [672,1680,47,119]
zones.append(Sous_Zone(info4 + infos))
infos = [624,1680,47,95]
zones.append(Sous_Zone(info4 + infos))
infos = [600,1728,23,23]
zones.append(Sous_Zone(info4 + infos))

infos = [192,1464,23,23]
zones.append(Sous_Zone(info5 + infos))
infos = [168,1488,47,71]
zones.append(Sous_Zone(info5 + infos))
infos = [192,1536,95,47]
zones.append(Sous_Zone(info5 + infos))
infos = [240,1560,95,71]
zones.append(Sous_Zone(info5 + infos))
infos = [264,1632,71,23]
zones.append(Sous_Zone(info5 + infos))

infos = [48,1296,47,95]
zones.append(Sous_Zone(info6 + infos))
infos = [96,1344,23,23]
zones.append(Sous_Zone(info6 + infos))
infos = [96,1200,47,143]
zones.append(Sous_Zone(info6 + infos))
infos = [144,1200,23,95]
zones.append(Sous_Zone(info6 + infos))

infos = [144,720,23,71]
zones.append(Sous_Zone(info7 + infos))
infos = [96,672,47,143]
zones.append(Sous_Zone(info7 + infos))
infos = [96,648,23,23]
zones.append(Sous_Zone(info7 + infos))
infos = [48,648,47,119]
zones.append(Sous_Zone(info7 + infos))
infos = [24,672,23,95]
zones.append(Sous_Zone(info7 + infos))
infos = [12,744,23,23]
zones.append(Sous_Zone(info7 + infos))
infos = [12,672,23,47]
zones.append(Sous_Zone(info7 + infos))

infos = [168,528,23,23]
zones.append(Sous_Zone(info8 + infos))
infos = [168,576,23,71]
zones.append(Sous_Zone(info8 + infos))
infos = [192,528,23,95]
zones.append(Sous_Zone(info8 + infos))
infos = [216,552,47,95]
zones.append(Sous_Zone(info8 + infos))
infos = [264,576,23,71]
zones.append(Sous_Zone(info8 + infos))
infos = [288,600,47,47]
zones.append(Sous_Zone(info8 + infos))

infos = [48,144,143,71]
zones.append(Sous_Zone(info9 + infos))
infos = [48,216,119,47]
zones.append(Sous_Zone(info9 + infos))
infos = [48,264,95,23]
zones.append(Sous_Zone(info9 + infos))
infos = [48,288,47,23]
zones.append(Sous_Zone(info9 + infos))

infos = [288,384,95,95]
zones.append(Sous_Zone(info10 + infos))
infos = [384,408,71,71]
zones.append(Sous_Zone(info10 + infos))
infos = [408,432,119,95]
zones.append(Sous_Zone(info10 + infos))
infos = [528,480,23,47]
zones.append(Sous_Zone(info10 + infos))

infos = [696,384,23,23]
zones.append(Sous_Zone(info11 + infos))
infos = [720,360,23,71]
zones.append(Sous_Zone(info11 + infos))
infos = [744,360,167,95]
zones.append(Sous_Zone(info11 + infos))
infos = [816,456,95,23]
zones.append(Sous_Zone(info11 + infos))
infos = [864,336,47,23]
zones.append(Sous_Zone(info11 + infos))

infos = [672,696,143,119]
zones.append(Sous_Zone(info12 + infos))
infos = [792,624,71,143]
zones.append(Sous_Zone(info12 + infos))
infos = [744,648,47,47]
zones.append(Sous_Zone(info12 + infos))
infos = [696,672,47,23]
zones.append(Sous_Zone(info12 + infos))

infos = [1176,792,47,119]
zones.append(Sous_Zone(info13 + infos))
infos = [1224,744,47,167]
zones.append(Sous_Zone(info13 + infos))
infos = [1272,768,23,167]
zones.append(Sous_Zone(info13 + infos))
infos = [1296,792,23,95]
zones.append(Sous_Zone(info13 + infos))

infos = [1056,720,47,47]
zones.append(Sous_Zone(info14 + infos))
infos = [1104,744,23,23]
zones.append(Sous_Zone(info14 + infos))
infos = [1008,768,143,143]
zones.append(Sous_Zone(info14 + infos))
infos = [1056,912,95,47]
zones.append(Sous_Zone(info14 + infos))

infos = [1056,240,47,119]
zones.append(Sous_Zone(info15 + infos))
infos = [1104,192,23,167]
zones.append(Sous_Zone(info15 + infos))
infos = [1128,168,23,167]
zones.append(Sous_Zone(info15 + infos))
infos = [1152,144,47,191]
zones.append(Sous_Zone(info15 + infos))
infos = [1152,144,71,-1]
zones.append(Sous_Zone(info15 + infos))
infos = [1152,144,119,143]
zones.append(Sous_Zone(info15 + infos))
infos = [1272,144,23,95]
zones.append(Sous_Zone(info15 + infos))

infos = [1584,672,23,47]
zones.append(Sous_Zone(info16 + infos))
infos = [1608,648,23,71]
zones.append(Sous_Zone(info16 + infos))
infos = [1632,624,143,95]
zones.append(Sous_Zone(info16 + infos))

infos = [2016,1440,23,23]
zones.append(Sous_Zone(info17 + infos))
infos = [2016,1464,47,23]
zones.append(Sous_Zone(info17 + infos))
infos = [1992,1488,95,95]
zones.append(Sous_Zone(info17 + infos))
infos = [2136,1608,23,23]
zones.append(Sous_Zone(info17 + infos))
infos = [2160,1512,47,119]
zones.append(Sous_Zone(info17 + infos))
infos = [2184,1464,23,47]
zones.append(Sous_Zone(info17 + infos))

infos = [2064,1320,71,23]
zones.append(Sous_Zone(info18 + infos))
infos = [2064,1248,95,71]
zones.append(Sous_Zone(info18 + infos))
infos = [2064,1176,47,71]
zones.append(Sous_Zone(info18 + infos))
infos = [2040,1152,47,47]
zones.append(Sous_Zone(info18 + infos))
infos = [2016,1176,23,23]
zones.append(Sous_Zone(info18 + infos))
infos = [2256,1296,23,47]
zones.append(Sous_Zone(info18 + infos))
infos = [2280,1272,47,71]
zones.append(Sous_Zone(info18 + infos))

infos = [2376,1392,23,119]
zones.append(Sous_Zone(info19 + infos))
infos = [2352,1416,23,119]
zones.append(Sous_Zone(info19 + infos))
infos = [2328,1440,23,143]
zones.append(Sous_Zone(info19 + infos))
infos = [2304,1584,23,23]
zones.append(Sous_Zone(info19 + infos))
infos = [2280,1608,23,23]
zones.append(Sous_Zone(info19 + infos))

infos = [2544,1344,23,23]
zones.append(Sous_Zone(info20 + infos))
infos = [2568,1224,95,119]
zones.append(Sous_Zone(info20 + infos))
infos = [2592,1200,47,23]
zones.append(Sous_Zone(info20 + infos))
infos = [2664,1224,23,95]
zones.append(Sous_Zone(info20 + infos))

infos = [2304,1680,71,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2256,1704,143,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2232,1728,167,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2208,1752,215,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2352,1776,95,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2352,1800,95,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2352,1824,119,23]
zones.append(Sous_Zone(info21 + infos))
infos = [2352,1848,47,23]
zones.append(Sous_Zone(info21 + infos))

infos = [2544,1824,95,47]
zones.append(Sous_Zone(info22 + infos))
infos = [2640,1800,23,71]
zones.append(Sous_Zone(info22 + infos))
infos = [2664,1776,23,95]
zones.append(Sous_Zone(info22 + infos))
infos = [2688,1728,23,143]
zones.append(Sous_Zone(info22 + infos))

infos = [2664,504,23,23]
zones.append(Sous_Zone(info23 + infos))
infos = [2640,528,71,215]
zones.append(Sous_Zone(info23 + infos))
infos = [2616,576,71,191]
zones.append(Sous_Zone(info23 + infos))
infos = [2592,600,23,95]
zones.append(Sous_Zone(info23 + infos))

infos = [2424,192,191,23]
zones.append(Sous_Zone(info24 + infos))
infos = [2400,216,167,23]
zones.append(Sous_Zone(info24 + infos))
infos = [2664,336,23,23]
zones.append(Sous_Zone(info24 + infos))
infos = [2688,312,23,143]
zones.append(Sous_Zone(info24 + infos))

infos = [2016,456,23,23]
zones.append(Sous_Zone(info25 + infos))
infos = [2016,480,95,23]
zones.append(Sous_Zone(info25 + infos))
infos = [2016,504,143,119]
zones.append(Sous_Zone(info25 + infos))

infos = [4,1710,181,137]
zones.append(Sous_Zone(infoaqua0 + infos))

infos = [581,150,180,185]
zones.append(Sous_Zone(infoaqua1 + infos))
infos = [762,221,95,114]
zones.append(Sous_Zone(infoaqua1 + infos))

infos = [317,1302,252,113]
zones.append(Sous_Zone(infoaqua2 + infos))
infos = [365,1416,204,23]
zones.append(Sous_Zone(infoaqua2 + infos))

infos = [2598,1086,95,41]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2574,1111,58,64]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2526,1134,58,65]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2478,1158,58,89]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2430,1182,58,161]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2422,1416,90,101]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2421,1518,235,65]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2397,1584,283,47]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2430,1632,274,23]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2454,1656,250,23]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2478,1680,226,23]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2502,1704,130,23]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2526,1728,106,23]
zones.append(Sous_Zone(infoaqua3 + infos))
infos = [2550,1752,82,23]
zones.append(Sous_Zone(infoaqua3 + infos))

