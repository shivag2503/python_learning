from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generate():
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '?']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    list_of_character = password_letters + password_symbols + password_numbers

    random.shuffle(list_of_character)

    gen_pass = "".join(list_of_character)

    input_password.insert(0, gen_pass)

    pyperclip.copy(gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    new_entry = {
        input_website.get(): {
            "email": input_email.get(),
            "password": input_password.get(),
        }
    }

    if len(input_password.get()) == 0 or len(input_website.get()) == 0:
        messagebox.showerror(title="Fields are blank", message="You can't save blank website or password!!")
    else:
        try:
            with open("password_manager.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", mode="w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            data.update(new_entry)

            with open("password_manager.json", "w") as write_file:
                json.dump(data, write_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- Search Password ---------------------------------- #

def search():
    text = input_website.get()
    if text == "":
        messagebox.showerror("Error", "Please enter website for which credentials to be search for")
    else:
        try:
            with open("password_manager.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No Data File Found")
        else:
            if text in data:
                email = data[text]["email"]
                password = data[text]["password"]
                messagebox.showinfo(f"Your {text} credentials", f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showerror("Error", f"No credentials found for {text}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1, sticky=E + W)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky=E + W)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

input_email = Entry(width=35)
input_email.insert(0, "shivamagrawal1166171@gmail.com")
input_email.grid(row=2, column=1, columnspan=2, sticky=E + W)

password = Label(text="Password:")
password.grid(row=3, column=0)

input_password = Entry(width=21)
input_password.grid(row=3, column=1, sticky=E + W)

generate_password = Button(text="Generate Password", command=pass_generate)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save_password)
add.grid(row=4, column=1, columnspan=2, sticky=E + W)

window.mainloop()
