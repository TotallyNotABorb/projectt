from tkinter import *
from PIL import Image, ImageTk


class General:
    def __init__(self):
        self.view = True
        self.search = True
        self.submit = True


class User(General):
    def __init__(self):
        super().__init__()
        self.add = False
        self.delete = False


class Admin(General):
    def __init__(self):
        super().__init__()
        self.add = True
        self.delete = True


window = Tk()
window.title("SpaceGlass")
window.iconbitmap(r"images/mag_glass.ico")
window.geometry("1160x690+300+150")

window.resizable(False, False)


def sign_in_frame():
    sign_in_frame = Frame(window, width=1160, height=690)
    sign_in_frame.place(x=0, y=0)

    # zadniy fon
    image = Image.open(r"images/backgrounddd.jpg")
    resize_image = image.resize((1160, 690))
    img = ImageTk.PhotoImage(resize_image)

    background_label = Label(sign_in_frame, image=img)
    background_label.place(x=0, y=0)
    background_label.image = img

    # nazvanie
    name1_label = Label(sign_in_frame, text="Space")
    name1_label.config(bg="#000a3d", fg="#0f0fef", font=("Arial", 20, "bold"))

    name1_label.place(x=482, y=50)
    name2_label = Label(sign_in_frame, text="Glass")
    name2_label.config(bg="#000a3d", fg="#ffffff", font=("Arial", 20, "bold"))
    name2_label.place(x=565, y=50)

    # login
    login_label = Label(sign_in_frame, text="Login:")
    login_label.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
    login_label.place(x=440, y=120)

    login_entry = Entry(sign_in_frame)
    login_entry.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
    login_entry.place(x=440, y=150)

    # password
    password_label = Label(sign_in_frame, text="Password:")
    password_label.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
    password_label.place(x=440, y=190)

    password_entry = Entry(sign_in_frame)
    password_entry.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
    password_entry.place(x=440, y=220)

    # control
    def signin_check():
        log_get = login_entry.get()
        pass_get = password_entry.get()
        with open("text/accounts.txt", "r") as accounts:
            read_acc = accounts.readlines()
        for i in range(len(read_acc)):
            if log_get in read_acc[i]:
                if pass_get in read_acc[i]:
                    main_menu_frame()

    sign_button = Button(sign_in_frame, text="Sign in", command=signin_check)
    sign_button.config(bg="#0f0fef", fg="#ffffff", activebackground="#ffffff", activeforeground="#0f0fef", width=20,
                       font=("Arial", 17), border=1)
    sign_button.place(x=440, y=270)

    log_sit_button = Button(sign_in_frame, text="Have no account? Press here to sign up!", command=sign_up_frame)
    log_sit_button.config(bg="#010010", fg="#ffffff", activebackground="#000000", activeforeground="#0f0fef", border=0)
    log_sit_button.place(x=480, y=650)


def sign_up_frame():
    sign_up_frame = Frame(window, width=1160, height=690)
    sign_up_frame.place(x=0, y=0)

    # zadniy fon
    image = Image.open(r"images/backgrounddd.jpg")
    resize_image = image.resize((1160, 690))
    img = ImageTk.PhotoImage(resize_image)

    background_label1 = Label(sign_up_frame, image=img)
    background_label1.place(x=0, y=0)
    background_label1.image = img
    # nazvanie
    name1_label = Label(sign_up_frame, text="Space")
    name1_label.config(bg="#000a3d", fg="#0f0fef", font=("Arial", 20, "bold"))
    name1_label.place(x=482, y=50)

    name2_label = Label(sign_up_frame, text="Glass")
    name2_label.config(bg="#000a3d", fg="#ffffff", font=("Arial", 20, "bold"))
    name2_label.place(x=565, y=50)

    # login
    login_label2 = Label(sign_up_frame, text="Login:")
    login_label2.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
    login_label2.place(x=440, y=120)

    login_entry2 = Entry(sign_up_frame)
    login_entry2.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
    login_entry2.place(x=440, y=150)

    # password
    password_label2 = Label(sign_up_frame, text="Password:")
    password_label2.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
    password_label2.place(x=440, y=190)

    password_entry2 = Entry(sign_up_frame)
    password_entry2.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
    password_entry2.place(x=440, y=220)
    # phone number
    number_label = Label(sign_up_frame, text="Number:")
    number_label.config(bg="#09154F", fg="#ffffff", font=("Arial", 18))
    number_label.place(x=440, y=260)

    number_entry = Entry(sign_up_frame)
    number_entry.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
    number_entry.place(x=440, y=300)

    # control
    def signup_check():
        login_save = login_entry2.get()
        pass_save = password_entry2.get()
        number_save = number_entry.get()
        accounts = login_save + ", " + pass_save + ", " + number_save
        with open("accounts.txt", "a+") as names:
            names.write(accounts + "\n")
            sign_in_frame()

    sign_button = Button(sign_up_frame, text="Sign up", command=signup_check)
    sign_button.config(bg="#0f0fef", fg="#ffffff", activebackground="#ffffff", activeforeground="#0f0fef", width=20,
                       font=("Arial", 17), border=1)
    sign_button.place(x=440, y=340)



