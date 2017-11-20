 
 
import os
import re
import shutil
import tkinter
 
def mots_pour_complements():
    """Liste des mots susceptibles d'être complétés"""
 
    liste_mots=['convivial','Déterminer','déterminer','si et seulement si','ensemble','solution','condition','nécessaire',
                'suffisante','condiment','par contre','contretemps','seulement','Seulement','Par contre','Par ailleurs',
                'Résoudre','résoudre','événement','alpha','beta']
    liste_mots=list(set(liste_mots))
    return liste_mots
 
def recherche_complement(saisie,liste_mots):
    """La variable saisie correspond au début du mot à compléter éventuellement;
 
       liste_mots est la liste de l'ensemble de tous les mots susceptibles d'être complétés
 
       En retour: liste_complement qui est la liste triée dans l'ordre croissant des mots trouvés
       dans liste_mots qui commencent par la variable affectée à saisie"""
 
    liste_complement=[]
    for mots in liste_mots:
        if mots.startswith(saisie):
            liste_complement.append(mots)
    numero_index=1
    while numero_index<len(liste_complement):
        numero_test=numero_index-1
        while liste_complement[numero_test]>liste_complement[numero_index] and numero_test>=0:
            numero_test=numero_test-1
        if numero_test<numero_index-1:
            tampon=liste_complement[numero_index]
            j=numero_index
            while j>numero_test+1:
                liste_complement[j]=liste_complement[j-1]
                j=j-1
            liste_complement[numero_test+1]=tampon    
        numero_index=numero_index+1
    return liste_complement
 
def selection(inutile):
    """Si l'utilisateur tape <'Down'> on positionne le focus sur la liste des mots"""    
    liste.focus_set()
 
def separation():
    """Fonction qui permet de récupérer le dernier <<mot>> qui est entrain d'être saisi"""
 
    phrase=zone_saisie.get()
    decoupage=phrase.split(' ')
    mot=decoupage[-1]
    decoupage=mot.split('\\')
    mot=decoupage[-1]
    return phrase,mot
 
def recuperation(inutile):
    """Fonction qui permet l'affichage dans la liste des propositions de complément"""
 
    [phrase,mot]=separation()
    liste_mots=mots_pour_complements()
    liste_complement=recherche_complement(mot,liste_mots)
    liste.delete(0,tkinter.END)
    if phrase[-1:]!=r' ':
        for mot_select in liste_complement:
            liste.insert(tkinter.END,mot_select)
        liste.selection_set(0,0)
 
def affiche(inutile):
    """Fonction qui complète après sélection le mot en cours de frappe"""
 
    [phrase,mot]=separation()
    phrase_sans_mot=phrase[:-len(mot)]
    zone_saisie.delete(0,tkinter.END)
    zone_saisie.insert(tkinter.END,phrase_sans_mot+liste.get(liste.curselection()))
    zone_saisie.focus_set()
    liste.delete(0,tkinter.END)
 
 
 
#Début du corps du programme    
 
#Création de la fenêtre principale nommée racine
racine=tkinter.Tk()
racine.title("Principale")
 
#Création de <<bouton>> de type Button pour fermer l'application
bouton=tkinter.Button(racine,text='Quitter',command=racine.destroy)
bouton.pack(side=tkinter.BOTTOM)
 
#Création de <<zone_saisie>> de type Entry où est tapé le texte
texte_saisi=tkinter.StringVar()
 
zone_saisie=tkinter.Entry(racine,textvariable=texte_saisi,width=80)
zone_saisie.pack()
zone_saisie.focus_set()
 
#Création de <<cadre>> de type Frame pour regrouper la liste avec un ascenseur
cadre=tkinter.Frame(racine)
cadre.pack()
 
#Création de <<ascenseur>> de type Scrollbar et de <<liste>> de type Listbox
#pour afficher la proposition des mots pour le complément
ascenseur=tkinter.Scrollbar(cadre,orient=tkinter.VERTICAL)
ascenseur.pack(side=tkinter.RIGHT,fill=tkinter.Y)
liste=tkinter.Listbox(cadre,yscrollcommand=ascenseur.set)
ascenseur.config(command=liste.yview)
liste.pack(fill=tkinter.Y)
 
#Exécution évenementiels en fonction des touches tapées sur le clavier
#La touche Return affiche le résultat
#La touche Down permet de sélectionner la liste
liste.bind('<Return>',affiche)
 
zone_saisie.bind('a',recuperation)
zone_saisie.bind('b',recuperation)
zone_saisie.bind('c',recuperation)
zone_saisie.bind('d',recuperation)
zone_saisie.bind('e',recuperation)
zone_saisie.bind('f',recuperation)
zone_saisie.bind('g',recuperation)
zone_saisie.bind('h',recuperation)
zone_saisie.bind('i',recuperation)
zone_saisie.bind('j',recuperation)
zone_saisie.bind('k',recuperation)
zone_saisie.bind('l',recuperation)
zone_saisie.bind('m',recuperation)
zone_saisie.bind('n',recuperation)
zone_saisie.bind('o',recuperation)
zone_saisie.bind('p',recuperation)
zone_saisie.bind('q',recuperation)
zone_saisie.bind('r',recuperation)
zone_saisie.bind('s',recuperation)
zone_saisie.bind('t',recuperation)
zone_saisie.bind('u',recuperation)
zone_saisie.bind('v',recuperation)
zone_saisie.bind('w',recuperation)
zone_saisie.bind('x',recuperation)
zone_saisie.bind('y',recuperation)
zone_saisie.bind('z',recuperation)
zone_saisie.bind('é',recuperation)
zone_saisie.bind('è',recuperation)
zone_saisie.bind('A',recuperation)
zone_saisie.bind('B',recuperation)
zone_saisie.bind('C',recuperation)
zone_saisie.bind('D',recuperation)
zone_saisie.bind('E',recuperation)
zone_saisie.bind('F',recuperation)
zone_saisie.bind('G',recuperation)
zone_saisie.bind('H',recuperation)
zone_saisie.bind('I',recuperation)
zone_saisie.bind('J',recuperation)
zone_saisie.bind('K',recuperation)
zone_saisie.bind('L',recuperation)
zone_saisie.bind('M',recuperation)
zone_saisie.bind('N',recuperation)
zone_saisie.bind('O',recuperation)
zone_saisie.bind('P',recuperation)
zone_saisie.bind('Q',recuperation)
zone_saisie.bind('R',recuperation)
zone_saisie.bind('S',recuperation)
zone_saisie.bind('T',recuperation)
zone_saisie.bind('U',recuperation)
zone_saisie.bind('V',recuperation)
zone_saisie.bind('W',recuperation)
zone_saisie.bind('X',recuperation)
zone_saisie.bind('Y',recuperation)
zone_saisie.bind('Z',recuperation)
zone_saisie.bind('<Down>',selection)
zone_saisie.bind('<Return>',affiche)
 
#Affichage du tout
racine.mainloop()
