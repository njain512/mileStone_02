#!/bin/python3

import random
from tkinter import *

root = Tk()
root.title("Password Generator")

print('Welcome to Password Generator')
print('Note: More than 8 characters for password is stronger!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

fullname = Entry(root, width=40, paddedborderwidth=5)
fullname.pack()
fullname.insert(0, "Fullname")

birtdate = Entry(root, width=40, paddedborderwidth=5)
birthdate.pack()
birthdate.insert(0, "Birthdate (**/**/****)")

age = Entry(root, width=40, paddedborderwidth=5)
age.pack()
age.insert(0, "Age")

number = Entry(root, width=10, paddedborderwidth=5)
number = int(number)
number.pack()
number, insert(0, 'Size of passwords')

length = Entry(root, width=10, paddedborderwidth=5)
length = int(length)
length.pack()
length.insert(0, 'Length of password')


def Clicks():
    Labels = Label(root, text=fullname.get())
    Labels.pack()


Generate = Button(root, text="Generate", padx=50, pady=300, command=Clicks)
Generate.pack()

root.mainloop()

print('Welcome to Password Generator')
print('Note: More than 8 characters for password is stronger!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

fullname = input('What is your name?: ')
birtdate = input('Your birthdate?: ')
age = input('Your Age?: ')
number = input('How many passwords do you want to generate?: ')
number = int(number)

length = input('Enter length of password: ')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
