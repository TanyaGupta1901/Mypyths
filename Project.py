from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import random
import pyperclip

root = Tk()
root.title('tg ki app')
root.geometry('500x500+500+200')
root['background']='yellow';
exp=''

def calculator():

    root = Toplevel()
    root.title('Calculator')
    root.geometry("400x500+500+200")


    strp = StringVar()
    global exp


    f1 = Frame(root, bg='black')
    f1.pack(expand=True, fill='both')

    f2 = Frame(root)
    f2.pack(expand=True, fill='both')

    f3 = Frame(root)
    f3.pack(expand=True, fill='both')

    f4 = Frame(root)
    f4.pack(expand=True, fill='both')

    f5 = Frame(root)
    f5.pack(expand=True, fill='both')

    f6 = Frame(root)
    f6.pack(expand=True, fill='both')

    def clicked(num, strp):
        global exp
        exp = exp + num
        strp.set(exp)

    def result():
        global exp
        try:
            res = str(eval(exp))
            exp = res
            strp.set(exp)
        except:
            exp = 'ERROR'
            strp.set(exp)

    def ce():
        global exp
        l = list(exp)
        l.pop()
        exp = ''.join(l)
        strp.set(exp)

    def call():
        global exp
        exp = ''
        strp.set(exp)

    entry = Entry(f1, bg='grey', fg='white', justify='right', font=('courier', 30, 'bold'), textvariable=strp,
                  borderwidth='6px').pack(expand=True, side=LEFT, fill='both', padx=3, pady=3)

    bt1 = Button(f2, text='%', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('%', strp)).pack(expand=True, side=LEFT, fill='both')
    bt2 = Button(f2, text='CE', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: ce()).pack(expand=True, side=LEFT, fill='both')
    bt3 = Button(f2, text='C', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: call()).pack(expand=True, side=LEFT, fill='both')
    bt4 = Button(f2, text='/', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('/', strp)).pack(expand=True, side=LEFT, fill='both')

    bt5 = Button(f3, text='7', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("7", strp)).pack(expand=True, side=LEFT, fill='both')
    bt6 = Button(f3, text='8', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("8", strp)).pack(expand=True, side=LEFT, fill='both')
    bt7 = Button(f3, text='9', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("9", strp)).pack(expand=True, side=LEFT, fill='both')
    bt8 = Button(f3, text='x', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('*', strp)).pack(expand=True, side=LEFT, fill='both')

    bt5 = Button(f4, text='4', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("4", strp)).pack(expand=True, side=LEFT, fill='both')
    bt6 = Button(f4, text='5', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("5", strp)).pack(expand=True, side=LEFT, fill='both')
    bt7 = Button(f4, text='6', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("6", strp)).pack(expand=True, side=LEFT, fill='both')
    bt8 = Button(f4, text='-', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('-', strp)).pack(expand=True, side=LEFT, fill='both')

    bt5 = Button(f5, text='1', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("1", strp)).pack(expand=True, side=LEFT, fill='both')
    bt6 = Button(f5, text='2', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("2", strp)).pack(expand=True, side=LEFT, fill='both')
    bt7 = Button(f5, text='3', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='cyan',
                 command=lambda: clicked("3", strp)).pack(expand=True, side=LEFT, fill='both')
    bt8 = Button(f5, text='+', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('+', strp)).pack(expand=True, side=LEFT, fill='both')

    bt5 = Button(f6, text='+/-', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('-', strp)).pack(expand=True, side=LEFT, fill='both')
    bt6 = Button(f6, text='0', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('0', strp)).pack(expand=True, side=LEFT, fill='both')
    bt7 = Button(f6, text='.', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: clicked('.', strp)).pack(expand=True, side=LEFT, fill='both')
    bt8 = Button(f6, text='=', relief=GROOVE, border=0, font=('courier', 20, 'bold'), bg='black', fg='yellow',
                 command=lambda: result()).pack(expand=True, side=LEFT, fill='both')

    root.mainloop()

def passwordgen():
    root = Toplevel()
    root.title('Password Generator')
    root.geometry('600x700+500+50')
    root['background'] = '#c72664'

    len = IntVar()
    pasd = StringVar()
    c = IntVar()

    def generate():

        try:
            l = len.get()
            if c.get() == 1:
                password = ''.join(random.choices(string.ascii_lowercase, k=l))
            elif c.get() == 2:
                password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=l))
            elif c.get() == 3:
                password = ''.join(
                    random.choices(string.ascii_lowercase + string.ascii_uppercase + string.printable, k=l))
            print(password)

            return password
        except:
            messagebox.showerror('ERROR', 'Please select an option')

    def gen():
        pas = generate()
        pasd.set(pas)

    def copyclip():
        rt = pasd.get()
        pyperclip.copy(rt)

    Label(root, fg='cyan', text='Enter the length:', font=("monotype corsiva", 30, 'bold'), bg="#c72264").pack(
        expand=True, fill='both', side=TOP)
    entry = Entry(root, textvariable=len, font=("comic sans ms", 20, 'bold'), bg='black', justify='center',
                  fg='yellow').pack(side=TOP)

    Label(root, fg='cyan', text='Enter the strength:', font=("monotype corsiva", 30, 'bold'), bg="#c72264").pack(
        expand=True, fill='both', side=TOP)
    r1 = Radiobutton(root, text='Weak', font=("comic sans ms", 15, 'bold'), bg="#c72264", fg='cyan', variable=c,
                     value=1).pack(side=TOP)
    r2 = Radiobutton(root, text='Average', font=("comic sans ms", 15, 'bold'), bg="#c72264", fg='cyan', variable=c,
                     value=2).pack(side=TOP)
    r3 = Radiobutton(root, text='Strong', font=("comic sans ms", 15, 'bold'), bg="#c72264", fg='cyan', variable=c,
                     value=3).pack(side=TOP)

    Button(root, text='Generate Password', bg='black', fg='cyan', font=("monotype corsiva", 20, 'bold'),
           command=gen).pack(pady=5)

    Label(root, fg='cyan', text='Your Password:', font=("monotype corsiva", 30, 'bold'), bg="#c72264").pack(expand=True,
                                                                                                            fill='both',
                                                                                                            side=TOP)
    output = Entry(root, textvariable=pasd, font=("comic sans ms", 20, 'bold'), justify='center', bg='black',
                   fg='yellow').pack(pady=5, side=TOP)

    Button(root, text='Copy to clipboard', bg='black', fg='cyan', font=("monotype corsiva", 20, 'bold'),
           command=copyclip).pack(pady=5, side=TOP)

    root.mainloop()


Button(root, text='Calculator', bg='cyan' ,fg='blue',font=('comic sans ms',30,'bold'),command=calculator).pack(fill=BOTH,pady=10,padx=10)
Button(root, text='Password Generator',bg='cyan' ,fg='blue', font=('comic sans ms',30,'bold'),command=passwordgen).pack(fill=BOTH,pady=10,padx=10)

root.mainloop()
