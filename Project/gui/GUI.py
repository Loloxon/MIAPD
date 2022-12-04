from tkinter import *
from tkinter.messagebox import showinfo

from gui.Table import Table

FONT = ("Arial", 20)
LABEL_FONT = ("Arial", 15)

root = Tk()
root.title("Comparing App")
root.geometry("1280x720")
root.resizable(False, False)

main_window = Frame(root, relief='sunken')
main_window.pack(fill=BOTH, expand=True, padx=10, pady=10)

# TODO
missing_data = True
#####################################           COUNTRY           #####################################

column_no = 0
row_no = 0
country_no = 0


def add_country(entry):
    global country_no
    entry.delete(0, "end")
    country_no += 1
    entry.delete(0, "end")
    entry.insert(0, "Unknown Country " + str(country_no))


add_country_label = Label(main_window, text="Enter the country", font=LABEL_FONT)
add_country_label.grid(row=row_no + 0, column=column_no)
add_country_entry = Entry(main_window, width=20, font=FONT, bd=1)
add_country_entry.insert(0, "Unknown Country 0")
add_country_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=10)
add_country_button = Button(main_window, text="Add new country", font=FONT,
                            command=lambda: add_country(add_country_entry))
add_country_button.grid(row=row_no + 2, column=column_no)

#####################################           CRITERION           #####################################

column_no = 1
row_no = 0
criterion_no = 0


def add_criterion(entry):
    global criterion_no
    entry.delete(0, "end")
    criterion_no += 1
    entry.delete(0, "end")
    entry.insert(0, "Unknown Criterion " + str(criterion_no))


add_criterion_label = Label(main_window, text="Enter the criterion", font=LABEL_FONT)
add_criterion_label.grid(row=row_no + 0, column=column_no)
add_criterion_entry = Entry(main_window, width=20, font=FONT)
add_criterion_entry.insert(0, "Unknown Criterion 0")
add_criterion_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=10)
add_criterion_button = Button(main_window, text="Add new criterion", font=FONT,
                              command=lambda: add_criterion(add_criterion_entry))
add_criterion_button.grid(row=row_no + 2, column=column_no, padx=50)

#####################################           EXPERT           #####################################

column_no = 2
row_no = 0
expert_no = 0


def add_expert(entry):
    global expert_no
    expert_no += 1
    entry.delete(0, "end")
    entry.insert(0, "Unknown Expert " + str(expert_no))


add_expert_label = Label(main_window, text="Enter the expert name", font=LABEL_FONT)
add_expert_label.grid(row=row_no, column=column_no)
add_expert_entry = Entry(main_window, width=20, font=FONT)
add_expert_entry.insert(0, "Unknown Expert 0")
add_expert_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=10)
add_expert_button = Button(main_window, text="Add new expert", font=FONT,
                           command=lambda: add_expert(add_expert_entry))
add_expert_button.grid(row=row_no + 2, column=column_no, padx=50)

#####################################           EXPERTS' PREVIEW           #####################################

column_no = 3
row_no = 3


