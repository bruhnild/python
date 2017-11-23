from tkinter import *

root = Tk()
prompt = StringVar()
root.title("AVATAR")
label = Label(root, fg="dark green")
label.pack()

frame = Frame(root,background='red')
frame.pack()

# Function definition

# first create the canvas
canvas = Canvas(height=200,width=200)
canvas.pack()

def Image1():
    canvas.delete("all")
    image1 = PhotoImage(file = "rapports.png")
    canvas.create_image(0,0,anchor='nw',image=image1)
    canvas.image = image1

def Image2():
    canvas.delete("all")
    image1 = PhotoImage(file = "report.png")
    canvas.create_image(0,0,anchor='nw',image=image1)
    canvas.image = image1

#Invoking through button
TextWindow = Label(frame,anchor = NW, justify = LEFT, bg= 'white', fg   = 'blue', textvariable = prompt, width = 75, height=20)
TextWindow.pack(side = TOP)

conversationbutton = Button(frame, text='Start    Conversation',width=25,fg="green",command = Image1)
conversationbutton.pack(side = RIGHT)

stopbutton = Button(frame, text='Stop',width=25,fg="red",command = Image2)
stopbutton.pack(side = RIGHT)

root.mainloop()