def main_menu_frame():
    main_menu_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

    welcoming_label=Label(main_menu_frame,text="Welcome!")
    welcoming_label.config(bg="#3f3f3f",width=20,fg="#ffffff", font=("Arial", 22,"bold"))
    welcoming_label.place(x=50,y=10)

    def add_frame():
        add_frame=Frame(window,width=1160,height=690,bg="#3f3f3f")

        user_label=Label(add_frame,text="User's login:",bg="#3f3f3f",fg="#ffffff",font=("Arial", 18,"bold"))
        user_label.place(x=10,y=10)

        user_entry=Entry(add_frame,bg="#ffffff",width=20,font=("Arial", 18), border=1)
        user_entry.place(x=10,y=50)

        phone_label=Label(add_frame,text="User's phone number:",bg="#3f3f3f",fg="#ffffff",font=("Arial", 18,"bold"))
        phone_label.place(x=10,y=90)

        phone_entry=Entry(add_frame,bg="#ffffff",width=20,font=("Arial", 18), border=1)
        phone_entry.place(x=10,y=130)

        vacant_label=Label(add_frame,text="Service required:",bg="#3f3f3f",fg="#ffffff",font=("Arial", 18,"bold"))
        vacant_label.place(x=10,y=170)

        vacant_entry=Entry(add_frame,bg="#ffffff",width=20,font=("Arial", 18), border=1)
        vacant_entry.place(x=10,y=210)

        def add_save():
            user=user_entry.get()
            phone=phone_entry.get()
            vacant=vacant_entry.get()
            data=user+", "+phone+", "+vacant
            with open ("data.txt","a+") as dataa:
                dataa.write(data+"\n")


        end_add_button=Button(add_frame,bg="#0f0fef",width=20,fg="#ffffff",text="Add",font=("Arial",18,"bold"),activebackground="#0f0fef",command=add_save)
        end_add_button.place(x=10,y=260)







        add_frame.place(x=0,y=0)

    def show_frame():
        show_frame=Frame(window,width=1160,height=690,bg="#3f3f3f")


        with open("data.txt","r+") as dataa:
            data=dataa.readlines()
        job_label=Label(show_frame,text=data,bg="#3f3f3f",fg="#ffffff",font=("Arial",18,))
        job_label.place(x=100,y=50)




        show_frame.place(x=0,y=0)



        end_add_button=Button(add_frame,bg="#0f0fef",width=20,fg="#ffffff",text="Add",font=("Arial",18,"bold"),activebackground="#0f0fef",command=add_save)
        end_add_button.place(x=10,y=260)










    add_button=Button(main_menu_frame,text="Add",command=add_frame)
    add_button.config(bg="#3f3f3f",width=14,fg="#ffffff",font=("Arial",15,"bold"),borderwidth=0,activebackground="#3f3f3f",activeforeground="#000000")
    add_button.place(x=1000,y=20)

    show_button=Button(main_menu_frame,text="Show",bg="#3f3f3f",width=14,fg="#ffffff",font=("Arial",15,"bold"),borderwidth=0,activebackground="#3f3f3f",activeforeground="#000000",command=show_frame)
    show_button.place(x=1000,y=60)

    def submit_frame():
        submit_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

        user_label = Label(submit_frame, text="Your login:", bg="#3f3f3f", fg="#ffffff", font=("Arial", 18, "bold"))
        user_label.place(x=10, y=10)

        user_entry = Entry(submit_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        user_entry.place(x=10, y=50)

        phone_label = Label(submit_frame, text="Your phone number:", bg="#3f3f3f", fg="#ffffff",
                            font=("Arial", 18, "bold"))
        phone_label.place(x=10, y=90)

        phone_entry = Entry(submit_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        phone_entry.place(x=10, y=130)

        vacant_label = Label(submit_frame, text="Service required:", bg="#3f3f3f", fg="#ffffff",
                             font=("Arial", 18, "bold"))
        vacant_label.place(x=10, y=170)

        vacant_entry = Entry(submit_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        vacant_entry.place(x=10, y=210)

        def submit_save():
            user=user_entry.get()
            phone=phone_entry.get()
            vacant=vacant_entry.get()
            data=user+", "+phone+", "+vacant
            with open ("userdata.txt","a+") as dataa:
                dataa.write(data+"\n")

        submit_button = Button(submit_frame, bg="#0f0fef", width=20, fg="#ffffff", text="Add", font=("Arial", 18, "bold"),
                                activebackground="#0f0fef", command=submit_save)
        submit_button.place(x=10, y=260)

        submit_frame.place(x=0,y=0)




    submit_active_button=Button(main_menu_frame,text="Submit",bg="#3f3f3f",width=14,fg="#ffffff",font=("Arial",15,"bold"),borderwidth=0,activebackground="#3f3f3f",activeforeground="#000000",command=submit_frame)
    submit_active_button.place(x=1000,y=100)








    main_menu_frame.place(x=0, y=0)


sign_in_frame()
window.mainloop()