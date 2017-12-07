from tkinter import *
import tkinter as tk
import tkinter.ttk
from tkinter import ttk
import os
import re
import psycopg2
import sys
import pprint
from subprocess import Popen
from PIL import ImageTk
from tkinter import font
from config import config

root = ""

def ListeChoix():
    
    
    # Connect to the PostgreSQL database server """
    conn = None
    # Read connection parameters
    params = config()
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params) 
    # Create a cursor
    cursor = conn.cursor()

    # Executer la requete pour obtenir la liste des statuts
    cursor.execute("SELECT  statut FROM coordination.opportunite group by statut")
    # Récupérer les résultats depuis la bdd
    records_statut = cursor.fetchall()
    # Enlever les accolades
    records_statut=[x for xs in records_statut for x in xs]

    # Executer la requete pour obtenir la liste des opportunités
    # Cursor.execute("SELECT  id_opp FROM coordination.opportunite group by id_opp")
    # Récupérer les résultats depuis la bdd
    # Records_id_opp = cursor.fetchall()
    # Enelever les accolades
    # Records_id_opp=[x for xs in records_id_opp for x in xs]

    def updateSQLView(event):
        # Executer la requete pour copier les csv depuis le serveur postgres de metis
        val = CategoryCombo.get()
        cursor.execute(
                """
            SELECT ROW_NUMBER() OVER(ORDER BY id_opp) id, * 
            FROM(
            SELECT 
               a.id_opp,
               a.nom,
               a.com_dep,
               a.emprise,
               a.travaux,
               e.prev_starr,
               a.cables,
               a.typ_cable,
               a.prog_dsp,
               CASE WHEN a.debut_trvx IS NULL THEN 'Inconnue'::character varying ELSE a.debut_trvx END AS debut_trvx,
               a.moa,
               d.nb_suf,
               f.longueur_max as longueur,
               CASE WHEN b.nb_chb_exists IS NULL THEN 0 ELSE b.nb_chb_exists END AS  nb_chb_exists,
               CASE WHEN g.nb_chb_a_creer IS NULL THEN 0 ELSE g.nb_chb_a_creer END AS  nb_chb_a_creer,
               CASE WHEN g.nb_chb_desserte IS NULL THEN 0 ELSE g.nb_chb_desserte END AS  nb_chb_desserte,
               CASE WHEN g.nb_chb_transport IS NULL THEN 0 ELSE g.nb_chb_transport END AS  nb_chb_transport,
               CASE WHEN g.nb_chb_indef IS NULL THEN 0 ELSE g.nb_chb_indef END AS  nb_chb_indef
            FROM coordination.opportunite a
            LEFT JOIN rip1.vue_chambres_adn b ON a.id_opp like b.id_opp
            LEFT JOIN administratif.vue_nb_suf_opp d ON a.id_opp like d.id_opp
            LEFT JOIN coordination.vue_rapport_prev_starr e ON a.id_opp like e.id_opp
            LEFT JOIN coordination.vue_rapport_longueur f ON a.id_opp like f.id_opp
            LEFT JOIN coordination.vue_nb_chb_a_creer g ON a.id_opp like g.id_opp
            where statut like '""" +val+
            """' GROUP BY 
            a.id_opp,a.nom, a.com_dep,a.emprise, a.travaux,e.prev_starr, a.cables, 
            a.typ_cable, a.prog_dsp, a.debut_trvx, a.moa, d.nb_suf, b.nb_chb_exists, 
            f.longueur_max, g.nb_chb_a_creer, g.nb_chb_desserte,g.nb_chb_transport, g.nb_chb_indef
            order by id_opp DESC
            )vue;
                """
                """
            SELECT 

                row_number() over () AS id,
                a.id_opp, 
                prev_starr,
                lg_prev_st,
                gc_typ_mut,
                sum(CASE WHEN a.gc_typ_mut IS null THEN null ELSE longueur END) as lg_typ_mut,
                gc_typ_int,
                sum(CASE WHEN a.gc_typ_int IS null THEN null ELSE longueur END) as lg_typ_int,
                sum(longueur) as longueur,
                a.com_dep
            FROM coordination.opportunite as a
            LEFT JOIN  rip1.vue_chambres_adn as b on a.id_opp=b.id_opp 
            LEFT JOIN  administratif.vue_nb_suf_opp as d on a.id_opp=d.id_opp
            where statut like '""" +val+
             """'GROUP BY
            a.id_opp, com_dep, prev_starr,lg_prev_st, gc_typ_mut, gc_typ_int
            ORDER BY id_opp
            ;
                """
        )
        
        p = Popen("script.bat", cwd=os.getcwd())
        stdout, stderr = p.communicate()
   


    def getUpdateData(event):
        cursor.execute("SELECT  id_opp FROM coordination.opportunite where statut LIKE '"+CategoryCombo.get()+"' group by id_opp")
        res=cursor.fetchall()
        res = [x for xs in res for x in xs]        
        AccountCombo['values'] = res        
        
        
    top=Toplevel(root) # créer la fenêtre (instancier)
    # Creation labels pour les combobox
    message = "Selectionner un statut"  #définir le texte de l'étiquette
    lab=Label(top, text=message).grid(row = 2,column = 1,padx = 1, pady=0) # définir l'étiquette
    message = "Selectionner une opportunité\n (A venir)"  #définir le texte de l'étiquette
    labo=Label(top, text=message).grid(row = 4,column = 1,padx = 1, pady=0) # définir l'étiquette
    # Creation des combobox
    AccountCombo = tkinter.ttk.Combobox( top, width = 15)
    sqlData = ListeChoix    
    CategoryCombo = tkinter.ttk.Combobox(top,  values = records_statut)


    # Ajouter les combobox
    CategoryCombo.bind('<<ComboboxSelected>>', updateSQLView)
    # AccountCombo.bind('<<ComboboxSelected>>', updateSQLView)
    CategoryCombo.grid(row = 3,column = 1,padx = 10,pady = 25)
    AccountCombo.grid(row = 5,column = 1,pady = 25,padx = 10)
    
    
root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Générateur de rapports - GUI")


class Application():
    def __init__(root, master):

    # Logo button in frame (right)
        ListButton.pack(fill=BOTH, expand=YES)


    # Text in frame (left)
    explanation = """Ce GUI permet la génération de rapports
    semi-automatisés par le choix
    d'un statut d'opportunité.

    L'application lancera les requêtes
    sur TOUTES les opportunités
    concernées par le statut choisi.

    Pour finir, l'utilisateur devra rentrer
    son mot de passe windows afin de
    lancer le lancement des opérations.

    A vous de jouer!"""
    colorfonttext = font.Font(family='verdana', size=8, weight=font.BOLD, slant=font.ITALIC)
    LabelExpl = Label(root, justify=CENTER, padx = 4, text=explanation,  fg = "red4", font=colorfonttext).pack(side="left")
                 
    # Logo Button in frame (left)
    IconButton = Button(command=ListeChoix)
    image = ImageTk.PhotoImage(file="logo.png")
    IconButton.config(image=image)
    IconButton.image = image
    IconButton.pack(fill=BOTH, expand=YES)
    
    # Button list in frame (down)
    colorfont = font.Font(family='verdana', size=10, weight=font.BOLD)
    ListButton = Button(text="Choisir dans la liste des opportunités à l\'étude", command=ListeChoix,font=colorfont, height=3).pack(side=TOP, anchor=W, fill=X, expand=YES)

        
root.mainloop()


