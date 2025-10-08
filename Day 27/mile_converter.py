from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{round(km, 2)}")

window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=300)
window.config(padx=50, pady=30)

#Entry
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

kilometer_result = Label(text="0")
kilometer_result.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

#Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()


