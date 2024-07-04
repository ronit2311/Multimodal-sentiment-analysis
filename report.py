"""Subprogram - Report"""

import mysql.connector as db
from tkinter import *


def student_report():

    conn = db.connect(host='localhost', user='root', passwd='ronz2311', database='student_db')
    curs = conn.cursor(buffered=True)
    curs.execute('SHOW TABLES')
    all_tables = curs.fetchall()
    all_tables.remove(('attendance',))   #list of all test names
    print(all_tables)

    page = Toplevel()
    page.title('DATAPHER')
    page.config(bg='#008c73')
    page.geometry('500x400')

    l_page = Label(page, text="TESTS", bg='#008c73', fg="white", font=("roboto", 15, 'bold')).place(relx=0, rely=0)
    page.resizable(0, 0)

    def generate_report(table):

        page.destroy()

        report_page = Tk()
        report_page.title("DATAPHER")
        report_page.geometry("550x400")
        report_page.resizable(0, 0)
        report_page.config(bg="#008c73")

        l_report = Label(report_page, text="ENTER STUDENT NAME", bg='#008c73',
                         fg="white", font=("roboto", 15, 'bold')).place(relx=0, rely=0.05)

        student_entry = Entry(report_page)
        student_entry.place(relx=0.005, rely=0.15)

        curs.execute("show tables")
        curs.execute(f'SELECT * FROM {table}')
        records = curs.fetchall()
        columns = curs.column_names

        def add_report():
            x = str(student_entry.get()).upper()

            student_report_page = Toplevel()
            student_report_page.title("DATAPHER")
            student_report_page.config(bg='#008c73')
            student_report_page.geometry("650x450")
            student_report_page.resizable(0, 0)

            for i in records:
                if i[1].upper() == x:
                    r_num = i[0]

                    l_report_page = Label(student_report_page, text="TEST REPORT", bg='#008c73', fg='white',
                                          font=("roboto", 15, 'underline'), justify='center').place(relx=0.35, rely=0.1)

                    text = Label(student_report_page, text=f'Name: {x}', bg='#008c73', fg="white",
                                 font=("Roboto", 13)).place(relx=0, rely=0.45)

                    text3 = Label(student_report_page, text=f'Roll Number: {r_num}', bg='#008c73', fg="white",
                                  font=("Roboto", 13)).place(relx=0.7, rely=0.45)

                    l_school = Label(student_report_page, text="THE PSBB MILLENNIUM SCHOOL", bg='#008c73', fg="white",
                                     font=("roboto", 15)).place(relx=0.28, rely=0.25)

                    text = Label(student_report_page, text="Academic year 2020-21", bg='#008c73', fg='#b6bdcf',
                                 justify='center',
                                 font=("Roboto", 14, "italic")).place(relx=0.3, rely=0.35)

                    text = Label(student_report_page, text="Class & Section: 12 'A'", bg='#008c73', fg="white",
                                 font=("Roboto", 13)).place(relx=0.3, rely=0.45)

                    m = 0.55
                    n = 0.25
                    for p in range(8):
                        r_border = Label(student_report_page, text="|", bg='#008c73', fg="white").place(relx=0.25,
                                                                                                        rely=m)

                        l_border = Label(student_report_page, text="|", bg='#008c73', fg="white").place(relx=0.6,
                                                                                                        rely=m)

                        m += 0.05
                        n += 0.05

                    c = 2
                    d = 0.65
                    for j in range(5):
                        test = Label(student_report_page, text=table.upper(), bg='#008c73', fg="white").place(relx=0.5,
                                                                                                              rely=0.55)
                        sub = Label(student_report_page, text=columns[j + 2], bg='#008c73', fg="white").place(relx=0.3,
                                                                                                              rely=d)
                        marks = Label(student_report_page, text=i[c], bg='#008c73', fg="white").place(relx=0.5, rely=d)

                        c += 1
                        d += 0.05
                    student_report_page.mainloop()

        submit = Button(report_page, text="GENERATE REPORT", command=add_report, bg='Gray', fg='Cyan',
                        activebackground='Gray', activeforeground="white").place(relx=0.005, rely=0.25)
        report_page.mainloop()

    a = 0.11
    for table in all_tables:
        l_table = Label(page, text=table[0].upper(), bg='#008c73', fg="white").place(relx=0, rely=a)
        b_table = Button(page, text='SELECT', command=lambda table=table: generate_report(table[0]), bg='Gray',
                         fg="Cyan", activebackground='Gray', activeforeground="white").place(relx=0.2, rely=a)
        a += 0.1

    page.mainloop()


