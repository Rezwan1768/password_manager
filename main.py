import tkinter
import tkinter.messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]        # generate random letters
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])  # generate random symbols
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])  # generate random numbers

    random.shuffle(password_list)

    password = ''.join(password_list)
    pass_field.delete(0, tkinter.END)
    pass_field.insert(0, password)
    pyperclip.copy(password) # copy password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info_to_file():
    website = website_field.get()
    email = email_field.get()
    password = pass_field.get()

    if website == '' or email == '' or password == '':
        tkinter.messagebox.showwarning(title="Empty Fields", message="Please don't leave any fields empty!")
        return
    # show confirmation message
    confirmation = tkinter.messagebox.askokcancel(title="Confirm", message=f"Website: {website}\nEmail: {email}\n"
                                                                           f"Password: {password}\nPress 'ok' to save")
    if confirmation:
        with open("data.txt", mode='a') as file:
            file.write(website + ' | ' + email + ' | ' + password + '\n')
            # delete the filed content after inserting to file
            website_field.delete(0, tkinter.END)
            pass_field.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

# ---------Window----------
window = tkinter.Tk()
window.title("Lock Pass")
window.configure(padx=50, pady=50)

# ---------Canvas----------
canvas = tkinter.Canvas(width=200, height=200)
# canvas = tkinter.Canvas(width=201, height=224, bg=YELLOW, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# ---------Website label and field--------
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_field = tkinter.Entry(width=35)
website_field.grid(row=1, column=1, columnspan=2, sticky='ew')
website_field.focus()

# ---------Email/Username label, field, and button--------
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_field = tkinter.Entry(width=35)
email_field.grid(row=2, column=1, columnspan=2, sticky='ew')
email_field.insert(0, "someguy@gmail.com")

# ---------Password label and field--------
pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0, sticky='ew')

pass_field = tkinter.Entry(width=21)
pass_field.grid(row=3, column=1, sticky='Ew')

pass_generate_btn = tkinter.Button(text="Generate Password", command= generate_password)
pass_generate_btn.grid(row=3, column=2, sticky='ew')

# ---------add button--------
add_btn = tkinter.Button(text="Add", width=36, command=add_info_to_file)
add_btn.grid(row=4, column=1, columnspan=2, sticky='ew')

window.mainloop()
