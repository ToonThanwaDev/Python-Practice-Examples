import sys
from tkinter import Tk, simpledialog, messagebox

def rectangle(width, height):
    result = width * height
    return result

root = Tk()
root.withdraw()

while True:
    query_width= simpledialog.askinteger('Area Calculator', 'Enter width: ')
    query_height = simpledialog.askinteger('Area Calculator', 'Enter height: ')
    Area = rectangle(query_width, query_height)
    if messagebox.askokcancel('Answer', 'result is: ' + str(Area)) == False:
        root.destroy()
        sys.exit()