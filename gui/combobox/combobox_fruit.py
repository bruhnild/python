# -*- coding:utf-8 -*-
 
from tkinter		import *	# GUI
from tkinter.ttk	import *	# Widgets avec thèmes
 
class MonProgramme(Tk):
	""" Mon programme graphique utilisant Python3 et Tkinter """
 
	def __init__(self):
		Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation                
                # Widgets
 
		# Quel fruit a été sélectionné ?
		print(self)
		self.fruitSelect	= StringVar()
		self.stockFruits	= ('Pomme', 'Poire', 'Banane')
		self.listeFruits	= Combobox(self, textvariable = self.fruitSelect, \
						values = self.stockFruits, state = 'readonly')
 
		# Placement des widgets
		self.listeFruits.grid()
 
# -------------------------
 
if(__name__ == '__main__'):
	application = MonProgramme()	# Instanciation de la classe
	application.mainloop()		# Boucle pour garder le programme en vie
	application.quit()		# Fermeture propre à la sortie de la boucle
