""" Student Management Program - Attendance, Test Programs"""""

from tkinter import *
from tkinter import PhotoImage
import attendance
import test
import report

def run():


    mainpage = Toplevel()
    mainpage.title('Student Management System')
    mainpage.geometry('620x450')
    mainpage.resizable(0, 0)


    datapher_logo = PhotoImage(file='datapher.png')


    l_logo = Label(mainpage, image=datapher_logo)
    l_logo.place(x=0, y=0, relwidth=1, relheight=1)

    l_credits = Label(mainpage, text='\t Created By: \t Shyam Sundar \t Ronit Bokadia \t Abishek \t', bg='Gray', fg='#420619')

    b_attendance = Button(mainpage, text='Attendance', command=attendance.attendance, bg='Gray', fg='White', activeforeground='Cyan', activebackground='Gray')
    b_create_test = Button(mainpage, text='Create Test', command=test.create_test, bg='Gray', fg='White', activeforeground='Cyan', activebackground='Gray')
    b_add_marks = Button(mainpage, text='Add Marks', command=test.marks_entry, bg='Gray', fg='White', activeforeground='Cyan', activebackground='Gray')
    b_generate_report = Button(mainpage, text='Generate Report', command=report.student_report, bg='Gray', fg='White', activeforeground='Cyan', activebackground='Gray')

    b_attendance.config(width=12, height=5)
    b_create_test.config(width=12, height=5)
    b_add_marks.config(width=12, height=5)
    b_generate_report.config(width=12, height=5)

    l_credits.place(x=95, y=420)

    b_attendance.place(x=65, y=285)
    b_create_test.place(x=202.5, y=285)
    b_add_marks.place(x=332.5, y=285)
    b_generate_report.place(x=470, y=285)

    mainpage.mainloop()