def preview():
    root.withdraw()
    preview_window = Toplevel()
    preview_window.title("Opinions")
    preview_window.geometry("1280x720")
    # "1024x576"
    preview_window.resizable(False, False)

    frame = Frame(preview_window, bg="light grey", pady=10, padx=10)
    frame.grid(row=0, column=0, padx=5, pady=5)

    preview_frame = Frame(preview_window, bg="light grey", pady=10, padx=10)
    preview_frame.grid(row=0, column=1, padx=5, pady=5)

    # TODO tutaj zaciągnąć z DB
    experts = ("Johnny", "Tom", "Annie", "Bob", "Rosie")
    experts_listbox = Listbox(frame, listvariable=Variable(value=experts), height=len(experts))
    experts_listbox.grid(row=0, column=0, padx=10, pady=10)
    experts_listbox.itemconfig(1, {'bg': 'red'})

    criteria = ("Military Strength", "Economical Strength", "Distance", "Political Relations")
    criteria_listbox = Listbox(frame, listvariable=Variable(value=criteria), height=len(criteria))
    criteria_listbox.grid(row=0, column=1, padx=10, pady=10)

    subcriteria = [("Fleet", "Aviation", "Land Forces"),
                   ("Current", "Through time"),
                   "",
                   ("With Country", "With Neighbours")]
    subcriteria_listbox = Listbox(frame, listvariable=Variable(value=subcriteria[0]), height=len(subcriteria[0]))
    subcriteria_listbox.grid(row=0, column=2, padx=10, pady=10)

    selected_experts = Label(frame, width=20, font=FONT)
    selected_experts.grid(row=2, column=0, columnspan=3, padx=10, pady=1)
    selected_criteria = Label(frame, width=20, font=FONT)
    selected_criteria.grid(row=3, column=0, columnspan=3, padx=10, pady=1)
    selected_subcriteria = Label(frame, width=20, font=FONT)
    selected_subcriteria.grid(row=4, column=0, columnspan=3, padx=10, pady=1)

    expert_chosen = ""
    criteria_chosen = ""
    subcriteria_chosen = ""
    chosen_options = False

    def show_selected(event):
        nonlocal expert_chosen, criteria_chosen, subcriteria_chosen, chosen_options

        selected_indices = experts_listbox.curselection()
        if len(selected_indices) > 0:
            expert_chosen = experts_listbox.get(selected_indices[0])

        selected_indices = criteria_listbox.curselection()
        if len(selected_indices) > 0:
            criteria_chosen = criteria_listbox.get(selected_indices[0])

            subcriteria_listbox.delete(0, "end")
            if subcriteria[selected_indices[0]] == "":
                subcriteria_listbox.insert("end", criteria_chosen)
            else:
                for sub in subcriteria[selected_indices[0]]:
                    subcriteria_listbox.insert("end", sub)

        selected_indices = subcriteria_listbox.curselection()
        if len(selected_indices) > 0:
            subcriteria_chosen = subcriteria_listbox.get(selected_indices[0])

        if expert_chosen != "" and criteria_chosen != "" and subcriteria_chosen != "":
            chosen_options = True

        selected_experts.config(text=expert_chosen)
        selected_criteria.config(text=criteria_chosen)
        selected_subcriteria.config(text=subcriteria_chosen)

    experts_listbox.bind('<<ListboxSelect>>', show_selected)
    criteria_listbox.bind('<<ListboxSelect>>', show_selected)
    subcriteria_listbox.bind('<<ListboxSelect>>', show_selected)

    def show_matrix():
        if not chosen_options:
            showinfo(title='Missing data', message="First you need to choice all the options from lists!")
        else:
            nonlocal subcriteria_chosen
            weight_name_entry = Entry(preview_frame, fg='blue', font=('Arial', 16, 'bold'), width=10)
            weight_name_entry.grid(row=0, column=0)
            weight_name_entry.insert("end", "Weight of the " + str(subcriteria_chosen) + ": ")
            weight_name_entry.config(state=DISABLED)
            weight_entry = Entry(preview_frame, fg='blue', font=('Arial', 16, 'bold'), width=10)
            weight_entry.grid(row=0, column=1)
            weight_name_entry.insert("end", "5")

            countries = ("Poland", "Spain", "USA", "Germany", "Russia")
            matrix = [[""]]
            for c in countries:
                matrix[0].append(c)
            for c in countries:
                tmp = [c]
                for _ in countries:
                    tmp.append(0)
                matrix.append(tmp)
            Table(preview_frame, matrix)

            def save():
                # TODO zapisywanie zmian
                pass

            save_button = Button(preview_frame, text="Save", font=FONT, command=save)
            save_button.grid(row=len(countries) + 1, columnspan=len(countries) + 1, pady=10, padx=10)

    matrix_button = Button(frame, text="Show matrix", font=FONT, command=show_matrix)
    matrix_button.grid(row=5, columnspan=3, pady=10, padx=10)

    def _return():
        root.deiconify()
        preview_window.destroy()

    return_button = Button(frame, text="Return", font=FONT, command=_return)
    return_button.grid(sticky=S, columnspan=3, pady=10, padx=10)


preview_button = Button(main_window, text="Show experts' opinions", font=FONT, command=preview)
preview_button.grid(row=row_no, columnspan=5, pady=10, padx=10)


#####################################           SOLVE           #####################################


def solve():
    global missing_data
    if missing_data:
        showinfo(title='Missing data', message="First you need fill all the necessary opinions!\n"
                                               "You can do it in \"Show experts' opinions\" section.")
    else:
        label = Label(main_window, text="Clicked")
        label.grid(sticky=S, columnspan=5, pady=10, padx=10)

        results = Toplevel()
        results.title("Ranking")
        results.geometry("400x800")
        # "1024x576"
        results.resizable(False, False)

        frame = Frame(results, bg="light grey", pady=10, padx=10)
        # frame.config(anchor=CENTER)
        # frame.pack(fill=BOTH, expand=True)
        frame.grid(sticky=SE, padx=5, pady=5)

        labels = []

        # TODO tutaj zaciągnąć z DB
        fake_ranking = [("first", 0.6), ("second", 0.2), ("third", 0.15), ("fourth", 0.05), ("second", 0.2),
                        ("third", 0.15), ("fourth", 0.05), ("second", 0.2), ("third", 0.15), ("fourth", 0.05)]
        top = fake_ranking[0][1]
        bottom = fake_ranking[-1][1]
        multi = 100 / top
        for country in fake_ranking:
            label_tmp = Label(frame, text=country[0], font=("Arial", round(country[1] * multi)))
            label_tmp.grid(sticky=S)
            # label_tmp.config(anchor=CENTER)
            labels.append(label_tmp)


buttonSolve = Button(main_window, text="Solve", font=("Arial", 30), command=solve, bg="blue", fg="pink", width=20)
buttonSolve.grid(sticky=S, columnspan=5, pady=10, padx=10)

main_window.mainloop()
