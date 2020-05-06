import random
import string
import tkinter as tk

window = tk.TK()

# Title for the window
window.title("Password Generator")

# Window Size
window.geometry("400x600")

# FUNCTIONS


special_char = ['!', '@', '£', '$', '%', '^', '&', '*', '(', ')', '.', ',', '?']

def make_password1();
len = length_password

random_lengthPass =''.join(random.choice(chars=string.ascii_lowercase + string.ascii_uppercase + string.digits)
                     for i in range(len))


def make_password2();
    num = number_password

    newPass = []
    for i in range(num):
        print make_password1(len, chars)

    getName = str(fullname.get())
    return phrase[random.randint(0, 3)] + name


def pass_output();
    getOutput = make_password2()

    pass_output = tk.label(text="", font=("Open Sans", 12))
    pass_output.grid(row=15)

    pass_output.insert(tk.END, getOutput)



#  LAYOUT

# GREETING
greeting = tk.label(text="Welcome to Password Generator!", font=("Open Sans", 16))
greeting.grid(row=0)

# NOTIFICATION
notification = tk.label(text="Note: More than 8 characters for password is stronger!", font=("Open San", 12))
notification.grid(row=1)

# FULLNAME
# user's input
fullname = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
fullname.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
fullname.grid(row=3)
# insertion cursor at this mark's position
fullname.insert(0, "Fullname")

# BIRTH MONTH
# user's input
birth_month = tk.Entry(window, width=20, borderwidth=5, relief="sunken")
# places the widget on the side of the window
birth_month.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_month.grid(row=4)
# insertion cursor at this mark's position
birth_month.insert(0, "Birth Month")

# BIRTH DAY
# user's input
birth_day = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_day.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_day.grid(row=5)
# insertion cursor at this mark's position
birth_day.insert(0, "Birth Day")

# BIRTH YEAR
# user's input
birth_year = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_year.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_year.grid(row=6)
# insertion cursor at this mark's position
birth_year.insert(0, "Birth Year")


# AGE
# user's input
age = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
age.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
age.grid(row=7)
# insertion cursor at this mark's position
age.insert(0, "Age")


# HOW MANY PASSWORDS to generate
# user's input
number_password = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
number_password.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
number_password.grid(row=7)
# insertion cursor at this mark's position
number_password.insert(0, "Numbers of passwords to generate")


# LENGTH OF a PASSWORD
# user's input
length_password = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
length_password.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
length_password.grid(row=7)
# insertion cursor at this mark's position
length_password.insert(0, "Numbers of passwords to generate")


# GENERATE BUTTON
generate_btn = tk.Button(text="Generate", command=pass_output, bg="orange")
#Generate = Button(root, text="Generate", padx=50, pady=300, command=Clicks)
generate_btn.grid(row=11)

# NEW PASSWORD GREETING
pw_gre = tk.label(text="Your NEW Password!", font=("Open Sans", 13))
pw_gre.grid(row=13)

# Display NEW PASSWORDS
new_pw = tk.label(font=("Open Sans", 12))
new_pw.grid(row=15)



window.mainloop()
