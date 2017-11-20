# -*- coding: utf-8 -*-
 
import sys
import os
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
import psycopg2

import sys
 
class Main(object):
    def __init__(self):
        # Ici tu implémentes le nécéssaire de ton appli
        self.ui = MainUI(self)
        self.ui.show()
 
        db = self.get_db()
        if not db:
            # Y a un blème afficher erreur et quitter 
            # ou ouvrir un dialogue pour chercher la db
            pass
 
        dat = self.set_data()
        if dat is not None:
            # pareil, afficher l'erreur (contenue dans dat) et puis ...
            print (dat)
 
    def get_db(self):
        if not os.path.isfile('blabla/postgis_21_sample'):
            return False
        return True
 
    def set_data(self):
        # Je n'utilise pas psycopg2 donc je suppose que tu es sure de ta mèthode
        try:
            conn = psycopg2.connect("dbname='postgis_23_sample' user='postgres' \
                                    host='localhost' password='postgres'")
        except Exception as why:
            return why
 
        curs = conn.cursor()
        self.listeSIRD= curs.execute("SELECT srtext FROM spatial_ref_sys;")
        self.listeSIRD= curs.fetchall()
 
        for row in self.listeSIRD :
            self.ui.combo.addItem(str(row))
 
 
class MainUI(QtWidgets.QMainWindow):
    def __init__(self, main):
        super(MainUI, self).__init__()
        # on garde une ref de l'appli
        self.main = main
        self.widget = QtGui.QWidget(self)
        gridLayout = QtGui.QGridLayout(self.widget)
        vLayot = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel('Label', self)
        vLayout.addWidget(self.label)
        self.label_1 = QtGui.QLabel('Label 1', self)
        vLayout.addWidget(self.label_1)
        self.comboBox = QtGui.QComboBox(self)
        vLayout.addWidget(self.comboBox)
        gridLayout.addLayout(vLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.widget)
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
