from tkinter import *
import tkinter.ttk
from tkinter import ttk
import os
import re
import psycopg2
import sys
import pprint

root = Tk()
root.geometry('425x300')


def add_symptom():
    y = symptoms.get(ACTIVE)
    selected_symptoms.insert(END, y)


def remove_symptom():
    selected_symptoms.delete(ACTIVE)


def diagnosis_validation():
    if selected_symptoms.size() < 5:
        print('Insufficient symptoms for diagnosis')
    else:
        diagnose()


def diagnose():
    for a in selected_symptoms.get(0, END):
        print(a)

label1 = Label(root, text='Symptoms')
label1.place(x=5, y=5)

i = ['Fever', 'Headache', 'Vomiting', 'Weakness', 'Blood in urine', 'Joint pains', 'Stomachache',
 'Heavy sweating']

symptoms = Listbox(root)
symptoms.place(x=5, y=30,
           width=150, height=200)
for x in i:
    symptoms.insert(END, x)

scrollb1 = Scrollbar(root, command=symptoms.yview)
scrollb1.place(x=154, y=31, height=200)

symptoms.configure(yscrollcommand=scrollb1.set)

label2 = Label(root, text='Selected symptoms')
label2.place(x=255, y=5)

selected_symptoms = Listbox(root)
selected_symptoms.place(x=255, y=30, width=150, height=200)

scrollb2 = Scrollbar(root, command=selected_symptoms.yview)
scrollb2.place(x=404, y=31, height=200)

selected_symptoms.configure(yscrollcommand=scrollb2.set)

add_button = ttk.Button(root, text='Add',
                    command=add_symptom)
add_button.place(x=175, y=30)

remove_button = ttk.Button(root, text='Remove',
                       command=remove_symptom)
remove_button.place(x=175, y=70)

diagnose_button = ttk.Button(root, text='Diagnose',
                         command=diagnosis_validation)
diagnose_button.place(x=175, y=205)

root.mainloop()
