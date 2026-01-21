from tkinter import *
window = Tk()
window.title("Tk")
window.geometry("400x400")
def event_keypressed(Event):
    print(Event.char)
def handle_click(Event):
    print(Event.x,Event.y)
btn=Button(text="Click me")
btn.pack()
window.bind("<Key>",event_keypressed)
btn.bind("<Button-1>",handle_click)
window.mainloop()
