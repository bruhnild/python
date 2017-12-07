import tkinter as tk
from PIL import ImageTk


        
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

class windowclass():
    def __init__(self, master):
        self.master = master
        self.btn = tk.Button(master, text="Button", command=self.command)
        image = ImageTk.PhotoImage(file="rapports_color.png")
        self.btn.config(image=image)
        self.btn.image = image
        self.btn.pack()

    def command(self):
        print("hello")
        # Supprime la 1ere fenetre
        self.master.withdraw()
        #creation d'une nouvelle fenetre
        #toplevel = tk.Toplevel(self.master)
        toplevel = ""
        # dessine la fenetre
        #toplevel.geometry("350x350")
        # appel la classe Demo2 avec le top fenêtre en paramètre
        app = Demo2(toplevel)

root = tk.Tk()
root.title("window")
root.geometry("350x350")
cls = windowclass(root)
root.mainloop()
