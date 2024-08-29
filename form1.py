import tkinter
from tkinter import *
import tkinter as tk
import psycopg2
from tkinter import ttk
from tkinter import messagebox

import form2


def form1():
    conn = psycopg2.connect(host='78.38.35.219', dbname='401463180', user='401463180', password='123456', port=5432,
                            options='-c search_path=school')
    cur = conn.cursor()
    root = Tk()
    root.title('School Database')
    root.config(background='pink')
    root.resizable(width=False, height=False)
    root.geometry("1300x600+90+50")  # Width, height, x, y

    cur.execute("""select * from student
            left join home on student.postcode=home.postcode""")
    data = cur.fetchall()

    title_label = Label(root, text="(Student & Home)  FORM", font="calibri 18 bold", fg="#800080", background='#ffccff')
    title_label.pack()

    # Create the table
    table = ttk.Treeview(root)
    table['columns'] = ('melli', 'firstName', 'lastName', 'birth', 'motherMelli',
                        'fatherMelli', 'postcode', 'postcode', 'phone', 'address')
    table.column('#0', width=50)
    table.column('melli', width=100)
    table.column('firstName', width=100)
    table.column('lastName', width=150)
    table.column('birth', width=100)
    table.column('motherMelli', width=100)
    table.column('fatherMelli', width=100)
    table.column('postcode', width=100)
    table.column('postcode', width=100)
    table.column('phone', width=100)
    table.column('address', width=400)
    table.pack(pady=10)

    # Add the title row
    table.insert('', 0, text='#', values=('کد ملی', 'نام', 'نام خانوادگی', 'تاریخ تولد',
                                          'کد ملی مادر', 'کد ملی پدر', 'کدپستی', 'کد پستی',
                                          'شماره ثابت', 'آدرس'))

    # Add the data to the table
    i = 0
    for row in data:
        table.insert('', 'end', text=i, values=(row[0], row[1], row[2], row[3], row[4], row[5],
                                                row[6], row[7], row[8], row[9]))
        i = i + 1

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    table.configure(yscrollcommand=scrollbar.set)
    scroll_label = Label(root, text="you can scroll down ----------->", font=("Calibri Bold", 12), background='pink')
    scroll_label.config(fg="#ff0066")
    scroll_label.place(x=1060, y=300)

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
                if child != title_label and child != scroll_label:
                    child.destroy()

        Lable1 = Label(root, text="please enter the values and then press the SAVE button :",
                       fg="#339933", font=("Calibri Bold", 14), background='pink')
        Lable1.place(x=50, y=285)
        Lable2 = Label(root, text="Note that all the fields are necessary (NULL values raise ERROR):",
                       fg="#e60000", font=("Calibri ", 10), background='pink')
        Lable2.place(x=100, y=440)

        studentLable = Label(root, text="school :", fg="#4d94ff", font=("Calibri Bold", 11), background='pink')
        studentLable.place(x=30, y=345)

        # melli code
        melli = Entry(root, width=15)
        melli.place(x=100, y=350)
        l1 = Label(root, text="melli code", background='pink')
        l1.place(x=100, y=325)

        # first name
        first = Entry(root, width=15)
        first.place(x=230, y=350)
        l2 = Label(root, text="first name", background='pink')
        l2.place(x=230, y=325)

        # last name
        last = Entry(root, width=15)
        last.place(x=360, y=350)
        l3 = Label(root, text="last name", background='pink')
        l3.place(x=360, y=325)

        # date of birth
        birth = Entry(root, width=15)
        birth.place(x=490, y=350)
        l4 = Label(root, text="date of birth", background='pink')
        l4.place(x=490, y=325)

        # mother melli code
        mother_melli = Entry(root, width=15)
        mother_melli.place(x=620, y=350)
        l5 = Label(root, text="mother melli code", background='pink')
        l5.place(x=620, y=325)

        # father melli code
        father_melli = Entry(root, width=15)
        father_melli.place(x=750, y=350)
        l6 = Label(root, text="father melli code", background='pink')
        l6.place(x=750, y=325)

        homeLable = Label(root, text="home :", fg="#4d94ff", font=("Calibri Bold", 11), background='pink')
        homeLable.place(x=30, y=410)

        # post code
        post = Entry(root, width=15)
        post.place(x=100, y=415)
        l7 = Label(root, text="post code", background='pink')
        l7.place(x=100, y=390)

        # telephone
        telephone = Entry(root, width=15)
        telephone.place(x=230, y=415)
        l8 = Label(root, text="telephone", background='pink')
        l8.place(x=230, y=390)

        # address
        address = Entry(root, width=59)
        address.place(x=360, y=415)
        l9 = Label(root, text="address", background='pink')
        l9.place(x=360, y=390)

        # insert the entries into database
        def insert_into_database():
            conn = psycopg2.connect(host='78.38.35.219', dbname='401463180', user='401463180', password='123456',
                                    port=5432,
                                    options='-c search_path=school')
            cur = conn.cursor()

            thing1 = post.get()
            thing2 = telephone.get()
            thing3 = address.get()

            try:
                cur.execute("""INSERT INTO school.home (postcode, telephone, address) 
                                VALUES (%s,%s,%s) ON CONFLICT(postcode) DO NOTHING""", (thing1, thing2, thing3))

                thing4 = melli.get()
                thing5 = first.get()
                thing6 = last.get()
                thing7 = birth.get()
                thing8 = mother_melli.get()
                thing9 = father_melli.get()

                cur.execute("""INSERT INTO school.student (student_melli_code , student_first_name, student_last_name,
                     date_of_birth, mother_melli_code, father_melli_code, postcode) 
                     VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(student_melli_code) DO NOTHING""",
                            (thing4, thing5, thing6, thing7, thing8, thing9, thing1))

                rows_affected = cur.rowcount
                if rows_affected == 0:
                    raise ValueError("Duplicate primary key : this 'student melli code' was added before")
                else:
                    tk.messagebox.showinfo("Done!", "new record added successfully."
                                                    "please click the REFRESH button to see the Changes")

                post.delete(0, END)
                telephone.delete(0, END)
                address.delete(0, END)
                melli.delete(0, END)
                first.delete(0, END)
                last.delete(0, END)
                birth.delete(0, END)
                mother_melli.delete(0, END)
                father_melli.delete(0, END)

                conn.commit()
                cur.close()
                conn.close()

                #clean the screen
                save_button.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Label):
                        if child != title_label and child != scroll_label:
                            child.destroy()

                for child in root.winfo_children():
                    if isinstance(child, tk.Entry):
                        child.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Error inserting record: {str(e)}")

        save_button = Button(root, text="SAVE", command=insert_into_database,
                             height=1, width=10, fg="#339933", font="Calibri 12 bold", background="#b3e6b3")
        save_button.place(x=750, y=400)

    def refresh():
        # deleting all
        children = table.get_children()
        for child in children[1:]:  # dont delete the tiltles
            table.delete(child)
        # adding again
        cur.execute("""select * from student
            left join home on student.postcode=home.postcode""")
        data = cur.fetchall()

        i = 0
        for row in data:
            table.insert('', 'end', text=i, values=(row[0], row[1],
                                                    row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
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
                    if child != title_label and child != scroll_label:
                        child.destroy()

            selected_item = table.selection()[0]
            student_primary_key = table.item(selected_item)['values'][0]  # 0 because melli code is the first column
            home_primary_key = table.item(selected_item)['values'][7]  # 7 because postcode is the 7th column

            # make a drop_down menu to choose which field should be edited
            choices = ['کد ملی', 'نام', 'نام خانوادگی', 'تاریخ تولد',
                       'کد ملی مادر', 'کد ملی پدر', 'کد پستی',
                       'شماره ثابت', 'آدرس']
            branch_lable = Label(root, text="choose a field to update", background='pink')
            branch_lable.place(x=125, y=310)
            branch_dropdown = ttk.Combobox(root, values=choices)
            branch_dropdown.pack(anchor=tkinter.W, padx=125, pady=55)
            entryLable = Label(root, text="enter the new value", background='pink')
            entryLable.place(x=325, y=310)
            entry = Entry(root, width=40)
            entry.place(x=325, y=335)

            # exValue =

            # get the choice and edit it
            def edit():
                home = False
                postcode = False
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
                elif branch_selected == 'کد ملی پدر':
                    ex_field = table.item(selected_item)['values'][5]
                    field_to_edit = "father_melli_code"
                elif branch_selected == 'کد پستی':
                    ex_field = table.item(selected_item)['values'][6]
                    field_to_edit = "postcode"
                    home = True
                    postcode = True
                elif branch_selected == 'شماره ثابت':
                    ex_field = table.item(selected_item)['values'][7]
                    field_to_edit = "telephone"
                    home = True
                elif branch_selected == 'آدرس':
                    ex_field = table.item(selected_item)['values'][8]
                    field_to_edit = "address"
                    home = True

                ex_label = Label(root, text=("previous value : " + str(ex_field)), background='pink')
                ex_label.place(x=400, y=400)

                if not home:
                    cur.execute(
                        "Update school.student set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                        " where student_melli_code = " + "'" + str(student_primary_key) + "'")

                if home:
                    cur.execute("Update school.home set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where postcode = " + "'" + str(home_primary_key) + "'")

                if postcode:
                    cur.execute("Update school.home set " + field_to_edit + " = " + "'" + str(entry.get()) + "'" +
                                " where postcode = " + "'" + str(home_primary_key) + "'")
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
                        if child != title_label and child != scroll_label:
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
                   'کد ملی مادر', 'کد ملی پدر', 'کد پستی',
                   'شماره ثابت', 'آدرس']
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
            elif selected == 'شماره ثابت':
                field_to_search = "telephone"
            elif selected == 'آدرس':
                field_to_search = "address"


            cur.execute("""select * from student
                                left join home on student.postcode=home.postcode
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

        def choose():
            root2.destroy()
            if r2.get() == 1:
                form1.form1()
            elif r2.get() == 2:
                form2.form2()

        label = Label(root2, text='Choose your form type : ', font=('Arial', 13))
        label.pack()
        label2 = Label(root2, text='', font=('Arial', 13))
        label2.pack()

        r2 = IntVar()

        form1_radio_button2 = Radiobutton(root2, text="student & home", variable=r2, value=1)
        form2_radio_button2 = Radiobutton(root2, text="student & parents", variable=r2, value=2)

        form1_radio_button2.pack()
        form2_radio_button2.pack()

        ok_button2 = Button(root2, text="OK", command=choose)
        ok_button2.pack()

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


'''
def back_to_menu():
    main.main()
    
back_button = Button(root, text="back to menu", command=back_to_menu, font="calibri 11 bold")
back_button.place(x=100, y=520, height=40, width=90)  
'''
