import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter :)")
# window.minsize(width=350, height=200)
window.config(padx=90, pady=20)

def button_click():
    miles = float(input_mile.get())
    kilometers = miles * 1.609344
    result_km.config(text=f"{kilometers}")


tkinter_label = tkinter.Label(text="A Tkinter Mile to KM Converter :)", font=("Verdana", 8, "bold"))
tkinter_enter = tkinter.Label(text="Please, enter digits below:")
tkinter_so = tkinter.Label(text="So, ", pady=20)
input_mile = tkinter.Entry(width=10)
tkinter_miles = tkinter.Label(text="Miles", pady=20)
tkinter_equal = tkinter.Label(text="=")
result_km = tkinter.Label(text="0", font=("Verdana", 8, "bold"))
tkinter_km = tkinter.Label(text="Km")
calculate_button = tkinter.Button(text="Calculate", command=button_click)

tkinter_label.grid(column=1)
tkinter_enter.grid(column=1, row=1)
tkinter_so.grid(column=0, row=2)
input_mile.grid(column=1, row=2)
tkinter_miles.grid(column=2, row=2)
tkinter_equal.grid(column=0, row=3)
result_km.grid(column=1, row=3)
tkinter_km.grid(column=2, row=3)
calculate_button.grid(column=1, row=4, pady=20)

window.mainloop()
