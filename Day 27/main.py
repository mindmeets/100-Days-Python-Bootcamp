import tkinter

window = tkinter.Tk()
window.title("My First GUI Application")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack(side="left")


window.mainloop()