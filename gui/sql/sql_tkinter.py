
#Import Modules
from tkinter import *
import tkinter.ttk
from tkinter import ttk
import os
import re
import psycopg2
import sys
import pprint


#Database
conn_string = "host='www.metis-reseaux.fr' dbname='l49' user='postgres' password='UhtS.1Hd2' port=5678"
db = psycopg2.connect(conn_string)
cursor=db.cursor()
print("Opened Database")
cursor.execute("CREATE TABLE IF NOT EXISTS public.marks (firstname varchar(45),lastname varchar(45),mark varchar(45))")
db.commit()
print("Table created")
#Variables
Surname = str()
Firstname = str()
Mark = str()
#Define Buttons
def addentry() :
   cursor.execute("INSERT INTO marks (firstname,lastname,mark) VALUES (%s,%s,%s)",(Firstname, Surname, Mark))
   db.commit()
   print ("Entry Added To Database")

def deleteentry() :
   selected=listbox.get(ACTIVE)
   name=selected[0]
   db.execute('DELETE FROM marks where Firstname =?', (name))
   print ("Entry Deleted")
#Window
window = Tk()
window.title("marks")
window.geometry("875x500")
#Labels
lbl_surname = Label(window, text="Surname:", font="Arial 12 bold")
lbl_first = Label(window, text="First-Name:", font="Arial 12 bold")
lbl_mark = Label(window, text="Mark (Percentage):", font="Arial 12 bold")
#Entry
txt_surname = Entry(window, textvariable=Surname)
txt_first = Entry(window, textvariable=Firstname)
txt_mark = Entry(window, textvariable=Mark)
#Button
def foo(event):#function called when '<<ComboboxSelected>>' event is triggered
    print (v.get())#how to access to combobox selected item
combo_value = str()
but_save = Button(window, text="Save", command= addentry, width=10)
but_delete = Button(window, text="Delete", command=deleteentry, width=10)
box_value = StringVar()
box = ttk.Combobox(window, textvariable=box_value,values=combo_value)
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
combo_value = cursor.fetchall()
combo_value.sort()
print (combo_value)
for row in combo_value:
   box['values'] = (row)
   box.current(0)
lbl_surname.grid(row=0, column=1, padx=100)
lbl_first.grid(row=0, column=0)
lbl_mark.grid(row=0, column=2)
txt_surname.grid(row=1, column=1, padx=110)
txt_first.grid(row=1, column=0, padx=10)
txt_mark.grid(row=1, column=2)
but_save.grid(row=0, column=3)
but_delete.grid(row=1, column=3)
box.grid(row=2)
window.mainloop()

