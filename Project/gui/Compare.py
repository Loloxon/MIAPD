from tkinter import *

FONT = ('Arial', 16, 'bold')


class Compare:

    def __init__(self, root, names, index, labels):
        self.root = root
        self.names = names
        self.index = index
        self.labels = labels

    def compare(self):
        idx = self.index
        for i in range(len(self.names)):
            for idx1 in range(len(self.names[i])):
                for idx2 in range(idx1 + 1, len(self.names[i])):
                    print(idx1, idx2)
                    if idx == 0:
                        self.index += 1
                        return self.show_compare(self.names[i][idx1], self.names[i][idx2], self.root, self.labels[i])
                    idx -= 1
        return -1, -1
    def show_compare(self, name1, name2, root, label):
        print(label)
        e = Entry(root, fg='black', font=FONT, width=50, justify=CENTER)
        e.grid(row=0, column=0, columnspan=4)
        e.insert("end", label)
        e.config(state=DISABLED)
        e = Entry(root, fg='black', font=FONT, width=20, justify=CENTER)
        e.grid(row=1, column=0)
        e.insert("end", name1)
        e.config(state=DISABLED)
        s1 = Scale(root, from_=9, to=1, width=25)
        s1.grid(row=1, column=1, padx=5)
        s2 = Scale(root, from_=9, to=1, width=25)
        s2.grid(row=1, column=2, padx=5)
        # e = Entry(root, fg='black', font=FONT, width=10, justify=CENTER)
        # e.grid(row=1, column=1)
        # # e.insert("end", "nonono")
        # e.config(state=NORMAL)
        e = Entry(root, fg='black', font=FONT, width=20, justify=CENTER)
        e.grid(row=1, column=3)
        e.insert("end", name2)
        e.config(state=DISABLED)
        return s1, s2

