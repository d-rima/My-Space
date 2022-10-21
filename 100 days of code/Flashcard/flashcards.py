import tkinter
import random
import csv

with open('100 days of code/Flashcard/Language_Data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data.remove(["German", "English"])

# Create The window
window = tkinter.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50)

# Create the canvas
front_card = tkinter.Canvas(width = 800, height = 526)
card_front = tkinter.PhotoImage(file = "100 days of code/Flashcard/card_front.png")
front_card.create_image(400, 263, image = card_front)
front_card.create_text(400, 150, text = "German", font = ("Ariel", 40, "italic"))
front_card_text = front_card.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
front_card.grid(row=0,column=0, columnspan = 2)

back_card = tkinter.Canvas(width = 800, height = 526)
back_front = tkinter.PhotoImage(file = "100 days of code/Flashcard/card_back.png")
back_card.create_image(400, 263, image = card_front)
back_card.create_text(400, 150, text = "English", font = ("Ariel", 40, "italic"))
back_card_text = back_card.create_text(400, 263, text = "English Word", font = ("Ariel", 60, "bold"))

def next_card():
    global word
    word = random.choice(data)
    back_card.grid_forget()
    front_card.itemconfig(front_card_text, text = word[0])
    front_card.grid(row = 0, column = 0, columnspan = 2)
    timer = window.after(3000, func = flip)

def flip():
    front_card.grid_forget()
    back_card.itemconfig(back_card_text, text = word[1])
    back_card.grid(row = 0, column = 0, columnspan = 2)

def is_correct():
    data.remove(word)
    print(len(data))
    next_card()


# Create the buttons
cross_image = tkinter.PhotoImage(file = "100 days of code/Flashcard/wrong.png")
wrong_button = tkinter.Button(image = cross_image, command = next_card)
wrong_button.grid(row = 1, column = 0)

check_image = tkinter.PhotoImage(file = "100 days of code/Flashcard/right.png")
right_button = tkinter.Button(image = check_image, command = is_correct)
right_button.grid(row = 1, column = 1)

next_card()

window.mainloop()