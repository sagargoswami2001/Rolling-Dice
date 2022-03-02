# Create GUI Dice Rolling Simulator Using Python.
from tkinter import *
import random
from tkinter import font

root = Tk()

root.title("Dice Simulator")

# set window size
root.geometry("600x500")

root['bg']='lightyellow'

'''
#set window color
root.configure(bg='lightyellow')
root.mainloop() 
'''

label = Label(root , font = ("Helvitica" , 400 , 'bold') , text = "Sagar Goswami" , fg = 'skyblue')

def rolldice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
    label.configure(text = f'{random.choice(dice)}')
    label.pack()

button = Button(root , font = ("Helvitica" , 25 , 'bold') , text = "Dice Roll" , command = rolldice , bg = 'lightblue' , fg = 'red')
button.pack()

root.mainloop()
