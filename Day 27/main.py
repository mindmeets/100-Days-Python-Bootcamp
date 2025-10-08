# import tkinter
from tkinter import *

def button_clicked():
    print("You clicked button")
    entry_text = input_box.get()
    # my_label.config(text="You clicked button")
    my_label.config(text=f"{entry_text}")

def clear_button_clicked():
    my_label.config(text="Enter your name")
    input_box.delete(0, END)

window = Tk()
window.title("My First GUI Application")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.pack(side="left")
my_label.config(text="Enter your name")
my_label.pack()
# my_label.pack()
# my_label.place(x=10, y=10)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label["text"] = "New Text"
# my_label.config(text="Another Text")

#Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
# button.place(x=280, y=70)
button.grid(column=0, row=2)

#Entry
input_box = Entry(width=10)
print(input_box.get())
# input_box.pack()
# input_box.place(x=280, y=25)
input_box.grid(column=0, row=1)

#Button
clear_btn = Button(text="Reset", command=clear_button_clicked)
# clear_btn.pack()
# clear_btn.place(x=280, y=70)
clear_btn.grid(column=3, row=2)

window.mainloop()



