# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_entre.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(0, 0, 1071, 697))
        self.fond.setText("")
        self.fond.setPixmap(QtGui.QPixmap("images/divers/map.jpg"))
        self.fond.setScaledContents(True)
        self.fond.setObjectName("fond")
        self.gros_sacha = QtWidgets.QLabel(self.centralwidget)
        self.gros_sacha.setGeometry(QtCore.QRect(230, 420, 131, 171))
        self.gros_sacha.setText("")
        self.gros_sacha.setPixmap(QtGui.QPixmap("images/divers/sacha.png"))
        self.gros_sacha.setScaledContents(True)
        self.gros_sacha.setObjectName("gros_sacha")
        self.inventory = QtWidgets.QPushButton(self.centralwidget)
        self.inventory.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.inventory.setObjectName("inventory")
        self.coeur3 = QtWidgets.QLabel(self.centralwidget)
        self.coeur3.setGeometry(QtCore.QRect(980, 10, 61, 61))
        self.coeur3.setText("")
        self.coeur3.setPixmap(QtGui.QPixmap("images/divers/coeur.png"))
        self.coeur3.setScaledContents(True)
        self.coeur3.setObjectName("coeur3")
        self.coeur2 = QtWidgets.QLabel(self.centralwidget)
        self.coeur2.setGeometry(QtCore.QRect(920, 10, 61, 61))
        self.coeur2.setText("")
        self.coeur2.setPixmap(QtGui.QPixmap("images/divers/coeur.png"))
        self.coeur2.setScaledContents(True)
        self.coeur2.setObjectName("coeur2")
        self.coeur1 = QtWidgets.QLabel(self.centralwidget)
        self.coeur1.setGeometry(QtCore.QRect(860, 10, 61, 61))
        self.coeur1.setText("")
        self.coeur1.setPixmap(QtGui.QPixmap("images/divers/coeur.png"))
        self.coeur1.setScaledContents(True)
        self.coeur1.setObjectName("coeur1")
        # self.joueur = QtWidgets.QLineEdit(self.centralwidget)
        # self.joueur.setGeometry(QtCore.QRect(10, 10, 113, 22))
        # self.joueur.setObjectName("joueur")
        self.pokemon_sauvage = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_sauvage.setGeometry(QtCore.QRect(60, 360, 111, 81))
        self.pokemon_sauvage.setText("")
        self.pokemon_sauvage.setPixmap(QtGui.QPixmap("images/divers/pikachu.png"))
        self.pokemon_sauvage.setScaledContents(True)
        self.pokemon_sauvage.setObjectName("pokemon_sauvage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 90, 571, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/divers/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(390, 380, 111, 41))
        self.play.raise_()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.play.setAutoFillBackground(True)
        self.play.setObjectName("play")
        self.inventory2 = QtWidgets.QPushButton(self.centralwidget)
        self.inventory2.setGeometry(QtCore.QRect(560, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        self.inventory2.setFont(font)
        self.inventory2.setAutoFillBackground(True)
        self.inventory2.setObjectName("inventory2")

        self.sacha = QtWidgets.QLabel(self.centralwidget)
        self.sacha.setGeometry(QtCore.QRect(390, 580, 19, 25))
        self.sacha.setText("")
        self.sacha.setPixmap(QtGui.QPixmap("images/animation/down0.png"))
        self.sacha.setScaledContents(True)
        self.sacha.setObjectName("sacha")
        self.maison = QtWidgets.QLabel(self.centralwidget)
        self.maison.setGeometry(QtCore.QRect(370, 520, 41, 41))
        
        self.maison.setText("")
        self.maison.setObjectName("maison")
        
        
        
        
        #pour les combats
        self.fondcombat = QtWidgets.QLabel(self.centralwidget)
        self.fondcombat.setGeometry(QtCore.QRect(0, 0, 1071, 721))
        self.fondcombat.setText("")
        self.fondcombat.setPixmap(QtGui.QPixmap("images/divers/fond combat.PNG"))
        self.fondcombat.setScaledContents(True)
        self.fondcombat.setObjectName("fondcombat")
        self.nompoke = QtWidgets.QLabel(self.centralwidget)
        self.nompoke.setGeometry(QtCore.QRect(140, 90, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.nompoke.setFont(font)
        self.nompoke.setStyleSheet("background-color:rgb(16,164,164);\n""border: 2px solid yellow")
        self.nompoke.setAlignment(QtCore.Qt.AlignCenter)
        self.nompoke.setObjectName("nompoke")
        self.nompokesauvage = QtWidgets.QLabel(self.centralwidget)
        self.nompokesauvage.setGeometry(QtCore.QRect(660, 90, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.nompokesauvage.setFont(font)
        self.nompokesauvage.setStyleSheet("background-color:rgb(16,164,164);\n""border: 2px solid yellow")
        self.nompokesauvage.setAlignment(QtCore.Qt.AlignCenter)
        self.nompokesauvage.setObjectName("nompokesauvage")
        self.vs = QtWidgets.QLabel(self.centralwidget)
        self.vs.setGeometry(QtCore.QRect(510, 10, 631, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.vs.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(50)
        self.vs.setFont(font)
        self.vs.setTextFormat(QtCore.Qt.MarkdownText)
        self.vs.setObjectName("vs")
        self.progressBar_notre = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_notre.setGeometry(QtCore.QRect(260, 210, 118, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(20)
        self.progressBar_notre.setFont(font)
        self.progressBar_notre.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: red;\n""    width: 20px;\n""}")
        self.progressBar_notre.setMaximum(250)
        self.progressBar_notre.setProperty("value", 100)
        self.progressBar_notre.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_notre.setObjectName("progressBar_notre")
        self.progressBarpokesauvage = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarpokesauvage.setGeometry(QtCore.QRect(750, 220, 118, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(20)
        self.progressBarpokesauvage.setFont(font)
        self.progressBarpokesauvage.setStyleSheet("QProgressBar {\n""    border: 2px solid grey;\n""    border-radius: 5px;\n""    background-color: lightgrey;\n""}\n""\n""QProgressBar::chunk {\n""    background-color: green;\n""    width: 20px;\n""}")
        self.progressBarpokesauvage.setMaximum(252)
        self.progressBarpokesauvage.setProperty("value", 100)
        self.progressBarpokesauvage.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarpokesauvage.setTextVisible(True)
        self.progressBarpokesauvage.setObjectName("progressBarpokesauvage")
        self.impagepoke = QtWidgets.QLabel(self.centralwidget)
        self.impagepoke.setGeometry(QtCore.QRect(160, 320, 331, 211))
        self.impagepoke.setText("")
        self.impagepoke.setPixmap(QtGui.QPixmap("pikachu.png"))
        self.impagepoke.setScaledContents(True)
        self.impagepoke.setObjectName("impagepoke")
        self.imagepokesauvage = QtWidgets.QLabel(self.centralwidget)
        self.imagepokesauvage.setGeometry(QtCore.QRect(640, 320, 331, 211))
        self.imagepokesauvage.setText("")
        self.imagepokesauvage.setPixmap(QtGui.QPixmap("pikachu.png"))
        self.imagepokesauvage.setScaledContents(True)
        self.imagepokesauvage.setObjectName("imagepokesauvage")
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 510, 361, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.attaque4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.attaque4.setObjectName("attaque4")
        self.gridLayout.addWidget(self.attaque4, 1, 1, 1, 1)
        self.attaque3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.attaque3.setObjectName("attaque3")
        self.gridLayout.addWidget(self.attaque3, 1, 0, 1, 1)
        self.attaque2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.attaque2.setObjectName("attaque2")
        self.gridLayout.addWidget(self.attaque2, 0, 1, 1, 1)
        self.attaque1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.attaque1.setObjectName("attaque1")
        self.gridLayout.addWidget(self.attaque1, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 520, 160, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseattack = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chooseattack.setObjectName("chooseattack")
        self.verticalLayout.addWidget(self.chooseattack)
        self.escape = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.escape.setObjectName("escape")
        self.verticalLayout.addWidget(self.escape)
        self.changepokemon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changepokemon.setObjectName("changepokemon")
        self.verticalLayout.addWidget(self.changepokemon)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(400, 280, 361, 161))
        self.widget.setObjectName("widget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 40, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonBox.setFont(font)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.areyousure = QtWidgets.QLabel(self.widget)
        self.areyousure.setGeometry(QtCore.QRect(110, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.areyousure.setFont(font)
        self.areyousure.setObjectName("areyousure")
        
        
        
        #interface inventaire

        self.inventairemarron = QtWidgets.QLabel(self.centralwidget)
        self.inventairemarron.setGeometry(QtCore.QRect(210, 90, 641, 521))
        self.inventairemarron.setText("")
        self.inventairemarron.setPixmap(QtGui.QPixmap("inventory.png"))
        self.inventairemarron.setScaledContents(True)
        self.inventairemarron.setObjectName("inventairemarron")
        self.fontgris = QtWidgets.QLabel(self.centralwidget)
        self.fontgris.setGeometry(QtCore.QRect(10, 0, 1021, 721))
        self.fontgris.setMaximumSize(QtCore.QSize(1021, 16777215))
        self.fontgris.setText("")
        self.fontgris.setPixmap(QtGui.QPixmap("map_assombrie.png"))
        self.fontgris.setScaledContents(True)
        self.fontgris.setObjectName("fontgris")
        self.image4 = QtWidgets.QLabel(self.centralwidget)
        self.image4.setGeometry(QtCore.QRect(280, 420, 101, 91))
        self.image4.setText("")
        self.image4.setObjectName("image4")
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_1.setGeometry(QtCore.QRect(230, 240, 231, 171))
        self.widget_1.setObjectName("widget_1")
        self.image1 = QtWidgets.QLabel(self.widget_1)
        self.image1.setGeometry(QtCore.QRect(40, 40, 121, 91))
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap("images/divers/pikachu.png"))
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")
        self.nom1 = QtWidgets.QLabel(self.widget_1)
        self.nom1.setGeometry(QtCore.QRect(30, 140, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom1.setFont(font)
        self.nom1.setAlignment(QtCore.Qt.AlignCenter)
        self.nom1.setObjectName("nom1")
        self.pv1 = QtWidgets.QLabel(self.widget_1)
        self.pv1.setGeometry(QtCore.QRect(130, 20, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pv1.setPalette(palette)
        self.pv1.setObjectName("pv1")
        self.bp1 = QtWidgets.QPushButton(self.widget_1)
        self.bp1.setGeometry(QtCore.QRect(42, 27, 141, 121))
        self.bp1.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp1.setText("")
        self.bp1.setObjectName("bp1")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(460, 260, 171, 151))
        self.widget_2.setObjectName("widget_2")
        self.pv2 = QtWidgets.QLabel(self.widget_2)
        self.pv2.setGeometry(QtCore.QRect(110, 0, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pv2.setPalette(palette)
        self.pv2.setObjectName("pv2")
        self.image2 = QtWidgets.QLabel(self.widget_2)
        self.image2.setGeometry(QtCore.QRect(20, 20, 121, 91))
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap("animation/pikachu.png"))
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")
        self.nom2 = QtWidgets.QLabel(self.widget_2)
        self.nom2.setGeometry(QtCore.QRect(10, 120, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom2.setFont(font)
        self.nom2.setAlignment(QtCore.Qt.AlignCenter)
        self.nom2.setObjectName("nom2")
        self.bp2 = QtWidgets.QPushButton(self.widget_2)
        self.bp2.setGeometry(QtCore.QRect(20, 10, 141, 121))
        self.bp2.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp2.setText("")
        self.bp2.setObjectName("bp2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(660, 270, 151, 131))
        self.widget_3.setObjectName("widget_3")
        self.image3 = QtWidgets.QLabel(self.widget_3)
        self.image3.setGeometry(QtCore.QRect(10, 10, 121, 91))
        self.image3.setText("")
        self.image3.setPixmap(QtGui.QPixmap("animation/pikachu.png"))
        self.image3.setScaledContents(True)
        self.image3.setObjectName("image3")
        self.nom3 = QtWidgets.QLabel(self.widget_3)
        self.nom3.setGeometry(QtCore.QRect(0, 110, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom3.setFont(font)
        self.nom3.setAlignment(QtCore.Qt.AlignCenter)
        self.nom3.setObjectName("nom3")
        self.pv3 = QtWidgets.QLabel(self.widget_3)
        self.pv3.setGeometry(QtCore.QRect(110, -10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pv3.setPalette(palette)
        self.pv3.setObjectName("pv3")
        self.bp3 = QtWidgets.QPushButton(self.widget_3)
        self.bp3.setGeometry(QtCore.QRect(10, 0, 141, 121))
        self.bp3.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp3.setText("")
        self.bp3.setObjectName("bp3")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(270, 430, 141, 131))
        self.widget_4.setObjectName("widget_4")
        self.nom4 = QtWidgets.QLabel(self.widget_4)
        self.nom4.setGeometry(QtCore.QRect(-10, 110, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom4.setFont(font)
        self.nom4.setAlignment(QtCore.Qt.AlignCenter)
        self.nom4.setObjectName("nom4")
        self.image4_2 = QtWidgets.QLabel(self.widget_4)
        self.image4_2.setGeometry(QtCore.QRect(10, 10, 121, 91))
        self.image4_2.setText("")
        self.image4_2.setPixmap(QtGui.QPixmap("animation/pikachu.png"))
        self.image4_2.setScaledContents(True)
        self.image4_2.setObjectName("image4_2")
        self.pv4 = QtWidgets.QLabel(self.widget_4)
        self.pv4.setGeometry(QtCore.QRect(100, -10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pv4.setPalette(palette)
        self.pv4.setObjectName("pv4")
        self.bp4 = QtWidgets.QPushButton(self.widget_4)
        self.bp4.setGeometry(QtCore.QRect(0, 0, 141, 121))
        self.bp4.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp4.setText("")
        self.bp4.setObjectName("bp4")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(480, 430, 141, 131))
        self.widget_5.setObjectName("widget_5")
        self.nom5 = QtWidgets.QLabel(self.widget_5)
        self.nom5.setGeometry(QtCore.QRect(-10, 110, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom5.setFont(font)
        self.nom5.setAlignment(QtCore.Qt.AlignCenter)
        self.nom5.setObjectName("nom5")
        self.image5 = QtWidgets.QLabel(self.widget_5)
        self.image5.setGeometry(QtCore.QRect(0, 10, 121, 91))
        self.image5.setText("")
        self.image5.setPixmap(QtGui.QPixmap("animation/pikachu.png"))
        self.image5.setScaledContents(True)
        self.image5.setObjectName("image5")
        self.lpv5 = QtWidgets.QLabel(self.widget_5)
        self.lpv5.setGeometry(QtCore.QRect(90, -10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lpv5.setPalette(palette)
        self.lpv5.setObjectName("lpv5")
        self.bp5 = QtWidgets.QPushButton(self.widget_5)
        self.bp5.setGeometry(QtCore.QRect(0, 0, 141, 121))
        self.bp5.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp5.setText("")
        self.bp5.setObjectName("bp5")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(670, 430, 151, 131))
        self.widget_6.setObjectName("widget_6")
        self.nom6 = QtWidgets.QLabel(self.widget_6)
        self.nom6.setGeometry(QtCore.QRect(-10, 110, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nom6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nom6.setFont(font)
        self.nom6.setAlignment(QtCore.Qt.AlignCenter)
        self.nom6.setObjectName("nom6")
        self.image6 = QtWidgets.QLabel(self.widget_6)
        self.image6.setGeometry(QtCore.QRect(10, 10, 121, 91))
        self.image6.setText("")
        self.image6.setPixmap(QtGui.QPixmap("animation/pikachu.png"))
        self.image6.setScaledContents(True)
        self.image6.setObjectName("image6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(100, -10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        self.label_6.setObjectName("label_6")
        self.bp6 = QtWidgets.QPushButton(self.widget_6)
        self.bp6.setGeometry(QtCore.QRect(20, 10, 141, 121))
        self.bp6.setStyleSheet("background-color: rgb(255,255,255,0)")
        self.bp6.setText("")
        self.bp6.setObjectName("bp6")
        self.pushButton_inv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inv.setGeometry(QtCore.QRect(480, 640, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_inv.setFont(font)
        self.pushButton_inv.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(700, 180, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayoutWidget_inv = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_inv.setGeometry(QtCore.QRect(370, 200, 160, 80))
        self.verticalLayoutWidget_inv.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_inv)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_inv)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_inv)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.fontgris.raise_()
        self.inventairemarron.raise_()
        self.image4.raise_()
        self.widget_1.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.widget_6.raise_()
        self.pushButton_inv.raise_()
        self.comboBox.raise_()
        self.verticalLayoutWidget.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pokemon"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))
      #  self.joueur.setText(_translate("MainWindow", "Nom Joueur"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.inventory2.setText(_translate("MainWindow", "Inventory"))
        self.nompoke.setText(_translate("MainWindow", "TextLabel"))
        self.nompokesauvage.setText(_translate("MainWindow", "TextLabel"))
        self.vs.setText(_translate("MainWindow", "VS"))
        self.progressBar_notre.setFormat(_translate("MainWindow", "%v PV"))
        self.progressBarpokesauvage.setFormat(_translate("MainWindow", "%v PV"))
        self.attaque4.setText(_translate("Dialog", "attack4"))
        self.attaque3.setText(_translate("Dialog", "attack3"))
        self.attaque2.setText(_translate("Dialog", "attack2"))
        self.attaque1.setText(_translate("Dialog", "attack1"))
        self.chooseattack.setText(_translate("Dialog", "choose attack"))
        self.escape.setText(_translate("Dialog", "change pokemon"))
        self.changepokemon.setText(_translate("Dialog", "escape"))
        self.areyousure.setText(_translate("Dialog", "Are you sure?"))
        self.nom1.setText(_translate("MainWindow", "Pikachu"))
        self.pv1.setText(_translate("MainWindow", "24/62"))
        self.pv2.setText(_translate("MainWindow", ""))
        self.nom2.setText(_translate("MainWindow", ""))
        self.nom3.setText(_translate("MainWindow", ""))
        self.pv3.setText(_translate("MainWindow", ""))
        self.nom4.setText(_translate("MainWindow", ""))
        self.pv4.setText(_translate("MainWindow", ""))
        self.nom5.setText(_translate("MainWindow", ""))
        self.lpv5.setText(_translate("MainWindow", ""))
        self.nom6.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))
        self.pushButton_inv.setText(_translate("MainWindow", "retour"))
        self.comboBox.setItemText(0, _translate("MainWindow", "my pokemons"))
        self.comboBox.setItemText(1, _translate("MainWindow", "carapuce"))
        self.pushButton_2.setText(_translate("MainWindow", "main pokemon"))
        self.pushButton_3.setText(_translate("MainWindow", "remove"))
        

        
        
