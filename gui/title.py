import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="rapports_color.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """Ce GUI permet la génération de rapport semi-automatisée
par le choix d'un statut d'opportunité.
Le script python sera alors appelé 
et il faudra rentrer le mot de passe windows de l'utilisateur."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
