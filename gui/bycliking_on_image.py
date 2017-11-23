from tkinter import *
import tkinter.ttk
from tkinter import ttk
import tkinter as tk
import os
import re
import psycopg2
import sys
import pprint
from subprocess import Popen
from PIL import ImageTk, Image    


def showImage():
        lbl1.configure(image=image_tk)
        btn.configure(text = "load image!", command=showImage1)

def showImage1(): 
        lbl1.configure(image=image_tk2)
        btn.configure(text = "load image!", command=showImage)
        

def showImage2(): 
        lbl1.configure(image=image_tk2)
        btn.configure(text = "load image!", command=showImage)


root = Tk()    
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

fname = "rapports.png"
image_tk = ImageTk.PhotoImage(Image.open(fname))

fname1 = "report.png"
image_tk1 = ImageTk.PhotoImage(Image.open(fname1))  # new image object

fname2 = "rapport_symbol.jpg"
image_tk2 = ImageTk.PhotoImage(Image.open(fname2))  # new image object


btn = ttk.Button(c, text="load image", command=showImage)
lbl1 = ttk.Label(c)
btn.grid(column=0, row=0, sticky=N, pady=5, padx=5)
lbl1.grid(column=1, row=1, sticky=N, pady=5, padx=5)

root.mainloop()
