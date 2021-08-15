import tkinter
import add_function as af
import search_function as sf

global phone_data
global web_entry
global with_google
global without_google
global web_label
global phone_checkbox
global add_button
global search_button
phone_data = "NA"

global email_label
global pass_label
global email_entry
global pass_entry
global gen_pass_button

white = "#fefefe"
window = tkinter.Tk()
window.config(padx=50, pady=20, highlightthickness=0, bg=white)
window.title("Password Manager")

icon = tkinter.PhotoImage(file="lock.png")
window.iconphoto(False, icon)

canvas = tkinter.Canvas(width=400, height=400, highlightthickness=0, bg=white)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=logo)
canvas.grid(row=0, column=1)


def add_data():
    sf.destroy_data()
    af.add_data()


def search_data():
    af.destroy_data()
    sf.search_data()


radio_state_main = tkinter.IntVar()
add_radio = tkinter.Radiobutton(text="Add Account Details", value=1, variable=radio_state_main, command=add_data,
                                bg=white)
add_radio.grid(row=1, column=0)

search_radio = tkinter.Radiobutton(text="Search Account Details", value=2, variable=radio_state_main,
                                   command=search_data,
                                   bg=white)
search_radio.grid(row=1, column=3)

window.mainloop()
