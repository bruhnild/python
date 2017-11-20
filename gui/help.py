#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
import tkinter.ttk
from tkinter import ttk
import os
import re
import psycopg2
import sys
import pprint

def callData():
	#Define our connection string
	conn_string = "host='www.metis-reseaux.fr' dbname='l49' user='postgres' password='UhtS.1Hd2' port=5678"
	
        # print the connection string we will use to connect
	print ("Connecting to database")
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
        # get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)


def ListeChoix():
#Define our connection string
    conn_string = "host='www.metis-reseaux.fr' dbname='l49' user='postgres' password='UhtS.1Hd2' port=5678"
    # print the connection string we will use to connect
    print ("Connecting to database")

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)    
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # execute our Query (selectionner un statut)
    StatutList = ['En attente', 'Traitée', 'A présenter', 'Abandonné']

    sql = 'select * from (WITH list_statut AS (SELECT  statut FROM coordination.opportunite group by statut) SELECT   list_statut.statut AS list_statut FROM list_statut)o WHERE list_statut IN %(StatutList)s'

    cursor.execute(sql, {'StatutList': tuple(StatutList),})
    # retrieve the records from the database
    records_statut = cursor.fetchall()
    print(records_statut)

    # execute our Query (selectionner une opportunite)
    cursor.execute("WITH un_id_opp AS (SELECT  id_opp FROM coordination.opportunite where statut like 'A présenter' group by id_opp) SELECT array_agg(un_id_opp.id_opp) AS id_opp FROM un_id_opp")
    # retrieve the records from the database
    records_id_opp = cursor.fetchall()
    print(records_id_opp)


    
    def getUpdateData(event):
        print(CategoryCombo.get())
        AccountCombo['values'] = records_id_opp[CategoryCombo.get()]
        
    top=Toplevel(root) # créer la fenêtre (instancier)
    # Creation labels pour les combobox
    message = "Selectionner un statut"  #définir le texte de l'étiquette
    lab=Label(top, text=message).grid(row = 2,column = 1,padx = 2, pady=0) # définir l'étiquette
    message = "Selectionner une opportunité"  #définir le texte de l'étiquette
    labo=Label(top, text=message).grid(row = 4,column = 1,padx = 2, pady=0) # définir l'étiquette
    # Creation des combobox
    AccountCombo = tkinter.ttk.Combobox( top, width = 15)
    sqlData = callData    
    CategoryCombo = tkinter.ttk.Combobox(top,  values = records_statut)
    # Ajouter les combobox
    CategoryCombo.bind('<<ComboboxSelected>>', getUpdateData)
    CategoryCombo.grid(row = 3,column = 1,padx = 10,pady = 25)
    AccountCombo.grid(row = 5,column = 1,pady = 25,padx = 10)



    

class App:
    def __init__(self, master):
        fm = Frame(master)
    
        Button(fm, text="Choisir dans la liste des opportunités à l\'étude",command=ListeChoix).pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm.pack(fill=BOTH, expand=YES)

  
        
        
root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Générateur de rapports - GUI")
display = App(root)
root.mainloop()

