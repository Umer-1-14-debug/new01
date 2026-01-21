
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Tk")
window.geometry("400x400")
def msg():
    messagebox.showwarning("Alert","Virus found in the system")
btn=Button(text="Click me",command=msg)
btn.pack()
window.mainloop()