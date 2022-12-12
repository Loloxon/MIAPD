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


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def init(db):
    db.add_expert('expert1')
    db.add_country('country1')
    db.add_country('country3')
    db.add_country('country2')
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

    array = np.array([[1, 7, 8],
                      [1 / 7, 1, 3],
                      [1 / 8, 1 / 3, 1]])
    matrix = "cost"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 7 / 5, 4 / 9, 4 / 5],
         [5 / 7, 1, 6 / 7, 7 / 6],
         [9 / 4, 7 / 6, 1, 3 / 2],
         [5 / 4, 6 / 7, 2 / 3, 1]])
    matrix = "purchase"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 7 / 3, 9 / 5, 2],
                      [3 / 7, 1, 8 / 5, 8 / 5],
                      [5 / 9, 5 / 8, 1, 2],
                      [1 / 2, 5 / 8, 1 / 2, 1]])
    matrix = "fuel"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 7 / 5, 4 / 3, 5 / 9],
         [5 / 7, 1, 2, 6 / 5],
         [3 / 4, 1 / 2, 1, 3 / 2],
         [9 / 5, 5 / 6, 2 / 3, 1]])
    matrix = "maintenance"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 2 / 5, 1 / 9, 1 / 7],
                      [2 / 5, 1, 1 / 9, 1 / 4],
                      [9, 9, 1, 5],
                      [7, 4, 1 / 5, 1]])
    matrix = "safety"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 1 / 9, 1 / 9, 1 / 9],
                      [9, 1, 5, 9 / 8],
                      [9, 1 / 5, 1, 7 / 9],
                      [9, 8 / 9, 9 / 7, 1]])
    matrix = "design"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 3],
                      [1 / 3, 1]])
    matrix = "capacity"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 6 / 5, 2 / 3, 5 / 2],
         [5 / 6, 1, 5 / 9, 7 / 5],
         [3 / 2, 9 / 5, 1, 1],
         [2 / 5, 5 / 7, 1, 1]])
    matrix = "trunk"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 9, 9, 3 / 8],
                      [1 / 9, 1, 2 / 3, 1 / 9],
                      [1 / 9, 3 / 2, 1, 1 / 9],
                      [8 / 3, 9, 9, 1]])
    matrix = "passenger"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 9, 4 / 3, 7 / 5],
                      [1 / 9, 1, 1 / 9, 1 / 9],
                      [3 / 4, 9, 1, 1 / 2],
                      [5 / 7, 9, 2, 1]])
    matrix = "warranty"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 7 / 5, 5, 9 / 5, 8],
                      [5 / 7, 1, 9 / 5, 7 / 5, 5 / 4],
                      [1 / 5, 5 / 9, 1, 3 / 7, 3 / 4],
                      [5 / 9, 5 / 7, 7 / 3, 1, 7 / 9],
                      [1 / 8, 4 / 5, 4 / 3, 9 / 7, 1]])
    matrix = "categories"
    expert = "expert1"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])


init(db)

# print(db.matrices)
# ahp = AHP(db)
# rank = ahp.calculate_ranking()
# print(db.subcategories_map)
# print(rank)

#####################################           COUNTRY           #####################################

column_no = 0
row_no = 1
country_no = 0

def add_country(entry):
    global country_no
    if entry.get() in db.countries:
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
add_country_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=5)
add_country_button = Button(main_window, text="Add new country", font=FONT,
                            command=lambda: add_country(add_country_entry))
add_country_button.grid(row=row_no + 2, column=column_no)

#####################################           CRITERION           #####################################

column_no = 1
row_no = 1
category_no = 0


def add_category(entry):
    global category_no
    if entry.get() in db.categories:
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
add_category_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=5)
add_category_button = Button(main_window, text="Add new category", font=FONT,
                             command=lambda: add_category(add_category_entry))
add_category_button.grid(row=row_no + 2, column=column_no, padx=50)

#####################################           EXPERT           #####################################

column_no = 2
row_no = 1
expert_no = 0


