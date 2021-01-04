from tkinter import *

start = Tk()
start.title("Variables")
start.geometry("400x600")

some = Label(start, text="Enter the first number")
some.pack()

first_number = Entry(start, width=10)
first_number.pack()
some = Label(start, text="Enter the second number")
some.pack()

second_number = Entry(start, width=10)
second_number.pack()


def addition():
    haha = Label(start, text="Sum is" + " " + str(int(first_number.get())+int(second_number.get())))
    haha.pack()

def substraction():
        haha = Label(start, text="Difference is" + " " + str(int(first_number.get()) - int(second_number.get())))
        haha.pack()


add = Button(start, text="Addition", command=addition)
add.pack()

add = Button(start, text="Difference", command=substraction)
add.pack()

start.mainloop()
