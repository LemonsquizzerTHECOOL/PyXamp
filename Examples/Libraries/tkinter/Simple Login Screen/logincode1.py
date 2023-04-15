import customtkinter as ctk
import tkinter.messagebox as tkmb

# Set the GUI theme (dark, light, system)
ctk.set_appearance_mode("system")
# I chose system, so it fits with people's OS preferences. (but if I had to choose I would choose dark)

# Set the default color theme (blue, green, dark-blue)
ctk.set_default_color_theme("blue")
# Green looks best, but I chose blue because it is my favorite color :D

app = ctk.CTk()
app.geometry("400x400")
app.title("Simple, Stylish Login Screen")


def login():
    # Define the valid username and password
    username = "Lemon"
    password = "pass123"

    # Check if entered username and password match
    if user_entry.get() == username and user_pass.get() == password:
        logged_in()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Incorrect password!', message='Please try typing the password again.')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Username Not Found!', message='Please check the username you entered and try again.')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


label = ctk.CTkLabel(app, text="Just Some Optional Text")  # Change it however you want (or delete this line)
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login Screen Example')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="•")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# You can delete this if you want lol (or change it)
label = ctk.CTkLabel(master=frame, text='By Lemonsqueezer')
label.pack(pady=12, padx=10)
#

def logged_in():
    success = ctk.CTkToplevel(app)
    success.geometry("300x250")
    success.title("Login Successful!")
    label = ctk.CTkLabel(master=success, text='Success!')
    label.pack(pady=12, padx=10)
# Customize This As Much As You Want!


app.mainloop()
