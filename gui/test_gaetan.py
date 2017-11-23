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

def do_go():
    top=Toplevel(root)
    ListButton.pack(fill=BOTH, expand=YES)
IconButton = Button()
image = ImageTk.PhotoImage(file="C:/github_repo/github_repo_python/gui/rapports_color.png")
IconButton.config(image=image)
IconButton.image = image
IconButton.pack(fill=BOTH, expand=YES)
helv36 = font.Font(family='verdana', size=10, weight=font.BOLD)
ListButton = Button(text="Choisir dans la liste des opportunités à l\'étude",font=helv36, height=3 ).pack(side=TOP, anchor=W, fill=X, expand=YES)

root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Générateur de rapports - GUI")
root.mainloop()


