from tkinter import *
from tkinter.messagebox import showinfo

import numpy as np

from Project.backend.AHP import AHP
from Project.gui.Table import Table
from Project.resources.DataBase import DataBase

FONT = ("Arial", 20)
LABEL_FONT = ("Arial", 15)
NO_SUBCATEGORY = "<no subcategory>"

root = Tk()
root.title("Comparing App")
root.geometry("1280x720")
root.resizable(False, False)

main_window = Frame(root, relief='sunken')
main_window.pack(fill=BOTH, expand=True, padx=10, pady=10)

db = DataBase()


def init(db):
    db.add_expert('expert1')
    db.add_country('country1')
    db.add_country('country2')
    db.add_country('country3')
    db.add_country('country4')

    db.add_category('cost')
    db.add_subcategory('cost', 'purchase')
    db.add_subcategory('cost', 'fuel')
    db.add_subcategory('cost', 'maintenance')
    db.add_category('safety')
    db.add_category('design')
    db.add_subcategory('capacity', 'trunk')
    db.add_subcategory('capacity', 'passenger')
    db.add_category('warranty')

    db.generate_matrices()

    db.set_matrix('cost', 'expert1', np.array([[1, 7, 8], [1 / 7, 1, 3], [1 / 8, 1 / 3, 1]]))
    db.set_matrix('purchase', 'expert1', np.array(
        [[1, 7 / 5, 4 / 9, 4 / 5], [5 / 7, 1, 6 / 7, 7 / 6], [9 / 4, 7 / 6, 1, 3 / 2], [5 / 4, 6 / 7, 2 / 3, 1]]))
    db.set_matrix('fuel', 'expert1', np.array(
        [[1, 7 / 3, 9 / 5, 2], [3 / 7, 1, 8 / 5, 8 / 5], [5 / 9, 5 / 8, 1, 2], [1 / 2, 5 / 8, 1 / 2, 1]]))
    db.set_matrix('maintenance', 'expert1', np.array(
        [[1, 7 / 5, 4 / 3, 5 / 9], [5 / 7, 1, 2, 6 / 5], [3 / 4, 1 / 2, 1, 3 / 2], [9 / 5, 5 / 6, 2 / 3, 1]]))

    db.set_matrix('safety', 'expert1',
                  np.array([[1, 2 / 5, 1 / 9, 1 / 7], [2 / 5, 1, 1 / 9, 1 / 4], [9, 9, 1, 5], [7, 4, 1 / 5, 1]]))

    db.set_matrix('design', 'expert1',
                  np.array([[1, 1 / 9, 1 / 9, 1 / 9], [9, 1, 5, 9 / 8], [9, 1 / 5, 1, 7 / 9], [9, 8 / 9, 9 / 7, 1]]))

    db.set_matrix('capacity', 'expert1', np.array([[1, 3], [1 / 3, 1]]))
    db.set_matrix('trunk', 'expert1', np.array(
        [[1, 6 / 5, 2 / 3, 5 / 2], [5 / 6, 1, 5 / 9, 7 / 5], [3 / 2, 9 / 5, 1, 1], [2 / 5, 5 / 7, 1, 1]]))
    db.set_matrix('passenger', 'expert1',
                  np.array([[1, 9, 9, 3 / 8], [1 / 9, 1, 2 / 3, 1 / 9], [1 / 9, 3 / 2, 1, 1 / 9], [8 / 3, 9, 9, 1]]))

    db.set_matrix('warranty', 'expert1',
                  np.array([[1, 9, 4 / 3, 7 / 5], [1 / 9, 1, 1 / 9, 1 / 9], [3 / 4, 9, 1, 1 / 2], [5 / 7, 9, 2, 1]]))

    db.set_matrix('categories', 'expert1', np.array(
        [[1, 7 / 5, 5, 9 / 5, 8], [5 / 7, 1, 9 / 5, 7 / 5, 5 / 4], [1 / 5, 5 / 9, 1, 3 / 7, 3 / 4],
         [5 / 9, 5 / 7, 7 / 3, 1, 7 / 9], [1 / 8, 4 / 5, 4 / 3, 9 / 7, 1]]))


init(db)

# print(db.matrices)
# ahp = AHP(db)
# rank = ahp.calculate_ranking()
# print(db.subcategories_map)
# print(rank)

#####################################           COUNTRY           #####################################

column_no = 0
row_no = 0
country_no = 0


def add_country(entry):
    global country_no
    if entry.get() in db.countries_map:
        showinfo(title='Invalid name!', message="Given country already exists in the database!")
    else:
        db.add_country(entry.get())
    db.generate_matrices()
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
category_no = 0


def add_category(entry):
    global category_no
    if entry.get() in db.categories_map:
        showinfo(title='Invalid name!', message="Given category already exists in the database!")
    else:
        db.add_category(entry.get())
    category_no += 1
    entry.delete(0, "end")
    entry.insert(0, "Unknown Criterion " + str(category_no))


add_category_label = Label(main_window, text="Enter the category", font=LABEL_FONT)
add_category_label.grid(row=row_no + 0, column=column_no)
add_category_entry = Entry(main_window, width=20, font=FONT)
add_category_entry.insert(0, "Unknown Criterion 0")
add_category_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=10)
add_category_button = Button(main_window, text="Add new category", font=FONT,
                             command=lambda: add_category(add_category_entry))
add_category_button.grid(row=row_no + 2, column=column_no, padx=50)

#####################################           EXPERT           #####################################

column_no = 2
row_no = 0
expert_no = 0


