# Pokémon: projet informatique

## Manuel d'utilisation 

### But du jeu

Le jeu consiste à jouer un personnage (nommé Sacha) que le joueur déplacera sur un fond de carte (map) afin de débusquer des pokémons, petits animaux dotés de pouvoirs élémentaires, dans la nature. Le but du jeu sera de combattre ces pokémons à l'aide de ceux déjà possédés par le joueur, et de les capturer en cas de victoire. 

### Comment se déroule une partie ?

Pour commencer une partie, il faut cliquer sur le bouton "Jouer" dans l'écran d'accueil. 
Il n'est pas possible de gagner une partie, le but est juste de capturer le plus de pokémons.
Il est en revanche possible de perdre, lorsque le joueur perd ses 3 coeurs (en haut à droite de l'écran), c'est "Game over", le jeu est perdu. Pour perdre un coeur, il faut que tous les pokémons de l'inventaire aient 0 PV (points de vie).

### Comment se déplacer sur la map ?

Le joueur peut déplacer son personnage sur la map à l'aide des touches du clavier gauche, haut, droite, et bas. Il peut aussi se déplacer grâce aux touches Z (haut), Q (gauche), S (bas), D (droite). Il ne peut se déplacer que dans ces directions. Lorsque le joueur arrive sur les limites de la map, son personnage ne pourra plus avancer dans cette direction malgré la pression effectuée sur la touche du clavier correspondante. De même, le personnage ne peut pas se déplacer dans la forêt, remonter une cascade, et ne peut grimper sur les buttes sans passer par les escaliers. Il peut en revanche descendre des cascades et des buttes partout. 

### Comment rencontrer des pokémons sur la map ? 

Les pokémons apparaissent de manière aléatoire sur la map. Pour en débusquer, il suffit de se promener en déplaçant son personnage, et il finira par se cogner à un pokémon sauvage !

### Comment activer un combat avec des pokémons sauvages ? 

Il suffit de rencontrer un pokémon sur la map avec son personnage. Dans les hautes herbes, il n'est pas possible de reprérer un pokémon avant d'en recontrer un, ce qui engendre automatiquement un combat. Autrement, le pokémon est visible (à partir d'une distance de 26 pixels avec le personnage), et il faut alors marcher jusqu'au pokémon visible jusqu'à ce que le joueur touche le pokémon pour lancer un combat.

### Quels sont les pokémons possédés au début du jeu ?

Le joueur commence le jeu avec 3 pokémons : un Bulbizar (Bulbasaur, de type plante et poison), un Salamèche (Charmander, type feu), un Carapuce (Squirtle, type eau).

### Comment accéder à son inventaire de pokémons ?

Il faut cliquer sur le bouton "Inventaire" en haut à gauche de l'écran, ou presser la touche "i" sur son clavier, ou alors aller jusqu'à la maison de Sacha avec son personnage et presser la touche "Entrée". Cette dernière option permet de voir tous les pokémons possédés en déroulant le menu en haut à droite.  

### Comment choisir les pokémons joués lors des combats ? 

Les pokémons joués lors des combats sont tirés de l'inventaire du joueur. En cliquant sur le bouton "Inventaire" en haut à gauche de l'écran, le joueur peut voir l'inventaire de ses pokémons. En se déplaçant sur la maison de Sacha et en pressant la touche "Entrée", le joueur peut voir à la fois son inventaire normal, et tous les pokémons qu'il possède à force de captures dans un menu déroulant. Il peut alors choisir d'enlever un pokémon de son inventaire en cliquant sur le pokémon en question et en cliquant ensuite sur "remove". Il peut choisir de rajouter un pokémon à son inventaire normal en cliquant sur le menu déroulant, et en cliquant sur le pokémon voulu - à condition qu'il reste une place de libre dans l'inventaire du joueur (jusqu'à 6 pokémons possédés). Cette fonctionnalité n'existe pas hors de la maison de Sacha !

### Comment choisir le pokémon joué en premier lors des combats ?

Il suffit d'accéder à l'inventaire du joueur, de cliquer sur le pokémon que le joueur veut comme pokémon principal, et de cliquer ensuite sur le bouton "main". Le pokémon principal, donc celui envoyé en premier lors des combats, sera doté d'une couronne dorée sur sa case d'inventaire. Il est possible de changer le pokémon principal à tout moment - sauf pendant les combats. Les pokémons n'ayant plus de points de vie (PV) ne peuvent pas être sélectionnés comme pokémon principal. Si le pokémon principal précédemment sélectionné n'a plus de PV, le pokémon suivant dans l'inventaire (en ligne) deviendra le nouveau pokémon principal automatiquement. 

### Comment se déroule un combat ?

Un combat pokémon est un duel entre un pokémon sauvage et un pokémon possédé par le joueur. Le joueur aura alors le choix, à chaque tour jusqu'à la fin du combat, de choisir une attaque, changer de pokémon, ou fuir le combat. 
* Attaquer : Chaque pokémon possède une attaque minimum et jusqu'à 4 attaques. Les starters - pokémons possédés au début du jeu - possèdent tous 2 attaques. Chaque attaque possède un type élémentaire. Chaque pokémon possède lui aussi un type élémentaire, et peut donc être doté d'attaques de type "neutre", ou alors correspondant au type du dit pokémon.
* Changer de pokémon : Cliquer sur cette option renvoie à l'inventaire du joueur. Il suffit de cliquer sur le pokémon voulu pour l'envoyer se battre à la place du pokémon sorti. Il est impossible d'envoyer un personnage sans PV (points de vie) au combat.
* Fuir : l'option de fuir sera toujours proposée mais la fuite ne sera pas toujours possible. L'action de ce tour sera alors gâchée, et le pokémon restera au combat.
Une attaque encaissée fera baisser les points de vie (PV) des pokémons. Lorsque le pokémon n'a plus de PV (PV = 0, barre de vie vide), il est KO. Le pokémon sauvage KO est automatiquement capturé par le joueur et placé dans son inventaire. Si le pokémon possédé par le joueur est KO, le joueur a le choix de fuir. La fuite sera alors automatique, et ne pourra pas être empêchée. Autrement, il peut choisir de continuer le combat, et le pokémon suivant dans l'inventaire sera envoyé au combat.
Si tous les pokémons sont KO (n'ont plus de PV), le joueur a perdu. Il perd alors un coeur, et retourne devant la maison de Sacha, tous ses pokémons soignés.

### Les types

Les types élémentaires sont très importants dans le jeu. En effet, chaque pokémon possède un ou plusieurs types qui le rendent capables de jouer des attaques spéciales d'un type élémentaires, mais en contrepartie les rendent faibles contre des types particuliers. 
Liste des types : acier, combat, dragon, eau, électrik, feu, fée, glace, insecte, normal, plante, poison, psy, roche, sol, spectre, ténèbres et vol.
Par exemple, le feu est faible contre l'eau, mais fort contre le type plante.
Le tableau des faiblesses et avantages entre les types est disponible facilement sur internet. 

### Comment soigner ses pokémons ? 

Après un combat, les pokémons possédés par le joueur auront pris des dégâts. Il faudra alors déplacer le personnage jusqu'à la maison de Sacha, placée en centre de la map, et de presser la touche "Entrée" afin de soigner les pokémons automatiquement. Cette action ouvrira aussi automatiquement l'inventaire du personnage, où il sera possible de changer le personnage principal du joueur - qui apparaîtra en premier dans un combat - et les joueurs possédés emportés par le joueur dans son inventaire. Un pokémon sera automatiquement soigné au maximum s'il évolue.

### Niveau et évolution des pokémons

Chaque pokémon a un niveau différent, selon son expérience. Les pokémons de départ sont de niveau 1. Les pokémons sauvages rencontrés peuvent être de niveaux variables. Lorsqu'un pokémon atteind un certain niveau, il évolue. Le niveau du pokémon influence les statistiques des pokémon (attaque, défense, attaque spéciale et défense spéciale), les PV maximum, et le calcul des dégâts infligés. Le niveau maximal est le niveau 100.

### Architecture du code

La programmation du jeu est organisé en 3 dossiers : 
* data : ce dossier contient toutes les images (sous-dossier "images"), les coordonnées de toutes les collisions sur la carte selon la direction du joueur, et les fichiers csv fournis.
  Les images sont elles-mêmes divisées en sous-dossier (rouge, blanc, et inversées pour chaque).
* documents : ce dossier contient les documents fournis. Il n'a pas été modifié.
* src : ce dossier contient tous les fichiers pythons nécessaires au jeu.

Le dossier src contient les fichiers pythons suivants : 
* pokemon.py : classes des Pokémon/Individu/Attacks/Teams et Zone/Sous-Zone utilisées ensuite par tous les autres fichiers,
* initialisation.py : détermine le starting pack avec lequel le joueur commence, les coordonnées des pokémons placés sur la carte, et les zones dans lesquelles les pokémons apparaissent aléatoirement,
* fight.py : gère les combats entre les pokémons,
* moving.py : gère les déplacements du joueurs sur la carte,
* gui.py : statique, gère toute l'interface graphique,
* inventory.py : gère les inventaires du joueur,
* main_window.py : importe tous les fichiers précédents, permet de lancer le jeu.





