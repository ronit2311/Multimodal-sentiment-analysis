import csv
import main
from tkinter import *


def check(entry_username, entry_passwd, page):

    file = open('credentials.txt', 'r')
    fcsv = csv.reader(file)
    for rec in list(fcsv):
        if entry_username.upper() == rec[0].upper():
            if entry_passwd == rec[1]:
                page.withdraw()
                main.run()
                break
