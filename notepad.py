from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Notepad')
root.geometry('900x600+100+100')

menu = Menu(root)

file = Menu(menu)
menu.add_cascade(label='File',menu=file)
file.add_cascade(label='New File')
file.add_cascade(label='Save')
file.add_separator()
file.add_cascade(label='Exit')

menu.add_cascade(label='File',menu=file)

ent = Entry(root, justify='left')

ent.pack(fill='both', expand=1)
root.config(menu=menu)
root.mainloop()
