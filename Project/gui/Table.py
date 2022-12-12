from tkinter import *

FONT = ('Arial', 16, 'bold')


class Table:

    def __init__(self, root, values, names):
        for i in range(len(names)):
            self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
            self.e.grid(row=i + 1, column=0)
            self.e.insert("end", names[i])
            self.e.config(state=DISABLED)
            self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
            self.e.grid(row=0, column=i + 1)
            self.e.insert("end", names[i])
            self.e.config(state=DISABLED)
        for i in range(len(values)):
            for j in range(len(values[0])):
                self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
                self.e.grid(row=i + 1, column=j + 1)
                self.e.insert("end", round(values[i][j], 3))
                if j <= i:
                    self.e.config(state=DISABLED)
