import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height = 300)

# Must pack in order to show label
my_label = tkinter.Label(text = "Is equal to 0 Km", font = ("Arial", 12))
my_label.place(x = 200, y =120)

miles_label = tkinter.Label(text = "Miles", font = ("Arial", 12))
miles_label.place(x = 280, y = 80)

# Button
def button_clicked():
    miles = input.get()
    if miles.isnumeric() == True:
        km = int(1.60934 * float(miles))
        my_label.config(text =f"is equal to {km} Km")


button = tkinter.Button(text = "Calculate", command = button_clicked)
button.place(x = 200, y = 160)

# entry
input = tkinter.Entry(width = 10, text = "0")
input.place(x = 200, y = 80)






window.mainloop()