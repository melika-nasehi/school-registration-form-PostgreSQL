import tkinter
from tkinter import *
import tkinter as tk

import form1
import psycopg2
from tkinter import ttk
from tkinter import messagebox


def form2():
    conn = psycopg2.connect(host='78.38.35.219', dbname='401463180', user='401463180', password='123456', port=5432,
                            options='-c search_path=school')
    cur = conn.cursor()
    root = Tk()
    root.title('School Database')
    root.config(background='#79d279')
    root.resizable(width=False, height=False)
    root.geometry("1300x600+90+50")  # Width, height, x, y

    cur.execute("""select * from student
            left join mother on student.mother_melli_code = mother.mother_melli_code
            left join father on student.father_melli_code = father.father_melli_code""")
    data = cur.fetchall()

    title_label = Label(root, text="(Student & parents)  FORM", font="calibri 18 bold", fg="#800080", background='#ffccff')
    title_label.pack()

    # Create the table
    table = ttk.Treeview(root)
    table['columns'] = ('melli', 'firstName', 'lastName', 'birth', 'motherMelli',
                        'fatherMelli', 'postcode', 'mother_melli_code', 'mother_first_name', 'mother_last_name',
                        "mother_phone", 'father_melli_code', 'father_first_name', 'father_last_name',
                        "father_phone")
    table.column('#0', width=50)
    table.column('melli', width=100)
    table.column('firstName', width=100)
    table.column('lastName', width=150)
    table.column('birth', width=100)
    table.column('motherMelli', width=100)
    table.column('fatherMelli', width=100)
    table.column('postcode', width=100)
    table.column('mother_melli_code', width=100)
    table.column('mother_first_name', width=100)
    table.column('mother_last_name', width=100)
    table.column('mother_phone', width=100)
    table.column('father_melli_code', width=100)
    table.column('father_first_name', width=100)
    table.column('father_last_name', width=100)
    table.column('father_phone', width=100)
    table.pack(pady=5)

    # Add the title row
    table.insert('', 0, text='#', values=('کد ملی', 'نام', 'نام خانوادگی', 'تاریخ تولد',
                                          'کد ملی مادر', 'کد ملی پدر', 'کدپستی', 'کد ملی مادر',
                                          'نام مادر', 'نام خانوادگی مادر', 'تلفن مادر', 'کد ملی پدر',
                                          'نام پدر', 'نام خانوادگی پدر', 'تلفن پدر'))

    # Add the data to the table
    i = 0
    for row in data:
        table.insert('', 'end', text=i, values=(row[0], row[1], row[2], row[3], row[4], row[5],
                                                row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                                                row[13], row[14]))
        i = i + 1

    # Add a scrollbar vertical
    scrollbar1 = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    table.configure(yscrollcommand=scrollbar1.set)
    scroll_label1 = Label(root, text="you can scroll down ----------->", font=("Calibri Bold", 12), background='pink')
    scroll_label1.config(fg="#ff0066")
    scroll_label1.place(x=1060, y=300)

    # Add a scrollbar horizontal
    scrollbar2 = ttk.Scrollbar(root, orient="horizontal", command=table.xview)
    scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
    table.configure(xscrollcommand=scrollbar2.set)
    scroll_label2 = Label(root, text="you can scroll left 👇", font=("Calibri Bold", 12), background='pink')
    scroll_label2.config(fg="#ff0066")
    scroll_label2.place(x=1000, y=550)

    # CRUD Buttons
    def create():
        # clean the screen
        for child in root.winfo_children():
            if isinstance(child, tk.Entry):
                child.destroy()

        for child in root.winfo_children():
            if isinstance(child, tk.Button):
                if child != create_button and child != update_button and child != delete_button and child != refresh_button:
                    child.destroy()

        for child in root.winfo_children():
            if isinstance(child, ttk.Combobox):
                child.destroy()

        for child in root.winfo_children():
            if isinstance(child, tk.Label):
                if child != title_label and child != scroll_label1 and child != scroll_label2:
                    child.destroy()

        Lable1 = Label(root, text="please enter the values and then press the SAVE button :",
                       fg="#339933", font=("Calibri Bold", 14), background='#79d279')
        Lable1.place(x=50, y=285)
        Lable2 = Label(root, text="Note that all the fields are necessary (NULL values raise ERROR):",
                       fg="#e60000", font=("Calibri ", 10), background='#79d279')
        Lable2.place(x=550, y=285)

        studentLable = Label(root, text="school :", fg="#4d94ff", font=("Calibri Bold", 11), background='#79d279')
        studentLable.place(x=30, y=345)

        # melli code
        melli = Entry(root, width=15)
        melli.place(x=100, y=350)
        l1 = Label(root, text="melli code", background='#79d279')
        l1.place(x=100, y=325)

        # first name
        first = Entry(root, width=15)
        first.place(x=230, y=350)
        l2 = Label(root, text="first name", background='#79d279')
        l2.place(x=230, y=325)

        # last name
        last = Entry(root, width=15)
        last.place(x=360, y=350)
        l3 = Label(root, text="last name", background='#79d279')
        l3.place(x=360, y=325)

        # date of birth
        birth = Entry(root, width=15)
        birth.place(x=490, y=350)
        l4 = Label(root, text="date of birth", background='#79d279')
        l4.place(x=490, y=325)

        # mother melli code
        mother_melli = Entry(root, width=15)
        mother_melli.place(x=620, y=350)
        l5 = Label(root, text="mother melli code", background='#79d279')
        l5.place(x=620, y=325)

        # father melli code
        father_melli = Entry(root, width=15)
        father_melli.place(x=750, y=350)
        l6 = Label(root, text="father melli code", background='#79d279')
        l6.place(x=750, y=325)

        # post code
        post = Entry(root, width=15)
        post.place(x=880, y=350)
        l7 = Label(root, text="post code", background='#79d279')
        l7.place(x=880, y=325)

        mother_label = Label(root, text="mother :", fg="#4d94ff", font=("Calibri Bold", 11), background='#79d279')
        mother_label.place(x=30, y=410)

        # mother first name
        mother_first_name = Entry(root, width=15)
        mother_first_name.place(x=100, y=415)
        l8 = Label(root, text="mother first name", background='#79d279')
        l8.place(x=100, y=390)

        # mother last name
        mother_last_name = Entry(root, width=15)
        mother_last_name.place(x=230, y=415)
        l9 = Label(root, text="mother last name", background='#79d279')
        l9.place(x=230, y=390)

        # mother phone
        mother_phone = Entry(root, width=15)
        mother_phone.place(x=360, y=415)
        l10 = Label(root, text="mother phone", background='#79d279')
        l10.place(x=360, y=390)

        father_label = Label(root, text="father :", fg="#4d94ff", font=("Calibri Bold", 11), background='#79d279')
        father_label.place(x=30, y=475)

        # father first name
        father_first_name = Entry(root, width=15)
        father_first_name.place(x=100, y=475)
        l11 = Label(root, text="father first name", background='#79d279')
        l11.place(x=100, y=450)

        # father last name
        father_last_name = Entry(root, width=15)
        father_last_name.place(x=230, y=475)
        l12 = Label(root, text="father last name", background='#79d279')
        l12.place(x=230, y=450)

        # father phone
        father_phone = Entry(root, width=15)
        father_phone.place(x=360, y=475)
        l13 = Label(root, text="father phone", background='#79d279')
        l13.place(x=360, y=450)

        # insert the entries into database
        def insert_into_database():
            conn = psycopg2.connect(host='78.38.35.219', dbname='401463180', user='401463180', password='123456',
                                    port=5432,
                                    options='-c search_path=school')
            cur = conn.cursor()

            try:
                #insert into mother
                thing1 = mother_melli.get()
                thing2 = mother_first_name.get()
                thing3 = mother_last_name.get()
                thing4 = mother_phone.get()

                cur.execute("""INSERT INTO school.mother (mother_melli_code, mother_first_name,
                                        mother_last_name, mother_phone) 
                                        VALUES (%s,%s,%s,%s) ON CONFLICT(mother_melli_code) DO NOTHING""",
                            (thing1, thing2, thing3, thing4))

                #insert into father
                thing5 = father_melli.get()
                thing6 = father_first_name.get()
                thing7 = father_last_name.get()
                thing8 = father_phone.get()

                cur.execute("""INSERT INTO school.father (father_melli_code, father_first_name,
                                                        father_last_name, father_phone) 
                                                        VALUES (%s,%s,%s,%s) ON CONFLICT(father_melli_code) DO NOTHING""",
                            (thing5, thing6, thing7, thing8))

                #insert into student
                thing9 = melli.get()
                thing10 = first.get()
                thing11 = last.get()
                thing12 = birth.get()
                thing13 = mother_melli.get()
                thing14 = father_melli.get()
                thing15 = post.get()

                cur.execute("""INSERT INTO school.student (student_melli_code , student_first_name, student_last_name,
                     date_of_birth, mother_melli_code, father_melli_code, postcode) 
                     VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(student_melli_code) DO NOTHING""",
                            (thing9, thing10, thing11, thing12, thing13, thing14, thing15))

                rows_affected = cur.rowcount
                if rows_affected == 0:
                    raise ValueError("Duplicate primary key : this 'student melli code' was added before")
                else:
                    tk.messagebox.showinfo("Done!", "new record added successfully."
                                                    "please click the REFRESH button to see the Changes")

                melli.delete(0, END)
                first.delete(0, END)
                last.delete(0, END)
                birth.delete(0, END)
                mother_melli.delete(0, END)
                father_melli.delete(0, END)
                post.delete(0, END)
                mother_first_name.delete(0, END)
                mother_last_name.delete(0, END)
                mother_phone.delete(0, END)
                father_first_name.delete(0, END)
                father_last_name.delete(0, END)
                father_phone.delete(0, END)

                conn.commit()
                cur.close()
                conn.close()

                # clean the screen
                save_button.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Label):
                        if child != title_label and child != scroll_label1 and child != scroll_label2:
                            child.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Entry):
                        child.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Error inserting record: {str(e)}")

        save_button = Button(root, text="SAVE", command=insert_into_database,
                             height=1, width=10, fg="#339933", font="Calibri 12 bold", background="#b3e6b3")
        save_button.place(x=650, y=440)

    def refresh():
        # deleting all
        children = table.get_children()
        for child in children[1:]:  # dont delete the tiltles
            table.delete(child)
        # adding again
        cur.execute("""select * from student
                    left join mother on student.mother_melli_code = mother.mother_melli_code
                    left join father on student.father_melli_code = father.father_melli_code""")
        data = cur.fetchall()

        i = 0
        for row in data:
            table.insert('', 'end', text=i, values=(row[0], row[1], row[2], row[3], row[4], row[5],
                                                    row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                                                    row[13], row[14]))
            i = i + 1

    def update():
        try:
            for child in root.winfo_children():
                if isinstance(child, tk.Entry):
                    child.destroy()

            for child in root.winfo_children():
                if isinstance(child, tk.Button):
                    if (child != create_button and child != update_button and child != delete_button
                            and child != refresh_button):
                        child.destroy()

            for child in root.winfo_children():
                if isinstance(child, ttk.Combobox):
                    child.destroy()

            for child in root.winfo_children():
                if isinstance(child, tk.Label):
                    if child != title_label and child != scroll_label1 and child != scroll_label2:
                        child.destroy()

            selected_item = table.selection()[0]
            student_primary_key = table.item(selected_item)['values'][0]  # 0 because melli code is the first column
            mother_primary_key = table.item(selected_item)['values'][7]  # 7 because mother melli code is the 7th column
            father_primary_key = table.item(selected_item)['values'][11]  # 11 because father melli code is the 11th column

            # make a drop_down menu to choose which field should be edited
            choices = ['کد ملی', 'نام', 'نام خانوادگی', 'تاریخ تولد',
                                          'کد ملی مادر', 'کد ملی پدر', 'کدپستی', 'کد ملی مادر',
                                          'نام مادر', 'نام خانوادگی مادر', 'تلفن مادر', 'کد ملی پدر',
                                          'نام پدر', 'نام خانوادگی پدر', 'تلفن پدر']

            branch_lable = Label(root, text="choose a field to update", background='#79d279')
            branch_lable.place(x=125, y=310)
            branch_dropdown = ttk.Combobox(root, values=choices)
            branch_dropdown.pack(anchor=tkinter.W, padx=125, pady=55)
            entryLable = Label(root, text="enter the new value", background='#79d279')
            entryLable.place(x=325, y=310)
            entry = Entry(root, width=40)
            entry.place(x=325, y=335)

            # exValue =

            # get the choice and edit it
            def edit():
                mother = False
                father = False
                mother_melli_code = False
                father_melli_code = False

                branch_selected = branch_dropdown.get()
                if branch_selected == 'کد ملی':
                    ex_field = table.item(selected_item)['values'][0]
                    field_to_edit = "student_melli_code"
                elif branch_selected == 'نام':
                    ex_field = table.item(selected_item)['values'][1]
                    field_to_edit = "student_first_name"
                elif branch_selected == 'نام خانوادگی':
                    ex_field = table.item(selected_item)['values'][2]
                    field_to_edit = "student_last_name"
                elif branch_selected == 'تاریخ تولد':
                    ex_field = table.item(selected_item)['values'][3]
                    field_to_edit = "date_of_birth"
                elif branch_selected == 'کد ملی مادر':
                    ex_field = table.item(selected_item)['values'][4]
                    field_to_edit = "mother_melli_code"
                    mother_melli_code = True
                elif branch_selected == 'کد ملی پدر':
                    ex_field = table.item(selected_item)['values'][5]
                    field_to_edit = "father_melli_code"
                    father_melli_code = True
                elif branch_selected == 'کد پستی':
                    ex_field = table.item(selected_item)['values'][6]
                    field_to_edit = "postcode"
                elif branch_selected == 'کد ملی مادر':
                    ex_field = table.item(selected_item)['values'][7]
                    field_to_edit = "mother_melli_code"
                    mother = True
                    mother_melli_code = True
                elif branch_selected == 'نام مادر':
                    ex_field = table.item(selected_item)['values'][8]
                    field_to_edit = "mother_first_name"
                    mother = True
                elif branch_selected == 'نام خانوادگی مادر':
                    ex_field = table.item(selected_item)['values'][9]
                    field_to_edit = "mother_last_name"
                    mother = True
                elif branch_selected == 'تلفن مادر':
                    ex_field = table.item(selected_item)['values'][10]
                    field_to_edit = "mother_phone"
                    mother = True
                elif branch_selected == 'کد ملی پدر':
                    ex_field = table.item(selected_item)['values'][11]
                    field_to_edit = "father_melli_code"
                    father = True
                    father_melli_code = True
                elif branch_selected == 'نام پدر':
                    ex_field = table.item(selected_item)['values'][12]
                    field_to_edit = "father_first_name"
                    father = True
                elif branch_selected == 'نام خانوادگی پدر':
                    ex_field = table.item(selected_item)['values'][13]
                    field_to_edit = "father_last_name"
                    father = True
                elif branch_selected == 'تلفن پدر':
                    ex_field = table.item(selected_item)['values'][14]
                    field_to_edit = "father_phone"
                    father = True

                ex_label = Label(root, text=("previous value : " + str(ex_field)), background='#79d279')
                ex_label.place(x=400, y=400)

                if not mother and not father and not mother_melli_code and not father_melli_code:
                    cur.execute(
                        "Update school.student set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                        " where student_melli_code = " + "'" + str(student_primary_key) + "'")

                if mother:
                    cur.execute("Update school.mother set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where mother_melli_code = " + "'" + str(mother_primary_key) + "'")

                if father:
                    cur.execute("Update school.father set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where father_melli_code = " + "'" + str(father_primary_key) + "'")

                if mother_melli_code:
                    cur.execute("Update school.mother set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where mother_melli_code = " + "'" + str(mother_primary_key) + "'")
                    cur.execute(
                        "Update school.student set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                        " where student_melli_code = " + "'" + str(student_primary_key) + "'")

                if father_melli_code:
                    cur.execute("Update school.father set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where father_melli_code = " + "'" + str(father_primary_key) + "'")
                    cur.execute(
                        "Update school.student set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                        " where student_melli_code = " + "'" + str(student_primary_key) + "'")

                # clean the screen
                submit_button.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Entry):
                        child.destroy()

                for child in root.winfo_children():
                    if isinstance(child, ttk.Combobox):
                        child.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Label):
                        if child != title_label and child != scroll_label1 and child != scroll_label2:
                            child.destroy()

            submit_button = Button(root, text="Submit", command=edit)
            submit_button.place(x=325, y=400)

        except Exception as e:
            messagebox.showerror("Error", "choose a record to update")

    def delete():
        try:
            selected_item = table.selection()[0]
            primary_key = table.item(selected_item)['values'][0]  # 0 because melli code is the first column

            if tk.messagebox.askyesno("Deleting", "Are you sure you want to delete this record?"):
                cur.execute("delete from school.student where student.student_melli_code=%s", (str(primary_key),))
                table.delete(selected_item)  # delete from table
        except Exception as e:
            messagebox.showerror("Error", "choose a record to delete")

    def search():
        search_root = Tk()
        search_root.geometry("700x500+400+200")  # Width, height, x, y
        search_root.title('school Database')
        search_root.grid()

        search_label = Label(search_root, text="Search by :")
        search_label.pack()

        choices = ['کد ملی', 'نام', 'نام خانوادگی', 'تاریخ تولد',
                   'کد ملی مادر', 'کد ملی پدر', 'کدپستی', 'کد ملی مادر',
                   'نام مادر', 'نام خانوادگی مادر', 'تلفن مادر', 'کد ملی پدر',
                   'نام پدر', 'نام خانوادگی پدر', 'تلفن پدر']
        option_dropdown = ttk.Combobox(search_root, values=choices)
        option_dropdown.pack()
        empty_label = Label(search_root, text="")
        empty_label.pack()
        entry_search_label = Label(search_root, text="enter the value to search")
        entry_search_label.pack()
        search_entry = Entry(search_root, width=40)
        search_entry.pack()

        def find():
            field_to_search = option_dropdown.get()
            thing_to_search = search_entry.get()

            selected = option_dropdown.get()
            if selected == 'کد ملی':
                field_to_search = "student_melli_code"
            elif selected == 'نام':
                field_to_search = "student_first_name"
            elif selected == 'نام خانوادگی':
                field_to_search = "student_last_name"
            elif selected == 'تاریخ تولد':
                field_to_search = "date_of_birth"
            elif selected == 'کد ملی مادر':
                field_to_search = "mother_melli_code"
            elif selected == 'کد ملی پدر':
                field_to_search = "father_melli_code"
            elif selected == 'کد پستی':
                field_to_search = "postcode"
            elif selected == 'کد ملی مادر':
                field_to_search = "mother_melli_code"
            elif selected == 'نام مادر':
                field_to_search = "mother_first_name"
            elif selected == 'نام خانوادگی مادر':
                field_to_search = "mother_last_name"
            elif selected == 'تلفن مادر':
                field_to_search = "mother_phone"
            elif selected == 'کد ملی پدر':
                field_to_search = "father_melli_code"
            elif selected == 'نام پدر':
                field_to_search = "father_first_name"
            elif selected == 'نام خانوادگی پدر':
                field_to_search = "father_last_name"
            elif selected == 'تلفن پدر':
                field_to_search = "father_phone"


            cur.execute("""select * from student
            left join mother on student.mother_melli_code = mother.mother_melli_code
            left join father on student.father_melli_code = father.father_melli_code
                                where """ + str(field_to_search) + """ = """ + """'""" +str(thing_to_search) + """'""")

            result_label = Label(search_root, text=str(cur.fetchall()))
            result_label.pack()

        find_button = Button(search_root, text="find", command=find, font="calibri 11 bold")
        find_button.pack()
        search_root.mainloop()

    def back_to_menu():
        root2 = Tk()
        root2.geometry("400x200+400+200")  # Width, height, x, y
        root2.title('school Database')
        root2.grid()

        label = Label(root2, text='Choose your form type : ', font=('Arial', 13))
        label.pack()
        label2 = Label(root2, text='', font=('Arial', 13))
        label2.pack()

        r = IntVar()

        form1_radio_button = Radiobutton(root2, text="student & home", variable=r, value=1)
        form2_radio_button = Radiobutton(root2, text="student & parents", variable=r, value=2)

        form1_radio_button.pack()
        form2_radio_button.pack()

        root2.mainloop()

    create_button = Button(root, text="Create new ➕", command=create, font="calibri 11 bold")
    create_button.place(x=100, y=520, height=40, width=110)

    update_button = Button(root, text="update ✍️", command=update, font="calibri 11 bold")
    update_button.place(x=230, y=520, height=40, width=90)

    delete_button = Button(root, text="        delete 🗑️", command=delete, font="calibri 11 bold")
    delete_button.place(x=340, y=520, height=40, width=80)

    refresh_button = Button(root, text="refresh ⟳", command=refresh, font="calibri 11 bold")
    refresh_button.place(x=490, y=520, height=40, width=100)

    search_button = Button(root, text="search a student 🔍", command=search, font="calibri 11 bold")
    search_button.place(x=630, y=520, height=40, width=160)

    back_button = Button(root, text="back to menu", command=back_to_menu, font="calibri 11 bold")
    back_button.place(x=830, y=520, height=40, width=90)

    root.mainloop()
    conn.commit()
    cur.close()
    conn.close()
