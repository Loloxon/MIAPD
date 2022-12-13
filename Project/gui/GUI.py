from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText

from Project.backend.AHP import AHP
from Project.gui.Table import Table

column_no = 0
row_no = 1
country_no = 0



class GUI:
    def __init__(self, data_base):
        self.FONT = ("Arial", 20)
        self.LABEL_FONT = ("Arial", 15)
        self.NO_SUBCATEGORY = "<no subcategory>"
        self.NO_CATEGORY = "<no category>"

        self.root = Tk()
        self.root.title("Comparing App")
        self.root.geometry("1600x900")
        self.root.resizable(False, False)

        main_window = Frame(self.root, relief='sunken')
        main_window.pack(fill=BOTH, expand=True, padx=100, pady=10)

        self.db = data_base
        self.ahp = AHP(self.db)

        self.country_no = 0
        self.category_no = 0
        self.expert_no = 0

        self.create_country_part(main_window, 0, 1)
        self.create_category_part(main_window, 1, 1)
        self.create_expert_part(main_window, 2, 1)
        self.create_preview_button(main_window, 3, 4)
        self.create_solve_button(main_window, 3, 0)

        main_window.mainloop()

    def create_country_part(self, root, column_no, row_no):
        country_list = ScrolledText(root, font=self.FONT, width=20, height=18)
        for country in self.db.countries:
            country_list.insert("end", "● " + country + "\n")
        country_list.config(state=DISABLED)
        country_list.grid(row=row_no + 3, sticky=N, column=column_no, padx=15, pady=5)

        def add_country(entry):
            if entry.get() in self.db.countries:
                showinfo(title='Invalid name!', message="Given country already exists in the database!")
            else:
                self.db.add_country(entry.get())
                country_list.config(state=NORMAL)
                country_list.insert("end", "● " + entry.get() + "\n")
                country_list.config(state=DISABLED)
            self.db.generate_matrices()
            self.country_no += 1
            entry.delete(0, "end")
            entry.insert(0, "Unknown Country " + str(self.country_no))

        add_country_label = Label(root, text="Enter new country", font=self.LABEL_FONT)
        add_country_label.grid(row=row_no + 0, column=column_no)
        add_country_entry = Entry(root, width=20, font=self.FONT, bd=1)
        add_country_entry.insert(0, "Unknown Country 0")
        add_country_entry.grid(row=row_no + 1, column=column_no, padx=15, pady=5)
        add_country_button = Button(root, text="Add new country", font=self.FONT,
                                    command=lambda: add_country(add_country_entry))
        add_country_button.grid(row=row_no + 2, column=column_no)

    def create_category_part(self, root, column_no, row_no):
        category_list = ScrolledText(root, font=self.FONT, width=20, height=18)
        for category in self.db.categories:
            category_list.insert("end", "● " + category + "\n")
            for subcategory in self.db.subcategories_map.get(category):
                category_list.insert("end", "   - " + subcategory + "\n")
        category_list.config(state=DISABLED)
        category_list.grid(row=row_no + 3, sticky=N, column=column_no, padx=15, pady=5)

        def add_category(entry):
            if entry.get() in self.db.categories:
                showinfo(title='Invalid name!', message="Given category already exists in the database!")
            else:
                self.db.add_category(entry.get())
                category_list.config(state=NORMAL)
                category_list.insert("end", "● " + entry.get() + "\n")
                category_list.config(state=DISABLED)
                for subcategory in self.db.subcategories_map.get(entry.get()):
                    category_list.config(state=NORMAL)
                    category_list.insert("end", " - " + subcategory + "\n")
                    category_list.config(state=DISABLED)
            self.category_no += 1
            entry.delete(0, "end")
            entry.insert(0, "Unknown Criterion " + str(self.category_no))

        add_category_label = Label(root, text="Enter new category", font=self.LABEL_FONT)
        add_category_label.grid(row=row_no + 0, column=column_no)
        add_category_entry = Entry(root, width=20, font=self.FONT)
        add_category_entry.insert(0, "Unknown Criterion 0")
        add_category_entry.grid(row=row_no + 1, column=column_no, padx=15, pady=5)
        add_category_button = Button(root, text="Add new category", font=self.FONT,
                                     command=lambda: add_category(add_category_entry))
        add_category_button.grid(row=row_no + 2, column=column_no, padx=50)

    def create_expert_part(self, root, column_no, row_no):
        expert_list = ScrolledText(root, font=self.FONT, width=20, height=18)
        for category in self.db.experts:
            expert_list.insert("end", "● " + category + "\n")
        expert_list.config(state=DISABLED)
        expert_list.grid(row=row_no + 3, sticky=N, column=column_no, padx=15, pady=5)

        def add_expert(entry):
            if entry.get() in self.db.experts:
                showinfo(title='Invalid name!', message="Given name already exists in the database!")
            else:
                self.db.add_expert(entry.get())
                expert_list.config(state=NORMAL)
                expert_list.insert("end", "● " + entry.get() + "\n")
                expert_list.config(state=DISABLED)

                self.root.withdraw()
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

                countries = self.db.countries
                sub = []
                for category in self.db.categories:
                    if len(self.db.subcategories_map.get(category)) > 0:
                        for subcategory in self.db.subcategories_map.get(category):
                            sub.append([category, subcategory])
                        sub.append([category, category])
                        # przechodze przez wszystkie podkategorie i porownuje kraje
                        # na koncu powordnuje podkategorie
                    else:
                        sub.append([category])
                        # porownuje kraje

                labels = ["categories"]
                names = [self.db.categories]
                categories = ["categories"]
                for s in sub:
                    if len(s) == 2:
                        if s[0] != s[1]:
                            labels.append("Comparison for " + str(s[1]) + " from " + str(s[0]))
                            names.append(countries)
                            categories.append(str(s[1]))
                            # #dla s[0] _ s[1]
                        else:
                            labels.append("Comparison for weights within " + str(s[0]))
                            names.append(self.db.subcategories_map.get(s[0]))
                            categories.append(str(s[0]))
                            # #dla s[0] wagi podkategorii
                    else:
                        labels.append("Comparison for " + str(s[0]))
                        names.append(countries)
                        categories.append(str(s[0]))
                        # # dla s[0]

                idx = 0
                e_label = Entry(frame, fg='black', font=self.FONT, width=50, justify=CENTER)
                e_label.grid(row=0, column=0, columnspan=4)
                e_label.config(state=DISABLED)
                e1 = Entry(frame, fg='black', font=self.FONT, width=20, justify=CENTER)
                e1.grid(row=1, column=0)
                e1.config(state=DISABLED)
                s1 = Scale(frame, from_=9, to=1, width=25)
                s1.grid(row=1, column=1, padx=5)
                s2 = Scale(frame, from_=9, to=1, width=25)
                s2.grid(row=1, column=2, padx=5)
                e2 = Entry(frame, fg='black', font=self.FONT, width=20, justify=CENTER)
                e2.grid(row=1, column=3)
                e2.config(state=DISABLED)

                previous_idx1 = -1
                previous_idx2 = -1

                expert_chosen = "idk"
                true_category = "idk"

                def _next():
                    nonlocal idx, names, labels, e_label, e1, e2, s1, s2, previous_idx1, previous_idx2, expert_chosen, \
                        true_category
                    finishing = True
                    _break = False

                    if idx > 0:
                        self.db.set_matrix_field(true_category, expert_chosen, previous_idx2, previous_idx1,
                                                 s1.get() / s2.get())

                    idx_copy = idx
                    for index, label in enumerate(labels):
                        for idx1 in range(len(names[index])):
                            for idx2 in range(idx1 + 1, len(names[index])):
                                if idx_copy == 0:
                                    idx += 1
                                    finishing = False
                                    current_name1 = names[index][idx1]
                                    current_name2 = names[index][idx2]
                                    current_label = label

                                    expert_chosen = entry.get()
                                    true_category = categories[index]

                                    previous_idx1 = idx1
                                    previous_idx2 = idx2
                                    _break = True
                                if _break:
                                    break
                                idx_copy -= 1
                            if _break:
                                break
                        if _break:
                            break

                    if finishing:
                        showinfo(title='Comparing done', message="All pAirs for this category have been compared!\n"
                                                                 "Saving opinions.")
                        save()
                    else:
                        e_label.config(state=NORMAL)
                        e_label.delete(0, "end")
                        e_label.insert(0, current_label)
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

                next_button = Button(frame, text="Next", font=self.FONT, command=_next)
                next_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

                def save():
                    if idx > 0:
                        self.db.set_matrix_field(true_category, expert_chosen, previous_idx2, previous_idx1,
                                                 s1.get() / s2.get())

                    # TODO zapisywanie zmian
                    self.root.deiconify()
                    new_expert_window.destroy()
                    pass

                save_button = Button(frame, text="Save and return", font=self.FONT, command=save)
                save_button.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

            self.expert_no += 1
            entry.delete(0, "end")
            entry.insert(0, "Unknown Expert " + str(self.expert_no))

        add_expert_label = Label(root, text="Enter new expert name", font=self.LABEL_FONT)
        add_expert_label.grid(row=row_no, column=column_no)
        add_expert_entry = Entry(root, width=20, font=self.FONT)
        add_expert_entry.insert(0, "Unknown Expert 0")
        add_expert_entry.grid(row=row_no + 1, column=column_no, padx=15, pady=5)
        add_expert_button = Button(root, text="Add new expert", font=self.FONT,
                                   command=lambda: add_expert(add_expert_entry))
        add_expert_button.grid(row=row_no + 2, column=column_no, padx=50)

    def create_preview_button(self, root, column_no, row_no):

        def preview():
            self.root.withdraw()
            preview_window = Toplevel()
            preview_window.title("Opinions")
            preview_window.geometry("1600x900")
            # "1024x576"
            preview_window.resizable(False, False)

            frame = Frame(preview_window, bg="light grey", pady=10, padx=10)
            frame.grid(row=0, column=0, rowspan=2, padx=15, pady=15)

            preview_frame_bottom = Frame(preview_window, bg="light grey", padx=10)
            preview_frame_bottom.grid(row=1, column=1, padx=5, pady=5)

            preview_frame_top = Frame(preview_window, bg="light grey", padx=10)
            preview_frame_top.grid(row=0, column=1, padx=5, pady=5)

            missing_data = self.db.is_missing_data()

            experts = self.db.experts
            experts_listbox = Listbox(frame, listvariable=Variable(value=experts), height=len(experts))
            experts_listbox.grid(row=0, column=0, padx=10, pady=10)

            categories = self.db.categories
            categories.insert(0, self.NO_CATEGORY)
            categories_listbox = Listbox(frame, listvariable=Variable(value=categories), height=len(categories))
            categories_listbox.grid(row=0, column=1, padx=10, pady=10)

            subcategories = list(self.db.subcategories_map.values())
            for sc in subcategories:
                sc.insert(0, self.NO_SUBCATEGORY)

            subcategories_listbox = Listbox(frame, listvariable=Variable(value=subcategories[0]),
                                            height=len(subcategories[0]))
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

            selected_experts = Label(frame, width=20, font=self.FONT)
            selected_experts.grid(row=2, column=0, columnspan=3, padx=10, pady=1)
            selected_categories = Label(frame, width=20, font=self.FONT)
            selected_categories.grid(row=3, column=0, columnspan=3, padx=10, pady=1)
            selected_subcategories = Label(frame, width=20, font=self.FONT)
            selected_subcategories.grid(row=4, column=0, columnspan=3, padx=10, pady=1)

            expert_chosen = ""
            category_chosen = ""
            subcategories_chosen = ""
            chosen_options = False

            def show_selected(event):
                nonlocal expert_chosen, category_chosen, subcategories_chosen, chosen_options
                missing_data = self.db.is_missing_data()

                selected_indices = experts_listbox.curselection()
                if len(selected_indices) > 0:
                    expert_chosen = experts_listbox.get(selected_indices[0])

                selected_indices = categories_listbox.curselection()
                category_chosen_no = 0
                if len(selected_indices) > 0:
                    category_chosen_no = selected_indices[0]
                    category_chosen = categories_listbox.get(selected_indices[0])

                    subcategories_listbox.delete(0, "end")
                    if selected_indices[0] == 0:
                        subcategories_listbox.insert("end", self.NO_SUBCATEGORY)
                    elif subcategories[selected_indices[0] - 1] == "":
                        subcategories_listbox.insert("end", category_chosen)
                    else:
                        for sub in subcategories[selected_indices[0] - 1]:
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
                            if categories[i] in category:
                                categories_listbox.itemconfig(i, {'bg': 'red'})
                            else:
                                categories_listbox.itemconfig(i, {'bg': 'white'})

                selected_experts.config(text=expert_chosen)
                selected_categories.config(text=category_chosen)
                selected_subcategories.config(text=subcategories_chosen)

            experts_listbox.bind('<<ListboxSelect>>', show_selected)
            categories_listbox.bind('<<ListboxSelect>>', show_selected)
            subcategories_listbox.bind('<<ListboxSelect>>', show_selected)

            def show_matrix():
                def isfloat(num):
                    try:
                        float(num)
                        return True
                    except ValueError:
                        return False

                if not chosen_options:
                    showinfo(title='Missing data', message="First you need to choice all the options from lists!")
                else:
                    nonlocal expert_chosen, category_chosen, subcategories_chosen
                    for widget in preview_frame_bottom.winfo_children():
                        widget.destroy()

                    key = subcategories_chosen
                    labels = self.db.countries
                    name = "Preview for " + str(expert_chosen) + ":\n"
                    if category_chosen == self.NO_CATEGORY:
                        key = "categories"
                        labels = self.db.categories
                        name += "categories' weights"
                    else:
                        if subcategories_chosen == self.NO_SUBCATEGORY:
                            key = category_chosen
                            name += str(category_chosen)
                            if len(self.db.subcategories_map.get(category_chosen)) > 0:
                                labels = list(self.db.subcategories_map.get(category_chosen))
                                name += " weights"
                        else:
                            name += str(subcategories_chosen) + " (" + str(category_chosen) + ")"
                    matrix = self.db.get_matrix(key, expert_chosen)
                    inconsistency_index = self.ahp.get_inconsistency_index(key, expert_chosen)
                    if not isinstance(inconsistency_index, str):
                        inconsistency_index = str(round(inconsistency_index, 5))
                    name += "\nInconsistency Index: " + inconsistency_index
                    Table(preview_frame_bottom, matrix, labels, preview_frame_top, name)

                    def save():
                        values = []
                        for widget in preview_frame_bottom.winfo_children():
                            if isinstance(widget, Entry):
                                values.append(widget.get())

                        mod = len(labels)
                        values = values[mod * 2:]
                        for v in values:
                            if not isfloat(v) or float(v) <= 0 or float(v) > 9:
                                showinfo(title='Invalid data!', message="Values need to be float type in range [1/9,9]")
                                return

                        true_category = category_chosen
                        if subcategories_chosen != self.NO_SUBCATEGORY:
                            true_category = subcategories_chosen
                        if true_category == self.NO_CATEGORY:
                            true_category = "categories"
                        for v in range(len(values)):
                            if v // mod < v % mod:
                                self.db.set_matrix_field(true_category, expert_chosen, v // mod, v % mod,
                                                         float(values[v]))

                        # TODO zapisywanie zmian
                        for widget in preview_frame_bottom.winfo_children():
                            widget.destroy()
                        pass

                    save_button = Button(preview_frame_bottom, text="Save", font=self.FONT, command=save, width=10)
                    save_button.grid(row=len(labels) + 1, columnspan=len(labels) + 1, pady=10, padx=10)

            def add_opinion():
                nonlocal expert_chosen, category_chosen, subcategories_chosen

                def missing_data(expert_chosen, category_chosen, subcategories_chosen):
                    for missing_expert, missing_categories in self.db.is_missing_data():
                        if missing_expert == expert_chosen and (category_chosen in missing_categories or
                                                                subcategories_chosen in missing_categories):
                            return True
                    return False

                if not chosen_options:
                    showinfo(title='Missing data', message="First you need to choice all the options from lists!")
                elif not missing_data(expert_chosen, category_chosen, subcategories_chosen):
                    showinfo(title='All opinions given',
                             message="No need to add more opinions as all of them have been "
                                     "already given.")
                else:
                    for widget in preview_frame_bottom.winfo_children():
                        widget.destroy()

                    names = self.db.countries
                    label = ""

                    if subcategories_chosen == self.NO_SUBCATEGORY:
                        if len(self.db.subcategories_map.get(category_chosen)) > 0:
                            names = list(self.db.subcategories_map.get(category_chosen))
                            label = "Comparison " + expert_chosen + " for weights within " + category_chosen
                        else:
                            label = "Comparison " + expert_chosen + " for " + category_chosen
                    else:
                        label = "Comparison " + expert_chosen + " for " + subcategories_chosen + " from " + category_chosen

                    idx = 0
                    e_label = Entry(preview_frame_bottom, fg='black', font=self.FONT, width=50, justify=CENTER)
                    e_label.grid(row=0, column=0, columnspan=4)
                    e_label.config(state=DISABLED)
                    e1 = Entry(preview_frame_bottom, fg='black', font=self.FONT, width=20, justify=CENTER)
                    e1.grid(row=1, column=0)
                    e1.config(state=DISABLED)
                    s1 = Scale(preview_frame_bottom, from_=9, to=1, width=25)
                    s1.grid(row=1, column=1, padx=5)
                    s2 = Scale(preview_frame_bottom, from_=9, to=1, width=25)
                    s2.grid(row=1, column=2, padx=5)
                    e2 = Entry(preview_frame_bottom, fg='black', font=self.FONT, width=20, justify=CENTER)
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
                            true_category = category_chosen
                            if subcategories_chosen != self.NO_SUBCATEGORY:
                                true_category = subcategories_chosen
                            self.db.set_matrix_field(true_category, expert_chosen, previous_idx2, previous_idx1,
                                                     s1.get() / s2.get())

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
                            showinfo(title='Comparing done', message="All pAirs for this category have been compared!\n"
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

                    _next()

                    next_button = Button(preview_frame_bottom, text="Next", font=self.FONT, command=_next)
                    next_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

                    def save():
                        # TODO zapisywanie zmian
                        for widget in preview_frame_bottom.winfo_children():
                            widget.destroy()
                        pass

                    save_button = Button(preview_frame_bottom, text="Save", font=self.FONT, command=save)
                    save_button.grid(row=2, column=2, columnspan=2, pady=10, padx=10)

            matrix_button = Button(frame, text="Show matrix", font=self.FONT, command=show_matrix)
            matrix_button.grid(row=5, column=0, pady=10, padx=10)
            add_opinion_button = Button(frame, text="Edit expert's opinions", font=self.FONT, command=add_opinion)
            add_opinion_button.grid(row=5, column=2, columnspan=2, pady=10, padx=10)

            def _return():
                self.root.deiconify()
                preview_window.destroy()

            return_button = Button(frame, text="Return", font=self.FONT, command=_return)
            return_button.grid(sticky=S, columnspan=3, pady=10, padx=10)

        preview_button = Button(root, text="Show\nexperts'\nopinions", font=self.FONT, command=preview, width=14,
                                height=7)
        preview_button.grid(column=column_no, row=0, rowspan=row_no, pady=10, padx=10)

    def create_solve_button(self, root, column_no, row_no):

        def solve():
            if self.db.is_missing_data():
                showinfo(title='Missing data', message="First you need fill all the necessary opinions!\n"
                                                       "You can do it in \"Show experts' opinions\" section.")
            else:
                # label = Label(main_window, text="Clicked")
                # label.grid(sticky=S, columnspan=5, pady=10, padx=10)

                results = Toplevel()
                results.title("Ranking")
                results.geometry("1600x900")  # "1024x576"
                results.resizable(False, False)

                frame = Frame(results, bg="light grey", pady=10, padx=10)
                frame.grid(sticky=SE, padx=5, pady=5)

                rank = self.ahp.calculate_ranking()

                ranking = []
                for i in range(len(rank[0])):
                    ranking.append((rank[0][i], rank[1][i]))
                # TODO dodać suwaczek
                for i in range(10):
                    ranking.append(("country" + (str(i)), 0.2))
                # TODO ewentualnie jakieś bajery do wyświetlania
                top = ranking[0][1]
                multi = 100 / top
                label_tmp = Label(frame, text="Which country is best\nto declare war on?", font=("Arial", 50, "bold"))
                label_tmp.grid(column=0, sticky=S, pady=10, padx=10)
                # labels.append(label_tmp)
                for idx, country in enumerate(ranking):
                    if idx == 0:
                        label_tmp = Label(frame, text=country[0] + ": " + str(round(country[1] * 100, 2)) + "%",
                                          font=("Arial", round(country[1] * multi)), fg="#F00")
                    elif idx == 1:
                        label_tmp = Label(frame, text=country[0] + ": " + str(round(country[1] * 100, 2)) + "%",
                                          font=("Arial", round(country[1] * multi)), fg="#A00")
                    elif idx == 2:
                        label_tmp = Label(frame, text=country[0] + ": " + str(round(country[1] * 100, 2)) + "%",
                                          font=("Arial", round(country[1] * multi)), fg="#500")
                    else:
                        label_tmp = Label(frame, text=country[0] + ": " + str(round(country[1] * 100, 2)) + "%",
                                          font=("Arial", round(country[1] * multi)))
                    label_tmp.grid(column=0, sticky=S, pady=10, padx=10)
                    # labels.append(label_tmp)


                # scrollbar = Scrollbar(frame, orient='vertical')
                # scrollbar.grid(row=0, column=1, sticky=NS)

                scrollderoot = Scrollbar(orient="vertical", command=frame.yview)
                scrollderoot.grid(column=1, row=0, sticky='ns', in_=frame)
                root.configure(yscrollcommand=scrollderoot.set)

        buttonSolve = Button(root, text="Solve", font=("Arial", 26), command=solve, bg="blue", fg="pink",
                             width=40)
        buttonSolve.grid(row=row_no, sticky=N, columnspan=3, pady=10, padx=10)
