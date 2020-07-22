from tkinter import *
from function import fizz_buzz


root = Tk()


def clickMe():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=clickMe, fg="blue", bg="white")
myButton.pack()

root.mainloop()




