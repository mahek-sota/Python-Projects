import time
from tkinter import *

root = Tk()
root.geometry('359x150+0+0')

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(1)

def start():
    text = time.strftime("%H:%M:%S")
    Label.config(text=text)
    Label.after(200,start)

Label = Label(root, font=("ds-digital", 50, "bold"), bg='black', fg='red',bd=50)
Label.grid(row=0,column=1)
start()
print('Done')
root.mainloop()

