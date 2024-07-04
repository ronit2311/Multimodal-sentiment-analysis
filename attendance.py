from tkinter import *
from tkinter import ttk
import mysql.connector as db
import datetime
import csv


def attendance():
    # getting student records from csv file

    f = open("attendance.csv", "r")
    records = list(csv.reader(f))
    print(records)

    today = datetime.date.today().strftime('%d%m%Y')
    conn = db.connect(host='localhost', user='root', passwd='ronz2311', database='student_db')
    curs = conn.cursor()

    curs.execute("create table attendance(rollno INT, name varchar(100))")
    conn.commit()


    for i in records:
        curs.execute(f'insert into attendance values("{i[0]}","{i[1]}")')
        conn.commit()


    curs.execute(f'ALTER TABLE ATTENDANCE ADD D{today} VARCHAR(10)')
    conn.commit()

    def mark_attendance(record, entry):
        curs.execute(f'UPDATE ATTENDANCE SET D{today} = "{entry}" WHERE rollno = "{record[0]}" ')
        conn.commit()

    root = Tk()
    root.title('DATAPHER')

    # Create A Main Frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame, bg='#008c73')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas, bg='#008c73')

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    l_title = Label(second_frame, text="STUDENT ATTENDANCE", bg='#008c73', fg='White',
                    font=("roboto", 15, "underline")).grid(row=0, pady=10, padx=20)

    curs.execute('SELECT rollno, name FROM ATTENDANCE')
    rows = curs.fetchall()
    num = 2
    for row in range(len(rows)):
        l_sid = Label(second_frame, text=rows[row][0], bg='#008c73', fg='White').grid(row=num, column=0)

        l_sname = Label(second_frame, text=rows[row][1], bg='#008c73', fg='White').grid(row=num, column=3)

        b_present = Button(second_frame, text='PRESENT', command=lambda row=row: mark_attendance(rows[row], 'P'),
                           bg='#383031',
                           fg='white', activebackground='white', activeforeground='black').grid(row=num, column=5,
                                                                                                padx=10, pady=10)
        b_absent = Button(second_frame, text='ABSENT', command=lambda row=row: mark_attendance(rows[row], 'A'),
                          bg='#383031',
                          fg='white', activebackground='white', activeforeground='black').grid(row=num, column=7,
                                                                                               padx=10, pady=10)
        b_on_duty = Button(second_frame, text='ON DUTY', command=lambda row=row: mark_attendance(rows[row], 'OD'),
                           bg='#383031', fg='white', activebackground='white', activeforeground='black').grid(row=num,
                                                                                                              column=9,
                                                                                                              padx=10,
                                                                                                              pady=10)
        num += 3

    root.mainloop()
