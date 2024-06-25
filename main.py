from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    result = round(miles * 1.609344, 2)
    km_output.config(text=f"{result}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)
miles_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
