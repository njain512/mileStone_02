'''
Neha Jain
Professor Penta
Programming for IT (CIS 153)
Title: Password Generator
Description: A program that will generate strong password(s) for you.
Type in your name as well as birth month, day, and year followed by age.
You can use numbers or words for all of the above inputs.
Then fill in how many passwords and of what length you want to generate.
Finally click on the 'Generate' button to generate the list of passwords.
Strong passwords will be displayed in a new window.

During the process of creating this program, I realized that I could
build a better program if I changed some of the components I had planned
on using in milestone 0. As such, I used replace instead of append to
make changes to elements in the password that include the user's personal
information. In the place of a list, I created separate variables to hold
the personal information of the user. I have used multiple functions,
including one which has a parameter, multiple if/else statements, a while
loop, a for loop, and multiple GUI windows.

This  program requires the random, string, and tkinter modules to run.

If I had more time, I would have added a radio button to the GUI that would
let the user decide if they want to use special characters or not.
May 6, 2020
'''


import random
import string
import tkinter as tk

window = tk.Tk()

# Title for the window
window.title("Password Generator")

# Window Size
window.geometry("400x310")

# FUNCTIONS ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- -------
def thanks(name):
    top2 = tk.Toplevel()
    thankUser = tk.Label(top2, text=name + ", Thank you for using the Password Generator.", font=("Open Sans", 40))
    thankUser.pack()


# num, len, nameIn, monthIn, dayIn, yearIn, ageIn
def generate_pass():

    num = int(number_password_input.get())
    len = int(length_password_input.get())
    nameIn = str(fullname_input.get())
    monthIn = str(birth_month_input.get())
    dayIn = str(birth_day_input.get())
    yearIn = str(birth_year_Input.get())
    ageIn = str(age_input.get())

    thanks(nameIn)

    top = tk.Toplevel()
    top.title("List of Strong Passwords")

    c=1
    while c <=num:
        c = c + 1

        if len >= 6:
                special_chars = string.punctuation
                letters = string.ascii_letters
                digits = string.digits

                make_pass = ''.join([random.choice(letters + digits + special_chars) for n in range(len)])

                if nameIn in make_pass:
                    make_pass = make_pass.replace(nameIn, random.choice(letters, digits, special_chars))
                    print(make_pass)
                elif monthIn in make_pass:
                    make_pass = make_pass.replace(monthIn, random.choice(letters, digits, special_chars))
                    print(make_pass)
                elif dayIn in make_pass:
                    make_pass = make_pass.replace(dayIn, random.choice(letters, digits, special_chars))
                    print(make_pass)
                elif yearIn in make_pass:
                    make_pass = make_pass.replace(yearIn, random.choice(letters, digits, special_chars))
                    print(make_pass)
                elif ageIn in make_pass:
                    make_pass = make_pass.replace(ageIn, random.choice(letters, digits, special_chars))
                    print(make_pass)
                else:
                    print(make_pass)
                displayPass= tk.Label(top, text=make_pass, font=("Open Sans", 10))
                displayPass.pack()

    if len <6:
        displayPass = tk.Label(top, text="Use more than 5 character to make strong password.", font=("Open Sans", 10))

        displayPass.pack()


#  LAYOUT ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- ------- -------

# GREETING
greet_1 = tk.Label(text="Welcome to Password Generator!", font=("Open Sans", 16))
greet_1.grid(row=0)

# NOTIFICATION
notification = tk.Label(text="Note: At least 6 characters are required for a strong password!", font=("Open San", 12))
notification.grid(row=1)

# FULLNAME
# user's input box
fullname_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
fullname_input.pack(side='left')
# place where you want widget (before or after this button)
fullname_input.grid(row=3)
# insertion cursor at this mark's position
fullname_input.insert(0, "Fullname")

# BIRTH MONTH
# user's input box
birth_month_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_month_input.pack(side='left')
# place where you want widget (before or after this button)
birth_month_input.grid(row=4)
# insertion cursor at this mark's position
birth_month_input.insert(0, "Birth Month")

# BIRTH DAY
# user's input box
birth_day_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_day_input.pack(side='left')
# place where you want widget (before or after this button)
birth_day_input.grid(row=5)
# insertion cursor at this mark's position
birth_day_input.insert(0, "Birth Day")

# BIRTH YEAR
# user's input box
birth_year_Input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
birth_year_Input.pack(side='left')
# place where you want widget (before or after this button)
birth_year_Input.grid(row=6)
# insertion cursor at this mark's position
birth_year_Input.insert(0, "Birth Year")

# AGE
# user's input box
age_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
age_input.pack(side='left')
# place where you want widget (before or after this button)
age_input.grid(row=7)
# insertion cursor at this mark's position
age_input.insert(0, "Age")

# HOW MANY PASSWORDS to generate
# user's input box
number_password_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
number_password_input.pack(side='left')
# place where you want widget (before or after this button)
number_password_input.grid(row=8)
# insertion cursor at this mark's position
number_password_input.insert(0, "Numbers of passwords to generate")

# LENGTH OF a PASSWORD input
# user's input box
length_password_input = tk.Entry(window, width=40, borderwidth=3, relief="sunken")
# places the widget on the side of the window
length_password_input.pack(side='left')
# place where you want widget (before or after this button)
length_password_input.grid(row=9)
# insertion cursor at this mark's position
length_password_input.insert(0, "Length of a password")

# GENERATE BUTTON
generate_btn = tk.Button(text="Generate", bg="orange", fg="white", command=generate_pass)
generate_btn.grid(row=11)

window.mainloop()
