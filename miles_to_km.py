from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

my_input = Entry(width=7)
my_input.grid(row=0, column=5)

label_1 = Label(text="Miles", font=("Arial", 12, "normal"))
label_1.config(padx=10, pady=0)
label_1.grid(row=0, column=6)

label_2 = Label(text="is equal to", font=("Arial", 12, "normal"))
label_2.grid(row=1, column=1)

label_3 = Label(text="0", font=("Arial", 12, "normal"))
label_3.grid(row=1, column=5)

label_4 = Label(text="Km", font=("Arial", 12, "normal"))
label_4.grid(row=1, column=6)


def calculate():
    km = float(my_input.get()) * 1.609
    label_3.config(text=km)


button = Button(text="calculate", command=calculate)
button.grid(row=2, column=5)

window.mainloop()
