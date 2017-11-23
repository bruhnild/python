
from tkinter import *
from tkinter import colorchooser
from tkinter import *
import tkinter as tk
import tkinter.ttk
from tkinter import ttk

class Root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.menu = Menu(self)
        self.menu.add_command(label="Open Toplevel", command=self.create_toplevel)
        self.config(menu=self.menu)

    def create_toplevel(self):
        self.new_toplevel = TopLevelWithButton(self)

class TopLevelWithButton(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.button = ttk.Button(self, text="Color Chooser", command=self.open_chooser)
        self.button.grid(row=0, column=0)

    def open_chooser(self):
        colorchooser.askcolor()

root = Root()
root.mainloop()
