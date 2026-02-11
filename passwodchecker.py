from tkinter import *
window = Tk()
window.title("Length Converter App")
window.geometry("400x400")
def check_strength():
    password = entry.get()
    length = len(password)
    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="light green")
    else:
        result_label.config(text="Very Strong", fg="dark green")
heading = Label(window, text="Password Strength Checker", font=("Arial", 14))
heading.pack(pady=20)
label = Label(window, text="Enter Password:")
label.pack()
entry = Entry(window)
entry.pack(pady=10)
btn = Button(window, text="Check Strength", command=check_strength)
btn.pack(pady=10)
result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)
window.mainloop()