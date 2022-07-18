from tkinter import *

root = Tk()
root.title('Calculate Circle Area')
root.geometry('500x500')

# Formula for finding area of circle π = 3.14
Label(text = 'Radius', font = 30).grid(row = 0, sticky = W)
radius = IntVar()
et1 = Entry(width = 30, textvariable = radius, font = 30)
et1.grid(row = 0, column = 1)

Label(text = 'Circle area', font = 30).grid(row = 1, sticky = W)
et2 = Entry(width = 30, font = 30)
et2.grid(row = 1, column = 1)

def calculate():
    et2.delete(0, END)
    r = radius.get()
    area = 3.14 *r*r
    et2.insert(0, area)

def deleteText():
    et1.delete(0, END)
    et2.delete(0, END)

btn1 = Button(text = 'Calculate', command = calculate).grid(row = 2, column = 1, sticky = W)
btn2 = Button(text = 'Clear', command = deleteText).grid(row = 2, column = 1, sticky = E)


root.mainloop()
