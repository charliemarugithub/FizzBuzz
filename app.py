from tkinter import *
from function import fizz_buzz


root = Tk()

myLabel = Label(root, text="FIZZBUZZ")
clearLine = Label(root, text="")
button = Button(root, text="Click Me!")

clearLine.grid(row=0, column=0)
myLabel.grid(row=1, column=0)
button.grid(row=1, column=3, padx=20)

root.mainloop()