def add_expert(entry):
    global expert_no
    if entry.get() in db.experts:
        showinfo(title='Invalid name!', message="Given name already exists in the database!")
    else:
        db.add_expert(entry.get())

        root.withdraw()
        new_expert_window = Toplevel()
        new_expert_window.title("Opinions")
        new_expert_window.geometry("720x480")
        # "1024x576"
        new_expert_window.resizable(False, False)

        frame = Frame(new_expert_window, bg="light grey", pady=10, padx=10)
        frame.grid(row=0, column=0, padx=5, pady=5)

        # key = subcategories_chosen
        all_labels = []
        # labels = list(db.countries_map.keys())

        countries = db.countries
        sub = []
        for category in db.categories:
            if len(db.subcategories_map.get(category)) > 0:
                for subcategory in db.subcategories_map.get(category):
                    sub.append([category, subcategory])
                sub.append([category, category])
                # przechodze przez wszystkie podkategorie i porownuje kraje
                # na koncu powordnuje podkategorie
            else:
                sub.append([category])
                # porownuje kraje

        labels = []
        names = []
        for s in sub:
            if len(s) == 2:
                if s[0] != s[1]:
                    labels.append("Comparison for " + str(s[1]) + " from " + str(s[0]))
                    names.append(countries)
                    # #dla s[0] _ s[1]
                else:
                    labels.append("Comparison for weights within " + str(s[0]))
                    names.append(db.subcategories_map.get(s[0]))
                    # #dla s[0] wagi podkategorii
            else:
                labels.append("Comparison for " + str(s[0]))
                names.append(countries)
                # # dla s[0]

        idx = 0
        e_label = Entry(frame, fg='black', font=FONT, width=50, justify=CENTER)
        e_label.grid(row=0, column=0, columnspan=4)
        e_label.config(state=DISABLED)
        e1 = Entry(frame, fg='black', font=FONT, width=20, justify=CENTER)
        e1.grid(row=1, column=0)
        e1.config(state=DISABLED)
        s1 = Scale(frame, from_=9, to=1, width=25)
        s1.grid(row=1, column=1, padx=5)
        s2 = Scale(frame, from_=9, to=1, width=25)
        s2.grid(row=1, column=2, padx=5)
        e2 = Entry(frame, fg='black', font=FONT, width=20, justify=CENTER)
        e2.grid(row=1, column=3)
        e2.config(state=DISABLED)

        previous_idx1 = -1
        previous_idx2 = -1

        expert_chosen = "idk"
        category_chosen = "idk"
        subcategories_chosen = "idk"

        def _next():
            nonlocal idx, names, labels, e_label, e1, e2, s1, s2, previous_idx1, previous_idx2, expert_chosen, \
                category_chosen, subcategories_chosen
            finishing = True
            _break = False

            if idx > 0:
                # print(previous_idx1, "to", previous_idx2, s1.get() / s2.get(), "for", expert_chosen,
                #       category_chosen, subcategories_chosen)

                true_category = category_chosen
                if subcategories_chosen != NO_SUBCATEGORY:
                    true_category = subcategories_chosen
                # print(true_category, expert_chosen, previous_idx1, previous_idx2, s1.get() / s2.get())
                db.set_matrix_field(true_category, expert_chosen, previous_idx2, previous_idx1, s1.get() / s2.get())

            idx_copy = idx
            for idx1 in range(len(names)):
                for idx2 in range(idx1 + 1, len(names)):
                    if idx_copy == 0:
                        idx += 1
                        finishing = False
                        current_name1 = names[idx1]
                        current_name2 = names[idx2]
                        previous_idx1 = idx1
                        previous_idx2 = idx2
                        _break = True
                    if _break:
                        break
                    idx_copy -= 1
                if _break:
                    break

            if finishing:
                showinfo(title='Comparing done', message="All pairs for this category have been compared!\n"
                                                         "Saving opinions.")
                save()
            else:
                e_label.config(state=NORMAL)
                e_label.delete(0, "end")
                e_label.insert(0, labels)
                e_label.config(state=DISABLED)

                e1.config(state=NORMAL)
                e1.delete(0, "end")
                e1.insert(0, current_name1)
                e1.config(state=DISABLED)

                e2.config(state=NORMAL)
                e2.delete(0, "end")
                e2.insert(0, current_name2)
                e2.config(state=DISABLED)

        # TODO dodawanie do database
        _next()

        next_button = Button(frame, text="Next", font=FONT, command=next)
        next_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        def save():
            # TODO zapisywanie zmian
            root.deiconify()
            new_expert_window.destroy()
            pass

        save_button = Button(frame, text="Save and return", font=FONT, command=save)
        save_button.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

    expert_no += 1
    entry.delete(0, "end")
    entry.insert(0, "Unknown Expert " + str(expert_no))


