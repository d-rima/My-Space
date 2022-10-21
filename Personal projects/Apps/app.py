import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []

# Everything that you put in your GUI will be attache dto the root
# root = tk.TK() paired with root.mainloop() will create a small white GUI 
root = tk.Tk()

# This function makes it so that when run, it will open your files, and show only the executables
def add_app():
    # This allows me to destroy anything that I put onto the frame, prior to adding to the list of apps, so as to avoid repeating files
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    # This makes it so that I can add the label of the various files to the frame
    for app in apps:
        label = tk.Label(frame, text=app, bg = "gray", )
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)

# This allows me to alter the size, and the color of my GUI
canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
#Unless you 'pack' the canvas, the changes you make will not be implemented
canvas.pack()

# tk.Frame allows you to put a frame around your GUI, you can alter its color here
frame = tk.Frame(root, bg="white")
# 'place' is needed for the frame to appear, and also gives the change to alter the height, width, and how much on either side it is visible 
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

# tk.Button allows you to make a button, as well as define its size, text color, and background color.
open_file = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg = "white", bg = "blue", command = add_app)
# You have to pack whatever it is that you are putting in
open_file.pack()

run_apps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "white", bg = "blue", command = run_apps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# This saves the apps in a file, so that you don't have to add them every time
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')