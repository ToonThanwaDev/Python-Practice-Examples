# 1 Bath = 0.0294 USD (DOLLAR)
# 1 Bath = 3.7639 JPY (YEN)
# 1 Bath = 0.027 EUR (EURO)
# 1 Bath = 0.02307 GBP (Pound)

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Currency Converter')
root.geometry('500x500')

# Input
money = IntVar()
Label(text = 'Amount (TH)', padx = 10, font = 30).grid(row = 0, sticky = W)
et1 = Entry(font = 30, width = 30, textvariable = money)
et1.grid(row = 0, column = 1)

choice = StringVar(value = 'Choose your currency')
Label(text = 'Choose currency', padx = 10, font = 30).grid(row = 1, sticky = W)
combo = ttk.Combobox(width = 30, font = 30, textvariable = choice)
combo['values'] = ('USD', 'JPY', 'EUR', 'GBP')
combo.grid(row = 1, column = 1)

# Output
Label(text = 'Result', padx = 10, font = 30).grid(row = 2, sticky = W)
et2 = Entry(font = 30, width = 30)
et2.grid(row = 2, column = 1)

def calculate():
    amount = money.get()
    currency = choice.get()

    if currency == 'USD':
        et2.delete(0, END)    
        result = ((amount * 0.0294), 'USD')
        et2.insert(0, result)
    elif currency == 'JPY':
        et2.delete(0, END)
        result = ((amount * 3.7639), 'JPY')
        et2.insert(0, result)
    elif currency == 'EUR':
        et2.delete(0, END)
        result = ((amount * 0.027), 'EUR')
        et2.insert(0, result)
    elif currency == 'GBP':
        et2.delete(0, END)
        result = ((amount * 0.02307), 'GBP')
        et2.insert(0, result)
    else:
        et2.delete(0, END)
        result = 'Not Found'
        et2.insert(0, result)

def deleteText():
    et1.delete(0, END)
    et2.delete(0, END)

Button(text = 'Calculate', font = 30, width = 15, command = calculate).grid(row = 3, column = 1, sticky = W)
Button(text = 'Clear', font = 30, width = 15, command = deleteText).grid(row = 3, column = 1, sticky = E)


root.mainloop()