def add_expert(entry):
    global expert_no
    if entry.get() in db.experts_map:
        showinfo(title='Invalid name!', message="Given name already exists in the database!")
    else:
        db.add_expert(entry.get())
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

    experts = list(db.experts_map.keys())
    experts_listbox = Listbox(frame, listvariable=Variable(value=experts), height=len(experts))
    experts_listbox.grid(row=0, column=0, padx=10, pady=10)
    # experts_listbox.itemconfig(1, {'bg': 'red'})

    categories = list(db.categories_map.keys())
    categories_listbox = Listbox(frame, listvariable=Variable(value=categories), height=len(categories))
    categories_listbox.grid(row=0, column=1, padx=10, pady=10)

    subcategories = list(db.subcategories_map.values())
    for sc in subcategories:
        sc.insert(0, NO_SUBCATEGORY)

    subcategories_listbox = Listbox(frame, listvariable=Variable(value=subcategories[0]), height=len(subcategories[0]))
    subcategories_listbox.grid(row=0, column=2, padx=10, pady=10)

    selected_experts = Label(frame, width=20, font=FONT)
    selected_experts.grid(row=2, column=0, columnspan=3, padx=10, pady=1)
    selected_categories = Label(frame, width=20, font=FONT)
    selected_categories.grid(row=3, column=0, columnspan=3, padx=10, pady=1)
    selected_subcategories = Label(frame, width=20, font=FONT)
    selected_subcategories.grid(row=4, column=0, columnspan=3, padx=10, pady=1)

    expert_chosen = ""
    category_chosen = ""
    subcategories_chosen = ""
    chosen_options = False

    def show_selected(event):
        nonlocal expert_chosen, category_chosen, subcategories_chosen, chosen_options

        selected_indices = experts_listbox.curselection()
        if len(selected_indices) > 0:
            expert_chosen = experts_listbox.get(selected_indices[0])

        selected_indices = categories_listbox.curselection()
        if len(selected_indices) > 0:
            category_chosen = categories_listbox.get(selected_indices[0])

            subcategories_listbox.delete(0, "end")
            if subcategories[selected_indices[0]] == "":
                subcategories_listbox.insert("end", category_chosen)
            else:
                for sub in subcategories[selected_indices[0]]:
                    subcategories_listbox.insert("end", sub)

        selected_indices = subcategories_listbox.curselection()
        if len(selected_indices) > 0:
            subcategories_chosen = subcategories_listbox.get(selected_indices[0])

        if expert_chosen != "" and category_chosen != "" and subcategories_chosen != "":
            chosen_options = True

        selected_experts.config(text=expert_chosen)
        selected_categories.config(text=category_chosen)
        selected_subcategories.config(text=subcategories_chosen)

    experts_listbox.bind('<<ListboxSelect>>', show_selected)
    categories_listbox.bind('<<ListboxSelect>>', show_selected)
    subcategories_listbox.bind('<<ListboxSelect>>', show_selected)

    def show_matrix():
        if not chosen_options:
            showinfo(title='Missing data', message="First you need to choice all the options from lists!")
        else:
            nonlocal expert_chosen, category_chosen, subcategories_chosen
            # weight_name_entry = Entry(preview_frame, fg='blue', font=('Arial', 16, 'bold'), width=10)
            # weight_name_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
            # weight_name_entry.insert("end", "Weight of the " + str(subcategories_chosen) + ": ")
            # weight_name_entry.config(state=DISABLED)
            # weight_entry = Entry(preview_frame, fg='blue', font=('Arial', 16, 'bold'), width=10)
            # weight_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
            # weight_name_entry.insert("end", "5")
            for widget in preview_frame.winfo_children():
                widget.destroy()

            countries = list(db.countries_map.keys())
            key = subcategories_chosen
            labels = list(db.countries_map.keys())
            if subcategories_chosen == NO_SUBCATEGORY:
                key = category_chosen
                if len(db.subcategories_map.get(category_chosen)) > 0:
                    labels = list(db.subcategories_map.get(category_chosen))
            matrix = db.get_matrix(key, expert_chosen)
            Table(preview_frame, matrix, labels)

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
    if db.is_missing_data():
        showinfo(title='Missing data', message="First you need fill all the necessary opinions!\n"
                                               "You can do it in \"Show experts' opinions\" section.")
    else:
        label = Label(main_window, text="Clicked")
        label.grid(sticky=S, columnspan=5, pady=10, padx=10)

        results = Toplevel()
        results.title("Ranking")
        results.geometry("800x800")
        # "1024x576"
        results.resizable(False, False)

        frame = Frame(results, bg="light grey", pady=10, padx=10)
        # frame.config(anchor=CENTER)
        # frame.pack(fill=BOTH, expand=True)
        frame.grid(sticky=SE, padx=5, pady=5)

        labels = []

        ahp = AHP(db)
        rank = ahp.calculate_ranking()

        ranking = []
        for i in range(len(rank[0])):
            ranking.append((rank[0][i], rank[1][i]))

        # TODO ewentualnie jakieś bajery do wyświetlania
        top = ranking[0][1]
        multi = 100 / top
        for country in ranking:
            label_tmp = Label(frame, text=country[0], font=("Arial", round(country[1] * multi)))
            label_tmp.grid(sticky=S)
            labels.append(label_tmp)


buttonSolve = Button(main_window, text="Solve", font=("Arial", 30), command=solve, bg="blue", fg="pink", width=20)
buttonSolve.grid(sticky=S, columnspan=5, pady=10, padx=10)

main_window.mainloop()
