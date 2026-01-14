from tkinter import *
from datetime import date
window=Tk()
window.title("Test")
window.geometry("400x400")
Lb1=Label(text="Enter your name",fg="white",bg="#0072FF",height=1,width=200)
name_label=Label(text='Full name',bg="#0072FF")
name_entry=Entry()
def display():
    name=name_entry.get()
    global massage
    massage="Welcome to the application \n Todays date is"
    greet="Hello"+" name "+"\n"
    test_box.insert(END,greet)
    test_box.insert(END,massage)
    test_box.insert(END,date.today)
test_box=Text(height=3)
btn=Button(text='Begain',command=display,height=1,bg="#0034FF",fg="white")
Lb1.pack()
test_box.pack()
btn.pack()
name_entry.pack()
name_label.pack()
window.mainloop()

