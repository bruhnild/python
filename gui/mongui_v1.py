#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
import tkinter.ttk
from tkinter import ttk 

# Fait appraitre la deuxieme fenetre
def ListeChoix():
    category = {'A présenter': ['utilities','rent','cable'],
        'A étudier': ['gas','oil','repairs'],
        'Abandonné':['parks','maintenance','payment']}
    
    def getUpdateData(event):
        AccountCombo['values'] = category[CategoryCombo.get()]
        
    top=Toplevel(root) # créer la fenêtre (instancier)
    # Creation labels pour les combobox
    message = "Selectionner un statut"  #définir le texte de l'étiquette
    lab=Label(top, text=message).grid(row = 2,column = 1,padx = 2, pady=0) # définir l'étiquette
    message = "Selectionner une opportunité"  #définir le texte de l'étiquette
    labo=Label(top, text=message).grid(row = 4,column = 1,padx = 2, pady=0) # définir l'étiquette
    # Creation des combobox
    AccountCombo = tkinter.ttk.Combobox( top, width = 15)
    CategoryCombo = tkinter.ttk.Combobox(top,  values = list(category.keys()))
    # Ajouter les combobox
    CategoryCombo.bind('<<ComboboxSelected>>', getUpdateData)
    CategoryCombo.grid(row = 3,column = 1,padx = 10,pady = 25)
    AccountCombo.grid(row = 5,column = 1,pady = 25,padx = 10)

    
   
def RentrerValeur():
    category = {'A présenter': ['utilities','rent','cable'],
        'A étudier': ['gas','oil','repairs'],
        'Abandonné':['parks','maintenance','payment']}
    
    def getUpdateData(event):
        AccountCombo['values'] = category[CategoryCombo.get()]
        
    top=Toplevel(root) # créer la fenêtre (instancier)
    # Creation labels pour les combobox
    message = "Selectionner un statut"  #définir le texte de l'étiquette
    lab=Label(top, text=message).grid(row = 2,column = 1,padx = 2, pady=0) # définir l'étiquette
    # Creation des combobox
    CategoryCombo = tkinter.ttk.Combobox(top,  values = list(category.keys()))
    # Ajouter les combobox
    CategoryCombo.bind('<<ComboboxSelected>>', getUpdateData)
    CategoryCombo.grid(row = 3,column = 1,padx = 10,pady = 25)



    

class App:
    def __init__(self, master):
        fm = Frame(master)
    
        Button(fm, text="Choisir dans la liste des opportunités à l\'étude",command=ListeChoix).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='Rechercher une opportunité à la main',command=RentrerValeur).pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm.pack(fill=BOTH, expand=YES)

  
        
        
root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Générateur de rapports - GUI")
display = App(root)
root.mainloop()