add_expert_label = Label(main_window, text="Enter the expert name", font=LABEL_FONT)
add_expert_label.grid(row=row_no, column=column_no)
add_expert_entry = Entry(main_window, width=20, font=FONT)
add_expert_entry.insert(0, "Unknown Expert 0")
add_expert_entry.grid(row=row_no + 1, column=column_no, padx=10, pady=5)
add_expert_button = Button(main_window, text="Add new expert", font=FONT,
                           command=lambda: add_expert(add_expert_entry))
add_expert_button.grid(row=row_no + 2, column=column_no, padx=50)

#####################################           EXPERTS' PREVIEW           #####################################

column_no = 3
row_no = 4


def preview():
    root.withdraw()
    preview_window = Toplevel()
    preview_window.title("Opinions")
    preview_window.geometry("1600x900")
    # "1024x576"
    preview_window.resizable(False, False)

    frame = Frame(preview_window, bg="light grey", pady=10, padx=10)
    frame.grid(row=0, column=0, padx=15, pady=15)

    preview_frame = Frame(preview_window, bg="light grey", pady=10, padx=10)
    preview_frame.grid(row=0, column=1, padx=5, pady=5)

    missing_data = db.is_missing_data()

    experts = db.experts
    experts_listbox = Listbox(frame, listvariable=Variable(value=experts), height=len(experts))
    experts_listbox.grid(row=0, column=0, padx=10, pady=10)

    categories = db.categories
    categories_listbox = Listbox(frame, listvariable=Variable(value=categories), height=len(categories))
    categories_listbox.grid(row=0, column=1, padx=10, pady=10)

    subcategories = list(db.subcategories_map.values())
    for sc in subcategories:
        sc.insert(0, NO_SUBCATEGORY)

    subcategories_listbox = Listbox(frame, listvariable=Variable(value=subcategories[0]), height=len(subcategories[0]))
    subcategories_listbox.grid(row=0, column=2, padx=10, pady=10)

    for i in range(len(experts)):
        for expert, _ in missing_data:
            if experts[i] == expert:
                experts_listbox.itemconfig(i, {'bg': 'red'})
    for i in range(len(categories)):
        for expert, category in missing_data:
            if expert == missing_data[0][0] and categories[i] in category:
                categories_listbox.itemconfig(i, {'bg': 'red'})
    # for i in range(len(subcategories[0])):
    #     for expert, subcategory in missing_data:
    #         if expert == missing_data[0][0] and categories[i] in subcategory:
    #             categories_listbox.itemconfig(i, {'bg': 'red'})

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
        missing_data = db.is_missing_data()

        selected_indices = experts_listbox.curselection()
        if len(selected_indices) > 0:
            expert_chosen = experts_listbox.get(selected_indices[0])

        selected_indices = categories_listbox.curselection()
        category_chosen_no = 0
        if len(selected_indices) > 0:
            category_chosen_no = selected_indices[0]
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

        for i in range(len(experts)):
            for expert, _ in missing_data:
                if experts[i] == expert_chosen:
                    experts_listbox.itemconfig(i, {'bg': 'red'})
        for i in range(len(categories)):
            for expert, category in missing_data:
                if expert == expert_chosen:
                    print(expert, category)
                    if categories[i] in category:
                        categories_listbox.itemconfig(i, {'bg': 'red'})
                    else:
                        categories_listbox.itemconfig(i, {'bg': 'white'})

        # for i in range(len(subcategories[category_chosen_no])):
        #     for expert, subcategory in missing_data:
        #         if expert == expert_chosen and subcategories[category_chosen_no][i] in subcategory:
        #             subcategories_listbox.itemconfig(i, {'bg': 'red'})

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

            key = subcategories_chosen
            labels = db.countries
            if subcategories_chosen == NO_SUBCATEGORY:
                key = category_chosen
                if len(db.subcategories_map.get(category_chosen)) > 0:
                    labels = list(db.subcategories_map.get(category_chosen))
            matrix = db.get_matrix(key, expert_chosen)
            Table(preview_frame, matrix, labels)

            def save():
                values = []
                for widget in preview_frame.winfo_children():
                    if isinstance(widget, Entry):
                        values.append(widget.get())
                        print(widget.get())

                mod = len(db.countries)
                values = values[mod*2:]
                for v in values:
                    if not isfloat(v) or float(v) <= 0 or float(v) > 9:
                        print(not isfloat(v))
                        # print(float(values[v]))
                        print(v)

                        showinfo(title='Invalid data!',
                                 message="Values need to be float type in range <0,9]")
                        return


                true_category = category_chosen
                if subcategories_chosen != NO_SUBCATEGORY:
                    true_category = subcategories_chosen
                print(values)
                for v in range(len(values)):
                    if v // mod < v % mod:
                        db.set_matrix_field(true_category, expert_chosen, v // mod, v % mod, float(values[v]))

                # TODO zapisywanie zmian
                for widget in preview_frame.winfo_children():
                    widget.destroy()
                pass

            save_button = Button(preview_frame, text="Save", font=FONT, command=save)
            save_button.grid(row=len(labels) + 1, columnspan=len(labels) + 1, pady=10, padx=10)

    def add_opinion():
        nonlocal expert_chosen, category_chosen, subcategories_chosen

        def missing_data(expert_chosen, category_chosen, subcategories_chosen):
            for missing_expert, missing_categories in db.is_missing_data():
                if missing_expert == expert_chosen and (category_chosen in missing_categories or
                                                        subcategories_chosen in missing_categories):
                    return True
            return False

        if not chosen_options:
            showinfo(title='Missing data', message="First you need to choice all the options from lists!")
        elif not missing_data(expert_chosen, category_chosen, subcategories_chosen):
            showinfo(title='All opinions given', message="No need to add more opinions as all of them have been "
                                                         "already given.")
        else:
            for widget in preview_frame.winfo_children():
                widget.destroy()

            names = db.countries
            print(names)
            label = ""

            if subcategories_chosen == NO_SUBCATEGORY:
                # key = category_chosen
                if len(db.subcategories_map.get(category_chosen)) > 0:
                    names = list(db.subcategories_map.get(category_chosen))
                    label = "Comparison " + expert_chosen + " for weights within " + category_chosen
                else:
                    label = "Comparison " + expert_chosen + " for " + category_chosen
            else:
                label = "Comparison " + expert_chosen + " for " + subcategories_chosen + " from " + category_chosen

            idx = 0
            e_label = Entry(preview_frame, fg='black', font=FONT, width=50, justify=CENTER)
            e_label.grid(row=0, column=0, columnspan=4)
            e_label.config(state=DISABLED)
            e1 = Entry(preview_frame, fg='black', font=FONT, width=20, justify=CENTER)
            e1.grid(row=1, column=0)
            e1.config(state=DISABLED)
            s1 = Scale(preview_frame, from_=9, to=1, width=25)
            s1.grid(row=1, column=1, padx=5)
            s2 = Scale(preview_frame, from_=9, to=1, width=25)
            s2.grid(row=1, column=2, padx=5)
            e2 = Entry(preview_frame, fg='black', font=FONT, width=20, justify=CENTER)
            e2.grid(row=1, column=3)
            e2.config(state=DISABLED)

            previous_idx1 = -1
            previous_idx2 = -1

            def _next():
                nonlocal idx, names, label, e_label, e1, e2, s1, s2, previous_idx1, previous_idx2, expert_chosen, \
                    category_chosen, subcategories_chosen
                finishing = True
                _break = False

                if idx > 0:
                    # print(previous_idx1, "to", previous_idx2, s1.get() / s2.get(), "for", expert_chosen,
                    #       category_chosen, subcategories_chosen)

                    true_category = category_chosen
                    if subcategories_chosen != NO_SUBCATEGORY:
                        true_category = subcategories_chosen
                    # print(true_category, expert_chosen, previous_idx1, previous_idx2, s1.get() / s2.get())
                    db.set_matrix_field(true_category, expert_chosen, previous_idx2, previous_idx1, s1.get() / s2.get())

                idx_copy = idx
                for idx1 in range(len(names)):
                    for idx2 in range(idx1 + 1, len(names)):
                        if idx_copy == 0:
                            idx += 1
                            finishing = False
                            current_name1 = names[idx1]
                            current_name2 = names[idx2]
                            previous_idx1 = idx1
                            previous_idx2 = idx2
                            _break = True
                        if _break:
                            break
                        idx_copy -= 1
                    if _break:
                        break

                if finishing:
                    showinfo(title='Comparing done', message="All pairs for this category have been compared!\n"
                                                             "Saving opinions.")
                    save()
                else:
                    e_label.config(state=NORMAL)
                    e_label.delete(0, "end")
                    e_label.insert(0, label)
                    e_label.config(state=DISABLED)

                    e1.config(state=NORMAL)
                    e1.delete(0, "end")
                    e1.insert(0, current_name1)
                    e1.config(state=DISABLED)

                    e2.config(state=NORMAL)
                    e2.delete(0, "end")
                    e2.insert(0, current_name2)
                    e2.config(state=DISABLED)

            # TODO dodawanie do database
            _next()

            next_button = Button(preview_frame, text="Next", font=FONT, command=_next)
            next_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

            def save():
                # TODO zapisywanie zmian
                for widget in preview_frame.winfo_children():
                    widget.destroy()
                pass

            save_button = Button(preview_frame, text="Save", font=FONT, command=save)
            save_button.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

    matrix_button = Button(frame, text="Show matrix", font=FONT, command=show_matrix)
    matrix_button.grid(row=5, column=0, pady=10, padx=10)
    add_opinion_button = Button(frame, text="Edit expert's opinions", font=FONT, command=add_opinion)
    add_opinion_button.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

    def _return():
        root.deiconify()
        preview_window.destroy()

    return_button = Button(frame, text="Return", font=FONT, command=_return)
    return_button.grid(sticky=S, columnspan=3, pady=10, padx=10)


preview_button = Button(main_window, text="Show\nexperts'\nopinions", font=FONT, command=preview, width=14, height=7)
preview_button.grid(column=column_no, row=0, rowspan=row_no, pady=10, padx=10)


#####################################           SOLVE           #####################################


def solve():
    if db.is_missing_data():
        print(db.is_missing_data())
        showinfo(title='Missing data', message="First you need fill all the necessary opinions!\n"
                                               "You can do it in \"Show experts' opinions\" section.")
    else:
        label = Label(main_window, text="Clicked")
        label.grid(sticky=S, columnspan=5, pady=10, padx=10)

        results = Toplevel()
        results.title("Ranking")
        results.geometry("1600x800")
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
            label_tmp = Label(frame, text=country[0] + ": " + str(round(country[1] * 100, 2)) + "%",
                              font=("Arial", round(country[1] * multi)))
            label_tmp.grid(sticky=S)
            labels.append(label_tmp)


buttonSolve = Button(main_window, text="Solve", font=("Arial", 26), command=solve, bg="blue", fg="pink", width=40)
buttonSolve.grid(row=0, sticky=N, columnspan=3, pady=10, padx=10)

main_window.mainloop()
