from tkinter import *
from tkinter.ttk import *

from time import strftime
import sys

root = Tk()
root.title('Digital Clock')

def get_time():
   time =  strftime("%H:%M:%S %p")
   clock.config(text=time)
   clock.after(1000, get_time)


clock = Label(root, font=('Poppins', 90), background = 'black', foreground = 'gold')
clock.pack(anchor='center')

get_time()
root.mainloop()

