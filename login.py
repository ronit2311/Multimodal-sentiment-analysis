from tkinter import *
import credential_check

#TKINTER PAGE

page = Tk()
page.title('LOGIN')
page.geometry('250x75')


#USERNAME

user_entry = Entry(page)
user_label = Label(page, text='Username: ')


#PASSWORD
passwd_entry = Entry(page)
passwd_label = Label(page, text='Password: ')


def submit():

    credential_check.check(str(user_entry.get()), str(passwd_entry.get()), page)



submit_button = Button(page, text='SUBMIT', command=submit)

user_entry.grid(row=0, column=1)
user_label.grid(row=0, column=0)

passwd_entry.grid(row=1, column=1)
passwd_label.grid(row=1, column=0)

submit_button.grid(row=2, column=1)

page.mainloop()
