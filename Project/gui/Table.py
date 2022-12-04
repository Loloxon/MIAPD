from tkinter import *


class Table:

    def __init__(self, root, lst):

        for i in range(len(lst)):
            for j in range(len(lst[0])):
                self.e = Entry(root, fg='blue', font=('Arial', 16, 'bold'), width=10)
                self.e.grid(row=i, column=j)
                self.e.insert("end", lst[i][j])
                if i == 0 or j <= i:
                    self.e.config(state=DISABLED)
