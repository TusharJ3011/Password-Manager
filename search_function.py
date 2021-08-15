import tkinter
from json import JSONDecodeError
from tkinter import messagebox
import json

white = "#fefefe"


def search_data():
    global web_entry
    global web_label
    global search_button

    def search():
        global details

        web = web_entry.get()
        if web == "":
            messagebox.showerror(title="Error!", message="Please enter data to search.")
            return
        try:
            with open("data.json", "r") as file:
                website = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            messagebox.showinfo(title="Search Result", message="Data not found")
        else:
            try:
                website_details = website[web.title()]
            except KeyError:
                messagebox.showinfo(title="Search Result", message="Data not found")
            else:
                email = website_details["Email/Username"]
                google_sign_in = website_details["Sign In Details"]
                password = website_details["Password"]
                mobile_number = website_details["Mobile Number"]
                details = tkinter.Label(text=f"\nSearch Result\nWebsite: {web.title()}\n{google_sign_in}\nEmail/Username: {email}\nPassword: {password}\nMobile Number: {mobile_number}", bg=white)
                details.grid(row=4, column=1)
        web_entry.delete(0, tkinter.END)

    web_label = tkinter.Label(text="Website:", bg=white)
    web_label.grid(row=2, column=0)

    web_entry = tkinter.Entry(width=75, relief="ridge", bg=white)
    web_entry.grid(row=2, column=1, columnspan=2)

    search_button = tkinter.Button(text="Search", command=search, bg=white, width=100, relief="ridge")
    search_button.grid(row=3, column=0, columnspan=3)


def destroy_data():
    global web_entry
    global web_label
    global search_button
    global details

    try:
        web_label.destroy()
        web_entry.destroy()
        search_button.destroy()
        details.destroy()
    except NameError:
        pass
