from tkinter import *

FONT = ('Arial', 16, 'bold')


class Compare:

    def __init__(self, root, names, index):
        self.root = root
        self.names = names
        self.index = index
        self.compare()

    def compare(self):
        idx = self.index
        print(idx)
        for idx1 in range(len(self.names)):
            for idx2 in range(idx1 + 1, len(self.names)):
                print(idx1, idx2)
                if idx == 0:
                    self.show_compare(self.names[idx1], self.names[idx2], self.root)
                    self.index += 1
                    return True
                idx -= 1
        return False

    def show_compare(self, name1, name2, root):
        e = Entry(root, fg='black', font=FONT, width=10)
        e.grid(row=0, column=0)
        e.insert("end", name1)
        e.config(state=DISABLED)
        e = Entry(root, fg='black', font=FONT, width=10)
        e.grid(row=0, column=1)
        # e.insert("end", "nonono")
        e.config(state=NORMAL)
        e = Entry(root, fg='black', font=FONT, width=10)
        e.grid(row=0, column=2)
        e.insert("end", name2)
        e.config(state=DISABLED)

        # for i in range(len(names)):
        #     self.e = Entry(root, fg='blue', font=FONT, width=10)
        #     self.e.grid(row=i + 1, column=0)
        #     self.e.insert("end", names[i])
        #     self.e.config(state=DISABLED)
        #     self.e = Entry(root, fg='blue', font=FONT, width=10)
        #     self.e.grid(row=0, column=i + 1)
        #     self.e.insert("end", names[i])
        #     self.e.config(state=DISABLED)
        # for i in range(len(values)):
        #     for j in range(len(values[0])):
        #         self.e = Entry(root, fg='blue', font=FONT, width=10)
        #         self.e.grid(row=i + 1, column=j + 1)
        #         self.e.insert("end", round(values[i][j], 3))
        #         if i == 0 or j <= i:
        #             self.e.config(state=DISABLED)
