# hello im ericka bolta aka eriii mango and i will be implementing a gui digital clock in all pink interface.
# This version will be a 12 hour format (MT 9/29/21)
# (I'm apart of a MT virtual bootcamp so I edited my code so I can keep track of the time lol)
#author Ericka Bolta 3-30-21

from tkinter import*
from tkinter.ttk import*

from datetime import datetime
import pytz

UTC = pytz.utc

IST = pytz.timezone('America/Denver')



root = Tk()
root.title("Pink DiGi Clock: Mountain Time") #window title display


def time():
    datetime_ist = datetime.now(IST)
    string = (datetime_ist.strftime("%I:%M:%S %p")) #12hour timezoneformat
    label.config(text=string)
    label.after(1000, time)

#imported a digital front from web and installed to my pc.
label = Label(root, font=("ds-digital", 80), background= "pink", foreground= "hot pink")
greeting = Label(text="by eriii mango", foreground="hot pink") #adding my tag
label.pack(anchor="center")
greeting.pack()
time()

mainloop()

