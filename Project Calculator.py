from tkinter import *

root = Tk()
root.title('Calculator')

content = ''
txt_input = StringVar(value = '0')

def btn(number):
    global content
    content += str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ''

def clear():
    global content
    content = ''
    txt_input.set('')
    display.insert(0, '0')

# แสดงผล (row = 5, column = 4)
display = Entry(font = ('arial', 20, 'bold'), fg = 'white', bg = 'black', textvariable = txt_input, justify = 'right')
display.grid(columnspan = 4)

# รับค่าผ่านปุ่ม
# Row1
btnac = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = 'C', command = clear, padx = 30, pady = 15).grid(row = 1, column = 0)
btnopen = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '(', command = lambda:btn('('), padx = 33, pady = 15).grid(row = 1, column = 1)
btnclose = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = ')', command = lambda:btn(')'), padx = 33, pady = 15).grid(row = 1, column = 2)
btndivide = Button(fg = 'white', bg = 'orange', font = ('arial', 20, 'bold'), text = '/', command = lambda:btn('/'), padx = 33, pady = 15).grid(row = 1, column = 3)

# Row2
btn7 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '7', command = lambda:btn(7), padx = 33, pady = 15).grid(row = 2, column = 0)
btn8 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '8', command = lambda:btn(8), padx = 30, pady = 15).grid(row = 2, column = 1)
btn9 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '9', command = lambda:btn(9), padx = 30, pady = 15).grid(row = 2, column = 2)
btnby= Button(fg = 'white', bg = 'orange', font = ('arial', 20, 'bold'), text = 'x', command = lambda:btn('*'), padx = 30, pady = 15).grid(row = 2, column = 3)

# Row3
btn4 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '4', command = lambda:btn(4), padx = 33, pady = 15).grid(row = 3, column = 0)
btn5 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '5', command = lambda:btn(5), padx = 30, pady = 15).grid(row = 3, column = 1)
btn6 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '6', command = lambda:btn(6), padx = 30, pady = 15).grid(row = 3, column = 2)
btnminus = Button(fg = 'white', bg = 'orange', font = ('arial', 20, 'bold'), text = '-', command = lambda:btn('-'), padx = 33, pady = 15).grid(row = 3, column = 3)

# Row4
btn1 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '1', command = lambda:btn(1), padx = 33, pady = 15).grid(row = 4, column = 0)
btn2 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '2', command = lambda:btn(2), padx = 30, pady = 15).grid(row = 4, column = 1)
btn3 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '3', command = lambda:btn(3), padx = 30, pady = 15).grid(row = 4, column = 2)
btnplus = Button(fg = 'white', bg = 'orange', font = ('arial', 20, 'bold'), text = '+', command = lambda:btn('+'), padx = 30, pady = 15).grid(row = 4, column = 3)

# Row5
btn0 = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '0', command = lambda:btn(0), padx = 83, pady = 15).grid(row = 5, column = 0, columnspan = 2)
btndot = Button(fg = 'white', bg = 'gray', font = ('arial', 20, 'bold'), text = '.', command = lambda:btn('.'), padx = 33, pady = 15).grid(row = 5, column = 2)
btnequal = Button(fg = 'white', bg = 'orange', font = ('arial', 20, 'bold'), text = '=', command = equal, padx = 30, pady = 15).grid(row = 5, column = 3)



root.mainloop()