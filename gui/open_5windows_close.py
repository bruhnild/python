from tkinter import *

root = Tk()

def ouvre():
    for i in range(5):
        tpl = Toplevel(root)
        Label(tpl,text="je suis la fenetre %s" %i).pack()

def ferme():
    for widget in root.winfo_children():
        if isinstance(widget,Toplevel):
            widget.destroy()

Label(root,text="J'ouvre et je ferme des fenetres !").pack()
Button(root,text="Ouvrir 5 fenetres",command=ouvre).pack()
Button(root,text="Fermer tout !",command=ferme).pack()

root.mainloop()
