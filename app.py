from tkinter import *


root = Tk()

HEIGHT = 300
WIDTH = 400

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

mainLabel = Label(root, text='FizzBuzz Program')
clearLine = Label(root, text='')
descriptionLabel1 = Label(root, text="if Input is divisable by 3, then Fizz will be displayed")
descriptionLabel2 = Label(root, text="if Input is divisable by 5, then Buzz will be displayed")
descriptionLabel3 = Label(root, text="if Input is divisable by 3 & 5, then FizzBuzz will be displayed")
entryField = Entry(root, text='Enter number here!')
myButton = Button(root, text="Calculate!!")
answerLabel = Label(root, text='answer here')


myButton.pack()
entryField.pack()
descriptionLabel1.pack()
descriptionLabel2.pack()
descriptionLabel3.pack()
answerLabel.pack()

root.mainloop()




