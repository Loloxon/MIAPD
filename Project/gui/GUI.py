from tkinter import *

FONT = ("Arial", 20)
LABEL_FONT = ("Arial", 15)

root = Tk()
root.title("Comparing App")
root.geometry("1280x720")
root.resizable(False, False)

main_window = Frame(root, relief='sunken')
main_window.pack(fill=BOTH, expand=True, padx=10, pady=10)

myLabel1 = Label(main_window, text="Hello")
myLabel2 = Label(main_window, text="Hellhrdo")
myLabel3 = Label(main_window, text="Hellntsnhrdo")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=1, column=1)


def add_country(text_box):
    text_box.delete("1.0", "end")
    label = Label(main_window, text="Clicked")
    label.grid(row=3, column=0)


add_country_label = Label(main_window, text="Add country", font=LABEL_FONT)
add_country_label.grid(row=0, column=0)
add_country_text_box = Text(main_window, width=20, height=1, bg="white", font=FONT)
add_country_text_box.insert(INSERT, "Poland")
add_country_text_box.grid(row=1, column=0)
add_country_button = Button(main_window, text="Add new country", font=FONT,
                            command=lambda: add_country(add_country_text_box))
add_country_button.grid(row=2, column=0)


def add_criterion(text_box):
    text_box.delete("1.0", "end")
    label = Label(main_window, text="Clicked")
    label.grid(row=3, column=1)


add_criterion_label = Label(main_window, text="Add criterion", font=LABEL_FONT)
add_criterion_label.grid(row=0, column=1)
add_criterion_text_box = Text(main_window, width=20, height=1, bg="white", font=FONT)
add_criterion_text_box.insert(INSERT, "Military force")
add_criterion_text_box.grid(row=1, column=1)
add_criterion_button = Button(main_window, text="Add new criterion", font=FONT,
                              command=lambda: add_criterion(add_criterion_text_box))
add_criterion_button.grid(row=2, column=1, padx=50)


def solve():
    label = Label(main_window, text="Clicked")
    label.grid(row=3, column=2)


buttonSolve = Button(main_window, text="Solve", font=FONT, command=solve, bg="blue", fg="pink")
buttonSolve.grid(row=2, column=2)

main_window.mainloop()
