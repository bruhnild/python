import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
def make_button():
    b = tk.Button(root)
    image = ImageTk.PhotoImage(file="C:/Users/jean-Noel-11/Desktop/temp/rapports.png")
    b.config(image=image)
    b.image = image
    b.pack()
make_button()
root.mainloop()
