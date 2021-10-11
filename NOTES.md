# Notes on this Project

Notes I took while creating the code and learning about Tkinter. In code format.

```python
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)       # --- sets minimum window size --- #

# --- 1) CREATING COMPONENTS --- #
# Labels (component)
my_label = tkinter.Label(text="Hi", font=("Arial", 18, "bold"))
# Labels: update content (use .config)
my_label.config(text="Not Hi but Hello")

# Buttons (component)
def button_click():
    input_content = input.get()
    my_label.config(text=input_content)


button = tkinter.Button(text="Click Me", command=button_click)      # command is a click event listener
new_button = tkinter.Button(text="New Button")

# Entry (component)
input = tkinter.Entry()


# --- 2) POSITIONING IN WINDOW --- #
# --- How components are to be laid out on the window --- #
# --- Three Systems: Pack(), Place() and Grid() --- #
# PS: one of these has to exist in order to appear at the window.

# Add "padding"
# .config(padx=value, pady=value2)

# PACK System
# my_label.pack()         # --> pack alone means center of program
# pack("left"), pack("bottom"), etc... other options
# pack (expand=True)      # --> tries to take the entire height and width available of the screen size
# button.pack()
# input.pack()

# GRID System (we adopted this one)
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
input.grid(column=3, row=2)

window.mainloop()          # --> end of project

# More on...
# PACK(), PLACE(), GRID()
# what do they do?

# PACK -> It packs each widget next to one another in vaguely logic format. By default, it starts from top and
# goes all the way down to the bottom of the screen, mid-center. One below the other. You can change this by
# adding pack(side="left")... if you do it for every widget, then it will start at the left and go all the way
# to the right side of the screen. Problem is: difficult to specify precise positions.

# PLACE -> All about precise positioning: you can specify X/Y axis values. Example: place(x=0, y=0), then it will
# place the widget at the top left portion of the screen. Problem is: too specific... if we've got a bunch of
# widgets, we gotta manage where to place each one exactly. Bit of a nightmare there.

# GRID -> It imagines your screen is purely made of a grid which you can define the number of columns and rows.
# For example: .grid(column=0, row=0). The grid system is based in relative positioning: this means that, even if
# you write .grid(column=5, row=5), it will still show your component in the top left corner of the screen because
# there is no other component there. So, the best way to work with grid is to put your first component in
# .grid(column=0, row=0) and then, the other components relative to this one.

# Caution: if you start with the place method, go all the way. If you do it with grid, go all the way.
# Don't mix them together, otherwise there's an Error in your code.
```