from tkinter import *

FONT = ('Arial', 16)
FONT_BIG = ('Arial', 20, 'bold')


class Table:

    def __init__(self, root, values, labels, label_root, name):
        self.name = Text(label_root, fg='blue', font=FONT_BIG, width=40, height=3)
        self.name.grid(row=0)
        self.name.insert("end", name)
        self.name.config(state=DISABLED)
        self.name.tag_configure("center", justify='center')
        self.name.tag_add("center", 1.0, "end")
        for i in range(len(labels)):
            self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
            self.e.grid(row=i + 1, column=0)
            self.e.insert("end", labels[i])
            self.e.config(state=DISABLED)
            self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
            self.e.grid(row=0, column=i + 1)
            self.e.insert("end", labels[i])
            self.e.config(state=DISABLED)
        for i in range(min(len(values), len(labels))):
            for j in range(min(len(values[0]), len(labels))):
                self.e = Entry(root, fg='blue', font=FONT, width=10, justify=CENTER)
                self.e.grid(row=i + 1, column=j + 1)
                self.e.insert("end", round(values[i][j], 3))
                if j <= i:
                    self.e.config(state=DISABLED)
