import tkinter

window = tkinter.Tk()
window.title("KM to Mile Converter :)")
window.config(padx=90, pady=20)

def button_click():
    km = float(input_km.get())
    miles = km / 1.609344
    result_miles.config(text=f"{miles}")


tkinter_label = tkinter.Label(text="A Tkinter KM to Mile Converter :)", font=("Verdana", 8, "bold"))
tkinter_enter = tkinter.Label(text="Please, enter digits below:")
tkinter_so = tkinter.Label(text="So, ", pady=20)
input_km = tkinter.Entry(width=10)
tkinter_kms = tkinter.Label(text="Kms", pady=20)
tkinter_equal = tkinter.Label(text="=")
result_miles = tkinter.Label(text="0", font=("Verdana", 8, "bold"))
tkinter_miles = tkinter.Label(text="Miles")
calculate_button = tkinter.Button(text="Calculate", command=button_click)

tkinter_label.grid(column=1)
tkinter_enter.grid(column=1, row=1)
tkinter_so.grid(column=0, row=2)
input_km.grid(column=1, row=2)
tkinter_kms.grid(column=2, row=2)
tkinter_equal.grid(column=0, row=3)
result_miles.grid(column=1, row=3)
tkinter_miles.grid(column=2, row=3)
calculate_button.grid(column=1, row=4, pady=20)

window.mainloop()
