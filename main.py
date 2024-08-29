from tkinter import *
import form1
import form2


def main():
    root = Tk()
    root.geometry("400x200+400+200")  # Width, height, x, y
    root.title('school Database')
    root.grid()

    def choose():
        root.destroy()
        if r.get() == 1:
            form1.form1()
        elif r.get() == 2:
            form2.form2()

    label = Label(root, text='Choose your form type : ' , font=('Arial', 13))
    label.pack()
    label2 = Label(root, text='', font=('Arial', 13))
    label2.pack()

    r = IntVar()

    form1_radio_button = Radiobutton(root, text="student & home", variable=r, value=1)
    form2_radio_button = Radiobutton(root, text="student & parents", variable=r, value=2)

    form1_radio_button.pack()
    form2_radio_button.pack()

    ok_button = Button(root, text="OK", command=choose)
    ok_button.pack()

    root.mainloop()


main()
