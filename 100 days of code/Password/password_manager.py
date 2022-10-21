import email
import tkinter
import random
from tkinter import messagebox
import json

# Set up the window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

# Create the background logo
canvas = tkinter.Canvas(height = 200, width = 200)
logo = tkinter.PhotoImage(file = "100 days of code/Password/logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

# Create the labels
website_label = tkinter.Label(text = "Website:")
website_label.grid(row = 1, column = 0)

username_label = tkinter.Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)

password_label = tkinter.Label(text = "Password:")
password_label.grid(row = 3, column = 0)

# Create user input boxes
website_input = tkinter.Text(height = 1, width = 21)
website_input.grid(row = 1, column = 1)
website_input.focus()

username_input = tkinter.Text(height = 1, width = 35)
username_input.grid(row = 2, column = 1, columnspan = 2)
username_input.insert(tkinter.END, "dallinrima@gmail.com")

password_input = tkinter.Text(height = 1, width = 21)
password_input.grid(row = 3, column = 1)

# Create buttons
def generate_password():
    usable_characters = ['a', 'b', 'c',	'd', 'e', 'f',	'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',	'r', 's', 't', 'u',	'v', 'w', 'x', 'y',	'z', 'A', 'B', 'C',	'D', 'E', 'F',	'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', "^", '&', "*"]
    password_letters = []
    password = ''
    for i in range(15):
        character = random.choice(usable_characters)
        password_letters.append(character)
        password = ''.join(password_letters)
    password_input.insert(tkinter.END, password)

def add_password():
    site = website_input.get(1.0, 'end-1c')
    username = username_input.get(1.0, 'end-1c')
    password = password_input.get(1.0, 'end-1c')
    new_data = {
        site: {
            "username": username,
            "password": password,
        }
    }
    is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\nUsername: {username}\nPassword: {password}\n Is it okay to save?")
    if is_ok == True:
        try: 
            with open('100 days of code/Password/passwords.json', 'r') as data_file:
                data = json.load(data_file)

        except:
            with open("100 days of code/Password/passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)
        else:
            with open('100 days of code/Password/passwords.json', 'r') as data_file:
                data = json.load(data_file)
            data.update(new_data) 
            with open("100 days of code/Password/passwords.json", "w") as data_file:
                json.dump(data, data_file, indent = 4)

def search():
    site = website_input.get(1.0, 'end-1c')
    with open('100 days of code/Password/passwords.json') as data_file:
        data = json.load(data_file)
        if site in data:
            username = data[site]["username"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Username: {username}\nPassword: {password}")

password_gen = tkinter.Button(text = "Generate Password", command = generate_password)
password_gen.grid(row = 3, column = 2)

add = tkinter.Button(text = "Add", command = add_password)
add.grid(row = 4, column = 1)

search = tkinter.Button(text = "Search", width = 13, command = search)
search.grid(row = 1, column = 2)
window.mainloop()