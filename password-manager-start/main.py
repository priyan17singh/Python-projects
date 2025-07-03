import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from password_generator import Password_Generator
#--------------------------------Find Password------------------------------------#

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json","r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message = "No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message = "No detail for the website exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = Password_Generator().password
    password_entry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field",message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as file:
                    # Reading the data.
                    data = json.load(file)
                    # Updating old data with new data.
                    
            except FileNotFoundError:
                with open("data.json","w") as file:
                    # Shaving the data.
                    json.dump(new_dict,file,indent=4)
            else:
                data.update(new_dict)
                with open("data.json","w") as file:
                    # Shaving the updated data.
                    json.dump(data,file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize()
window.config(padx=50,pady=50)
window.title("Password manager")

canvas = Canvas(width=200, height=200,highlightthickness=0)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website",font=("Arial",16))
website_label.grid(column=0,row=1)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1,row=1, sticky="EW")

email_label = Label(text="Email/Username",font=("Arial",16))
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2, sticky="EW")
email_entry.insert(END,"priyan17singh@gmail.com")

password_label = Label(text="Password",font=("Arial",16))
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3, sticky="EW")

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3, sticky="EW")

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1, sticky="EW")

add_button = Button(text="Add",width=35, command=save)
add_button.grid(column=1,row=4,columnspan=2, sticky="EW")

window.mainloop()

#--------------------------------END--------------------------------------------------#