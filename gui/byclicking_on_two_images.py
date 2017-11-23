import tkinter as tk

root1 = tk.Tk()

def new_window():
    root2 = tk.Toplevel()
    # click the last button and all tk windows close
    def shutdown():
        root1.destroy()
        root2.destroy()
    background_image2 = tk.PhotoImage(file = 'rapports.png')
    background_button2 = tk.Button(root2, image = background_image2, command = shutdown)
    background_button2.pack()
    root2.mainloop()

background_image1 = tk.PhotoImage(file = 'report.png')
# have used a button not a label for me to make another tk window
background_button1 = tk.Button(root1, image = background_image1, command = new_window)
background_button1.pack()

root1.mainloop()
