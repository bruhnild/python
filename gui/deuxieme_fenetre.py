from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Choisir dans la liste des opportunit�s � l'�tude", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 40)
C2 = Checkbutton(top, text = "Rechercher une opportunit� � la main", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 40)
C1.pack()
C2.pack()
top.mainloop()

