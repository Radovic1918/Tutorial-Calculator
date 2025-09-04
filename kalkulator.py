from tkinter import *

root = Tk()
root.title("Kalkulator")

def dodaj_broj(broj):
    trenutni = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(trenutni) + str(broj))

def dodaj_ocisti():
    entry.delete(0, END)

def dodaj_plus():
    prvi_broj = entry.get()
    global p_br
    global math
    math = "sabiranje"
    p_br = int(prvi_broj)
    entry.delete(0, END)

def dodaj_minus():
    prvi_broj = entry.get()
    global p_br
    global math
    math = "oduzimanje"
    p_br = int(prvi_broj)
    entry.delete(0, END)

def dodaj_mnozi():
    prvi_broj = entry.get()
    global p_br
    global math
    math = "mnozenje"
    p_br = int(prvi_broj)
    entry.delete(0, END)


def dodaj_dijeli():
    prvi_broj = entry.get()
    global p_br
    global math
    math = "dijeljenje"
    p_br = int(prvi_broj)
    entry.delete(0, END)


def dodaj_jednako():
    drugi_broj = entry.get()
    entry.delete(0, END)
    if math == "sabiranje":
        entry.insert(0, p_br + int(drugi_broj))
    elif math == "oduzimanje":
        entry.insert(0, p_br - int(drugi_broj))
    elif math == "mnozenje":
        entry.insert(0, p_br * int(drugi_broj))
    elif math == "dijeljenje":
        entry.insert(0, p_br / int(drugi_broj))


    

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, columnspan=3, padx=10, pady=10)

dugme1 = Button(root, text="1", padx=40, pady=20, command=lambda: dodaj_broj(1))
dugme1.grid(row=1, column=0)
dugme2 = Button(root, text="2", padx=40, pady=20, command=lambda: dodaj_broj(2))
dugme2.grid(row=1, column=1)
dugme3 = Button(root, text="3", padx=40, pady=20, command=lambda: dodaj_broj(3))
dugme3.grid(row=1, column=2)

dugme4 = Button(root, text="4", padx=40, pady=20, command=lambda: dodaj_broj(4))
dugme4.grid(row=2, column=0)
dugme5 = Button(root, text="5", padx=40, pady=20, command=lambda: dodaj_broj(5))
dugme5.grid(row=2, column=1)
dugme6 = Button(root, text="6", padx=40, pady=20, command=lambda: dodaj_broj(6))
dugme6.grid(row=2, column=2)

dugme7 = Button(root, text="7", padx=40, pady=20, command=lambda: dodaj_broj(7))
dugme7.grid(row=3, column=0)
dugme8 = Button(root, text="8", padx=40, pady=20, command=lambda: dodaj_broj(8))
dugme8.grid(row=3, column=1)
dugme9 = Button(root, text="9", padx=40, pady=20, command=lambda: dodaj_broj(9))
dugme9.grid(row=3, column=2)

dugme0 = Button(root, text="0", padx=40, pady=20, command=lambda: dodaj_broj(0))
dugme0.grid(row=4, column=1)


dugmeplus = Button(root, text="+", padx=39, pady=20, command = dodaj_plus)
dugmeplus.grid(row=4, column=0)

dugmeminus = Button(root, text="-", padx=40, pady=20, command = dodaj_minus)
dugmeminus.grid(row=4, column=2)

dugmemnozenje = Button(root, text="*", padx=40, pady=20, command = dodaj_mnozi)
dugmemnozenje.grid(row=5, column=0)

dugmedijeljenje = Button(root, text="/", padx=40, pady=20, command = dodaj_dijeli)
dugmedijeljenje.grid(row=6, column=0)


dugmejednako = Button(root, text="=", padx=90, pady=20, command = dodaj_jednako)
dugmejednako.grid(row=5, column=1, columnspan=2)

dugmeocisti = Button(root, text="C", padx=90, pady=20, command = dodaj_ocisti)
dugmeocisti.grid(row=6, column=1, columnspan=2)


root.mainloop()