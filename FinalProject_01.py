'''
Neha Jain
Professor Penta
Programming for IT (CIS 153)
Title: Password Generator
Description: A program that will generate strong password(s) for you.
Type in your name, birth month, birth day, birth year, age.
Then fill in how many numbers of passwords and
how much longer or length of a password to generate.
Then click on 'Generate' button to generate. The program will
display strong passwords at the bottom.
I used while loop, for loop, if-else statement, parameter import random, and tkinter (GUI).
I wish I more time to make the radio button for the user if they want to use special characters or not..
May 6, 2020
'''


import random
import string
import tkinter as tk

window = tk.TK()

# Title for the window
window.title("Password Generator")

# Window Size
window.geometry("400x600")

def examplefunc():
    show_pass_func(number_password_input,length_password_input,fullname_input, birth_month_input, birth_day_input, birth_year_Input, age_input)


# FUNCTIONS
def show_pass_func(num, len, nameIn, monthIn, dayIn, yearIn, ageIn):
    special_chars = string.punctuation

    # new_pw_result = rand_generator.get()

    while num >= 6:
        #new_pw = str()

        newPass = [i]
        for i in range(num):
            special_chars = string.punctuation
            letters = string.ascii_letters
            digits = string.digits
            for i in range(len):
                make_pass = ''.join(random.choice(letters, digits, special_chars))

                if nameIn in make_pass:
                    make_pass = make_pass.replace(nameIn, "ochoay")
                    print(make_pass)
                elif monthIn in make_pass:
                    make_pass = make_pass.replace(monthIn, "wink")
                    print(make_pass)
                elif dayIn in make_pass:
                    make_pass = make_pass.replace(dayIn, "00")
                    print(make_pass)
                elif yearIn in make_pass:
                    make_pass = make_pass.replace(yearIn, "pow")
                    print(make_pass)
                elif ageIn in make_pass:
                    make_pass = make_pass.replace(ageIn, "5783")
                    print(make_pass)
                else:
                    print(make_pass)
    if num < 6:
        print("Use more than 5 character to make strong password.")



        #random_lengthPass = ''.join(random.choice(chars=string.ascii_lowercase + string.ascii_uppercase + string.digits)
        #                            for i in range(len))




#  LAYOUT

# GREETING
greet_1 = tk.label(text="Welcome to Password Generator!", font=("Open Sans", 16))
greet_1.grid(row=0)

# NOTIFICATION
notification = tk.label(text="Note: At least 6 characters are required for a strong password!", font=("Open San", 12))
notification.grid(row=1)

# FULLNAME
# user's input box
fullname_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
fullname_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
fullname_input.grid(row=3)
# insertion cursor at this mark's position
fullname_input.insert(0, "Fullname")

# BIRTH MONTH
# user's input box
birth_month_input = tk.Entry(window, width=20, borderwidth=5, relief="sunken")
# places the widget on the side of the window
birth_month_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_month_input.grid(row=4)
# insertion cursor at this mark's position
birth_month_input.insert(0, "Birth Month")

# BIRTH DAY
# user's input box
birth_day_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_day_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_day_input.grid(row=5)
# insertion cursor at this mark's position
birth_day_input.insert(0, "Birth Day")

# BIRTH YEAR
# user's input box
birth_year_Input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_year_Input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
birth_year_Input.grid(row=6)
# insertion cursor at this mark's position
birth_year_Input.insert(0, "Birth Year")


# AGE
# user's input box
age_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
age_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
age_input.grid(row=7)
# insertion cursor at this mark's position
age_input.insert(0, "Age")


# HOW MANY PASSWORDS to generate
# user's input box
number_password_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
number_password_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
number_password_input.grid(row=7)
# insertion cursor at this mark's position
number_password_input.insert(0, "Numbers of passwords to generate")


# LENGTH OF a PASSWORD input
# user's input box
length_password_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
length_password_input.pack(side='left', ipadx=20, padx=30)
# place where you want widget (before or after this button)
length_password_input.grid(row=7)
# insertion cursor at this mark's position
length_password_input.insert(0, "Numbers of passwords to generate")


# GENERATE BUTTON
generate_btn = tk.Button(text="Generate", bg="orange", fg="white", command=show_pass_func,)
#Generate = Button(root, text="Generate", padx=50, pady=300, command=Clicks)
generate_btn.grid(row=11)

# NEW PASSWORD GREETING
greet_2 = tk.label(text="Your NEW Password!", font=("Open Sans", 13))
greet_2.grid(row=13)

# Display all NEW PASSWORDS
show_pass_func = tk.label(text=make_pass, font=("Open Sans", 12))
show_pass_func.grid(row=15)


window.mainloop()
