"""Subprogram - Tests"""

from tkinter import *
import mysql.connector as db
import tkinter as ttk


def create_test():

    page = Tk()
    page.title('DATAPHER')

    l_page = Label(page, text="CREATE A TEST", bg='#008c73', fg="white", font=("roboto", 15, "underline")).place(
        relx=0.3, rely=0)
    page.geometry("500x380")
    page.configure(bg='#008c73')
    page.resizable(0, 0)

    l_testname = Label(page, text='TESTNAME: ', bg='#008c73', fg="white").place(relx=0.2, rely=0.2)
    l_sub1 = Label(page, text='SUB(1): ', bg='#008c73', fg="white").place(relx=0, rely=0.3)
    l_sub2 = Label(page, text='SUB(2): ', bg='#008c73', fg="white").place(relx=0, rely=0.4)
    l_sub3 = Label(page, text='SUB(3): ', bg='#008c73', fg="white").place(relx=0, rely=0.5)
    l_sub4 = Label(page, text='SUB(4): ', bg='#008c73', fg="white").place(relx=0, rely=0.6)
    l_sub5 = Label(page, text='SUB(5): ', bg='#008c73', fg="white").place(relx=0, rely=0.7)

    e_testname = Entry(page)
    e_sub1 = Entry(page)
    e_sub2 = Entry(page)
    e_sub3 = Entry(page)
    e_sub4 = Entry(page)
    e_sub5 = Entry(page)

    e_testname.place(relx=0.35, rely=0.2)
    e_sub1.place(relx=0.1, rely=0.3)
    e_sub2.place(relx=0.1, rely=0.4)
    e_sub3.place(relx=0.1, rely=0.5)
    e_sub4.place(relx=0.1, rely=0.6)
    e_sub5.place(relx=0.1, rely=0.7)

    conn = db.connect(host='localhost', user='root', passwd='ronz2311', database='student_db')
    curs = conn.cursor()

    def create():
        curs.execute(f'CREATE TABLE {str(e_testname.get())} AS (SELECT ROLLNO, NAME FROM attendance)')
        conn.commit()
        curs.execute(f'ALTER TABLE {str(e_testname.get())} ADD ({str(e_sub1.get())} FLOAT, {str(e_sub2.get())} FLOAT, '
            f'{str(e_sub3.get())} FLOAT, {str(e_sub4.get())} FLOAT, {str(e_sub5.get())} FLOAT)')
        conn.commit()
        page.destroy()

    b_create = Button(page, text='DONE', command=create, fg='black', activebackground="grey",
                      activeforeground="cyan").place(relx=0, rely=0.8)

    page.mainloop()


def marks_entry():
    conn = db.connect(host='localhost', user='root', passwd='ronz2311', database='student_db')
    curs = conn.cursor(buffered=True)

    page = Tk()
    page.title('DATAPHER')
    page.geometry("330x350")
    page.config(bg='#008c73')
    l_label = Label(page, text="Which test do you want to add marks for?", bg='#008c73', fg="white", font=5).place(x=10,
                                                                                                                   y=10)

    l_testname = Label(page, text='TESTNAME: ', bg='#008c73', fg="white").place(relx=0, rely=0.2)
    e_testname = Entry(page)
    e_testname.place(relx=0.3, rely=0.2, relwidth=0.62)

    def enter_marks():

        root = Tk()
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        #add scrollbar
        my_canvas = Canvas(main_frame, bg='#008c73')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        marks_page = Frame(my_canvas, bg='#008c73')

        my_canvas.create_window((0, 0), window=marks_page, anchor="nw")

        l_mark_p = Label(marks_page, text="SELECT STUDENT", bg='#008c73', fg="white",
                         font=("Roboto", 15, "underline")).grid(row=2, column=0)

        curs.execute(f'SELECT rollno, NAME FROM {str(e_testname.get().lower())}')
        rows = curs.fetchall()

        def add_student_marks(record):
            student_page = Tk()
            student_page.title('DATAPHER')
            student_page.config(bg='#008c73')
            student_page.geometry('420x400')
            student_page.resizable(0, 0)

            curs.execute(f'SELECT * FROM {str(e_testname.get().lower())}')
            columns = curs.column_names
            l_head = Label(student_page, text="MARKS", bg='#008c73', fg="white",
                           font=("roboto", 20, 'underline')).place(relx=0.4, rely=0.1)

            l_sub1 = Label(student_page, text=columns[2], bg='#008c73', fg="white").place(relx=0.2, rely=0.3)
            l_sub2 = Label(student_page, text=columns[3], bg='#008c73', fg="white").place(relx=0.2, rely=0.4)
            l_sub3 = Label(student_page, text=columns[4], bg='#008c73', fg="white").place(relx=0.2, rely=0.5)
            l_sub4 = Label(student_page, text=columns[5], bg='#008c73', fg="white").place(relx=0.2, rely=0.6)
            l_sub5 = Label(student_page, text=columns[6], bg='#008c73', fg="white").place(relx=0.2, rely=0.7)

            e_sub1 = Entry(student_page)
            e_sub2 = Entry(student_page)
            e_sub3 = Entry(student_page)
            e_sub4 = Entry(student_page)
            e_sub5 = Entry(student_page)

            e_sub1.place(relx=0.42, rely=0.3)
            e_sub2.place(relx=0.42, rely=0.4)
            e_sub3.place(relx=0.42, rely=0.5)
            e_sub4.place(relx=0.42, rely=0.6)
            e_sub5.place(relx=0.42, rely=0.7)

            def save_marks():
                curs.execute(
                    f'UPDATE {str(e_testname.get().lower())} SET {columns[2]} = {str(e_sub1.get())},'
                    f' {columns[3]} = {str(e_sub2.get())}, {columns[4]} = {str(e_sub3.get())},'
                    f' {columns[5]} = {str(e_sub4.get())}, {columns[6]} = {str(e_sub5.get())}'
                    f' WHERE rollno = "{record[0]}" ')
                conn.commit()
                student_page.destroy()

            b_save = Button(student_page, text='SAVE', command=save_marks, bg='grey', fg="black").place(relx=0.4,
                                                                                                           rely=0.8)

        y = 3
        for row in range(len(rows)):
            l_sid = Label(marks_page, text=rows[row][0], bg='#008c73', fg="white").grid(row=y, column=0)
            l_sname = Label(marks_page, text=rows[row][1], bg='#008c73', fg="white").grid(row=y, column=1)
            b_enter_marks = Button(marks_page, text='ADD MARKS', command=lambda row=row: add_student_marks(rows[row]),
                                   bg="grey", fg="black").grid(row=y, column=3)
            y += 1
        b_finish = Button(marks_page, text='FINISH', command=marks_page.destroy,bg='grey', fg="black",
                          activeforeground="black", activebackground="white").grid(row=y, column=1)
        root.mainloop()

    def check_test():
        curs.execute('SHOW TABLES')
        tables = curs.fetchall()
        if (str(e_testname.get().lower()),) in tables:
            enter_marks()
        else:
            l_error = Label(page, text='TABLE DOES NOT EXIST').grid(row=1, column=0)

    b_submit = Button(page, text='SUBMIT', command=check_test, bg='grey', fg="BLACK").place(relx=0.2, rely=0.35)

    page.mainloop()
