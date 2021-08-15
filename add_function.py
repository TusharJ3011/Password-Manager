import tkinter
from json import JSONDecodeError
from tkinter import messagebox
import json
from random import randint, shuffle, choice
import pyperclip

white = "#fefefe"


def add_data():
    global phone_data
    global web_entry
    global with_google
    global without_google
    global web_label
    global phone_checkbox
    global add_button
    phone_data = "NA"

    global email_label
    global pass_label
    global email_entry
    global pass_entry
    global gen_pass_button

    def gen_pass():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        password_letters = [choice(letters) for i in range(randint(8, 10))]
        password_symbols = [choice(symbols) for i in range(randint(2, 4))]
        password_numbers = [choice(numbers) for i in range(randint(2, 4))]
        password_list = password_numbers + password_letters + password_symbols
        shuffle(password_list)
        password = ''
        for char in password_list:
            password += char
        pass_entry.delete(0, tkinter.END)
        pass_entry.insert(0, password)
        pyperclip.copy(password)

    def google_data():
        global email_label
        global pass_label
        global email_entry
        global pass_entry
        global gen_pass_button
        global radio_value
        try:
            email_label.destroy()
            pass_label.destroy()
            email_entry.destroy()
            pass_entry.destroy()
            gen_pass_button.destroy()
        except NameError:
            pass

        text = tkinter.StringVar()
        text.set("NA")
        email_label = tkinter.Label(text="Google Account Address/Username:", bg=white)
        pass_label = tkinter.Label(text="Password:", bg=white)
        email_entry = tkinter.Entry(width=75, relief="ridge", bg=white)
        pass_entry = tkinter.Entry(width=75, relief="ridge", bg=white, state="disabled", textvariable=text)
        email_label.grid(row=4, column=0)
        pass_label.grid(row=5, column=0)
        email_entry.grid(row=4, column=1, columnspan=2)
        pass_entry.grid(row=5, column=1, columnspan=2)
        radio_value = 1
        return

    def enter_data():
        global email_label
        global pass_label
        global email_entry
        global pass_entry
        global gen_pass_button
        global radio_value
        try:
            email_label.destroy()
            pass_label.destroy()
            email_entry.destroy()
            pass_entry.destroy()
        except NameError:
            pass

        email_label = tkinter.Label(text="Email/Username:", bg=white)
        pass_label = tkinter.Label(text="Password", bg=white)
        email_entry = tkinter.Entry(width=75, relief="ridge", bg=white)
        pass_entry = tkinter.Entry(width=48, relief="ridge", bg=white)
        gen_pass_button = tkinter.Button(text="Generate Password", command=gen_pass, bg=white, relief="ridge")
        email_label.grid(row=4, column=0)
        pass_label.grid(row=5, column=0)
        email_entry.grid(row=4, column=1, columnspan=2)
        pass_entry.grid(row=5, column=1)
        gen_pass_button.grid(row=5, column=2)
        radio_value = 2
        return

    def add_phone_number():
        is_checked = checked_state.get()
        global phone_entry
        global phone_data
        if is_checked:
            phone_entry = tkinter.Entry(width=75, relief="ridge", bg=white)
            phone_entry.grid(row=6, column=1, columnspan=2)
        else:
            phone_entry.destroy()
            phone_data = "NA"
            print(phone_data)

    def add():
        global email_entry
        global pass_entry
        global phone_data
        global phone_entry
        global radio_value
        try:
            phone_data = phone_entry.get()
        except:
            pass
        if phone_data == "":
            phone_data = "NA"
        print(phone_data)
        web = web_entry.get()
        try:
            email = email_entry.get()
            password = pass_entry.get()
        except NameError:
            messagebox.showerror(title="Error", message=f"Please Enter Sign In Details!")
            return
        if radio_value == 1:
            google_sign_in = "Signed In With Google"
        elif radio_value == 2:
            google_sign_in = "Signed In Without Google"
        errors = ''
        if len(web) == 0 or len(email) == 0 or len(password) == 0:
            if len(web) == 0: errors += "Website, "
            if len(email) == 0: errors += "Email/Username, "
            if len(password) == 0: errors += "Password, "
            messagebox.showerror(title="Error", message=f"{errors[0:-2]} fields missing!")
            return
        print(phone_data)
        save_data = messagebox.askyesno(title="Confirmation",
                                        message=f"Data Entries:\nWebsite: {web}\n{google_sign_in}\nEmail/Username: {email}\nPassword: {password}\nMobile Number: {phone_data}\nDo "
                                                "you want to save it?")
        web = web.title()
        if save_data:
            new_data = {web:
                            {"Email/Username": email,
                             "Sign In Details": google_sign_in,
                             "Password": password,
                             "Mobile Number": phone_data}
                        }
            try:
                with open("data.json", "r") as file:
                    old_data = json.load(file)
            except (FileNotFoundError, JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                old_data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(old_data, file, indent=4)
        web_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        pass_entry.delete(0, tkinter.END)
        try:
            phone_entry.delete(0, tkinter.END)
        except:
            pass

    web_label = tkinter.Label(text="Website:", bg=white)
    web_label.grid(row=2, column=0)

    web_entry = tkinter.Entry(width=75, relief="ridge", bg=white)
    web_entry.grid(row=2, column=1, columnspan=2)

    radio_state = tkinter.IntVar()
    with_google = tkinter.Radiobutton(text="Signed In with Google", value=1, variable=radio_state, command=google_data,
                                      bg=white)
    without_google = tkinter.Radiobutton(text="Signed In without Google", value=2, variable=radio_state,
                                         command=enter_data,
                                         bg=white)
    with_google.grid(row=3, column=0)
    without_google.grid(row=3, column=2)

    checked_state = tkinter.IntVar()
    phone_checkbox = tkinter.Checkbutton(text="Do you want to add mobile number?", variable=checked_state, onvalue=True,
                                         offvalue=False, command=add_phone_number, bg=white)
    phone_checkbox.grid(row=6, column=0)

    add_button = tkinter.Button(text="Add", command=add, bg=white, width=100, relief="ridge")
    add_button.grid(row=7, column=0, columnspan=3)


def destroy_data():
    global web_entry
    global with_google
    global without_google
    global web_label
    global phone_checkbox
    global add_button
    global email_label
    global pass_label
    global email_entry
    global pass_entry
    global gen_pass_button
    global phone_entry

    try:
        web_label.destroy()
        web_entry.destroy()
        with_google.destroy()
        without_google.destroy()
        phone_checkbox.destroy()
        add_button.destroy()
        email_label.destroy()
        pass_label.destroy()
        email_entry.destroy()
        pass_entry.destroy()
        gen_pass_button.destroy()
        phone_entry.destroy()
    except NameError:
        pass
