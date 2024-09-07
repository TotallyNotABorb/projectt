
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("SpaceGlass")
window.iconbitmap(r"images/mag_glass.ico")
window.geometry("1160x690+300+150")

window.resizable(False, False)

bg3 = Image.open(r"images/background3.jpg")
resize_bg3 = bg3.resize((1160, 690))
tru_bg3 = ImageTk.PhotoImage(resize_bg3)


admin = False

def sign_in_frame():
    global admin
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
        global admin
        log_get = login_entry.get()
        pass_get = password_entry.get()
        with open("text/accounts.txt", "r") as accounts:
            read_acc = accounts.readlines()
        for i in range(len(read_acc)):
            if log_get in read_acc[i]:
                if pass_get in read_acc[i]:
                    main_menu_frame()
        if log_get == "Bagel" and pass_get =="ILoveBagels":
            global admin
            admin = True


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
        if number_save.isdigit():
            accounts = login_save + ", " + pass_save + ", " + number_save
            with open("text/accounts.txt", "a+") as names:
                names.write(accounts + "\n")
                sign_in_frame()
        else:
            error_label = Label(sign_up_frame, text="Phone n. can only contain numbers!", bg="#0f2065", fg="#ff0000",
                                font=("Arial", 18))
            error_label.place(x=375, y=380)

    sign_button = Button(sign_up_frame, text="Sign up", command=signup_check)
    sign_button.config(bg="#0f0fef", fg="#ffffff", activebackground="#ffffff", activeforeground="#0f0fef", width=20,
                       font=("Arial", 17), border=1)
    sign_button.place(x=440, y=340)


def main_menu_frame():


    main_menu_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")


    image2 = Image.open(r"images/background2.jpg")
    resize_image2 = image2.resize((1160, 690))
    img2 = ImageTk.PhotoImage(resize_image2)

    background_label = Label(main_menu_frame, image=img2)
    background_label.place(x=0, y=0)
    background_label.image = img2

    welcoming_label = Label(main_menu_frame, text="Welcome!")
    welcoming_label.config(bg="#1f1f29", width=20, fg="#ffffff", font=("Arial", 22, "bold"))
    welcoming_label.place(x=50, y=10)

    def add_frame():
        add_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

        bg3 = Image.open(r"images/background3.jpg")
        resize_bg3 = bg3.resize((1160, 690))
        tru_bg3 = ImageTk.PhotoImage(resize_bg3)

        background_label = Label(add_frame, image=tru_bg3)
        background_label.place(x=0, y=0)
        background_label.image = tru_bg3

        user_label = Label(add_frame, text="User's login:", bg="#0b0119", fg="#ffffff", font=("Arial", 18, "bold"))
        user_label.place(x=10, y=10)

        user_entry = Entry(add_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        user_entry.place(x=10, y=50)

        phone_label = Label(add_frame, text="User's phone number:", bg="#0b0119", fg="#ffffff",
                            font=("Arial", 18, "bold"))
        phone_label.place(x=10, y=90)

        phone_entry = Entry(add_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        phone_entry.place(x=10, y=130)

        vacant_label = Label(add_frame, text="Service required:", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"))
        vacant_label.place(x=10, y=170)

        vacant_entry = Entry(add_frame, bg="#ffffff", width=20, font=("Arial", 18), border=1)
        vacant_entry.place(x=10, y=210)

        def add_save():
            user = user_entry.get()
            phone = phone_entry.get()
            vacant = vacant_entry.get()
            if phone.isdigit():
                data = user + ", " + phone + ", " + vacant
                with open("text/data.txt", "a+") as dataa:
                    dataa.write(data + "\n")

                with open("text/data.txt", "r") as file:
                    lines = file.readlines()

                lines.sort(key=lambda line: line.split(",")[0])

                with open("text/data.txt", "w") as file:
                    file.writelines(lines)
            else:
                error_label = Label(add_frame, text="Phone n. can only contain numbers!", bg="#0b0119", fg="#ff0000",
                                    font=("Arial", 18))
                error_label.place(x=330, y=130)

        end_add_button = Button(add_frame, bg="#0f0fef", width=20, fg="#ffffff", text="Add", font=("Arial", 18, "bold"),
                                activebackground="#0f0fef", command=add_save)
        end_add_button.place(x=10, y=260)

        delete_label = Label(add_frame, text="Delete entry by login:", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"))
        delete_label.place(x=850, y=300)

        delete_entry = Entry(add_frame, bg="#ffffff", width=20, font=("Arial", 18), borderwidth=0)
        delete_entry.place(x=850, y=340)

        global main_menu_frame

        quit_button = Button(add_frame, bg="#0b0119", width=20, fg="#ffffff", text="Go to main menu",
                             font=("Arial", 18, "bold"), activebackground="#3f3f3f", command=main_menu_frame,
                             borderwidth=0)
        quit_button.place(x=830, y=10)

        def delete_save():
            user_to_delete = delete_entry.get()
            with open("text/data.txt", "r") as file:
                lines = file.readlines()
            with open("text/data.txt", "w") as file:
                for line in lines:
                    if not line.startswith(user_to_delete + ','):
                        file.write(line)

        delete_button = Button(add_frame, bg="#ff0000", width=20, fg="#ffffff", text="Delete",
                               font=("Arial", 18, "bold"), activebackground="#f00f00", command=delete_save)
        delete_button.place(x=825, y=380)

        add_frame.place(x=0, y=0)

    def format_line(line):
        words = line.split()
        formatted_words = []
        labels = ["Name", "Number", "Service"]

        for i, word in enumerate(words):
            if i < len(labels):
                formatted_words.append(f"{labels[i]}: {word}")
            else:
                formatted_words.append(word)

        return '   '.join(formatted_words)

    def show_frame():
        show_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

        bg3 = Image.open(r"images/background3.jpg")
        resize_bg3 = bg3.resize((1160, 690))
        tru_bg3 = ImageTk.PhotoImage(resize_bg3)

        background_label = Label(show_frame, image=tru_bg3)
        background_label.place(x=0, y=0)
        background_label.image = tru_bg3

        with open("text/data.txt", "r") as file:
            data = file.readlines()

        formatted_data = '\n'.join(format_line(line) for line in data).title()

        job_label = Label(show_frame, text=formatted_data, bg="#0b0119", fg="#ffffff", font=("Arial", 18),
                          justify='left')
        job_label.place(x=100, y=50)

        show_frame.place(x=0, y=0)

        global main_menu_frame

        quit_button = Button(show_frame, bg="#0b0119", width=20, fg="#ffffff", text="Go to main menu",
                             font=("Arial", 18, "bold"), activebackground="#0b0119", command=main_menu_frame,
                             borderwidth=0)
        quit_button.place(x=830, y=10)
    if admin:
        add_button = Button(main_menu_frame, text="Add", command=add_frame)
        add_button.config(bg="#1f1f29", width=14, fg="#ffffff", font=("Arial", 15, "bold"), borderwidth=0,
                        activebackground="#1f1f29", activeforeground="#000000")
        add_button.place(x=1000, y=20)

    show_button = Button(main_menu_frame, text="Show", bg="#1f1f29", width=14, fg="#ffffff", font=("Arial", 15, "bold"),
                         borderwidth=0, activebackground="#1f1f29", activeforeground="#000000", command=show_frame)
    show_button.place(x=1000, y=60)

    def update_frame():
        update_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

        bg3 = Image.open(r"images/background3.jpg")
        resize_bg3 = bg3.resize((1160, 690))
        tru_bg3 = ImageTk.PhotoImage(resize_bg3)

        background_label = Label(update_frame, image=tru_bg3)
        background_label.place(x=0, y=0)
        background_label.image = tru_bg3

        search_label = Label(update_frame, text="Enter name to update:", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"))
        search_label.place(x=10, y=10)

        search_entry = Entry(update_frame, bg="#ffffff", width=30, font=("Arial", 18), border=1)
        search_entry.place(x=10, y=50)

        result_label = Label(update_frame, text="", bg="#0b0119", fg="#ffffff", font=("Arial", 18), wraplength=1100,
                             justify="left")
        result_label.place(x=10, y=100)

        def search_entry_by_name():
            search_name = search_entry.get()
            found = False
            with open("text/data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(search_name + ","):
                        result_label.config(text=line.strip())
                        found = True
                        break
            if not found:
                result_label.config(text="Name not found, try again!")

        update_label = Label(update_frame, text="Which field to update?", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"))
        update_label.place(x=10, y=150)

        field_var = StringVar(value="name")
        field_name_radio = Radiobutton(update_frame, text="Name", variable=field_var, value="name", bg="#0b0119",
                                       fg="#ffffff", font=("Arial", 18))
        field_name_radio.place(x=10, y=200)

        field_phone_radio = Radiobutton(update_frame, text="Phone", variable=field_var, value="phone", bg="#0b0119",
                                        fg="#ffffff", font=("Arial", 18))
        field_phone_radio.place(x=10, y=250)

        field_service_radio = Radiobutton(update_frame, text="Service", variable=field_var, value="service",
                                          bg="#0b0119", fg="#ffffff", font=("Arial", 18))
        field_service_radio.place(x=10, y=300)

        new_value_label = Label(update_frame, text="New name/service/phone:", bg="#0b0119", fg="#ffffff",
                                font=("Arial", 18, "bold"))
        new_value_label.place(x=10, y=350)

        new_value_entry = Entry(update_frame, bg="#ffffff", width=30, font=("Arial", 18), border=1)
        new_value_entry.place(x=10, y=400)

        def update_entry():
            search_name = search_entry.get()
            field_to_update = field_var.get()
            new_value = new_value_entry.get()
            if not search_name or not new_value:
                result_label.config(text="Please fill every line!!!")
                return

            found = False
            with open("text/data.txt", "r") as file:
                lines = file.readlines()

            with open("text/data.txt", "w") as file:
                for line in lines:
                    if line.startswith(search_name + ","):
                        parts = line.strip().split(", ")
                        if field_to_update == "name":
                            file.write(f"{new_value}, {parts[1]}, {parts[2]}\n")
                        elif field_to_update == "phone":
                            file.write(f"{parts[0]}, {new_value}, {parts[2]}\n")
                        elif field_to_update == "service":
                            file.write(f"{parts[0]}, {parts[1]}, {new_value}\n")
                        found = True
                    else:
                        file.write(line)

            if found:
                result_label.config(text=f"Updated!")
            else:
                result_label.config(text="Entry not found! Try again!")

        update_button = Button(update_frame, text="Update", bg="#0f0fef", fg="#ffffff", font=("Arial", 18, "bold"),
                               activebackground="#0f0fef", command=update_entry)
        update_button.place(x=10, y=450)

        global main_menu_frame

        quit_button = Button(update_frame, text="Go to main menu", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"), activebackground="#0b0119", command=main_menu_frame,
                             borderwidth=0)
        quit_button.place(x=10, y=500)

        update_frame.place(x=0, y=0)

    def search_frame():
        search_frame = Frame(window, width=1160, height=690, bg="#3f3f3f")

        bg3 = Image.open(r"images/background3.jpg")
        resize_bg3 = bg3.resize((1160, 690))
        tru_bg3 = ImageTk.PhotoImage(resize_bg3)

        background_label = Label(search_frame, image=tru_bg3)
        background_label.place(x=0, y=0)
        background_label.image = tru_bg3

        name_label = Label(search_frame, text="Enter name to search", bg="#0b0119", fg="#ffffff",
                           font=("Arial", 18, "bold"))
        name_label.place(x=10, y=10)

        name_entry = Entry(search_frame, bg="#ffffff", width=30, font=("Arial", 18), border=1)
        name_entry.place(x=10, y=50)

        result_label = Label(search_frame, text="", bg="#0b0119", fg="#ffffff", font=("Arial", 18), wraplength=1100,
                             justify="left")
        result_label.place(x=10, y=100)

        def search_name():
            search_name = name_entry.get()
            found = False

            with open("text/data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(search_name + ","):
                        result_label.config(text=line.strip())
                        found = True
                        break

            if not found:
                result_label.config(text="Couldnt find such name, try again!")

        search_button = Button(search_frame, text="Search", bg="#0f0fef", fg="#ffffff", font=("Arial", 18, "bold"),
                               activebackground="#0f0fef", command=search_name)
        search_button.place(x=350, y=50)

        global main_menu_frame

        quit_button = Button(search_frame, text="Go to main menu", bg="#0b0119", fg="#ffffff",
                             font=("Arial", 18, "bold"),
                             activebackground="#0b0119", command=main_menu_frame, borderwidth=0)
        quit_button.place(x=10, y=150)

        search_frame.place(x=0, y=0)

    search_button = Button(main_menu_frame, text="Search", bg="#1f1f29", width=14, fg="#ffffff",
                           font=("Arial", 15, "bold"), borderwidth=0, activebackground="#1f1f29",
                           activeforeground="#000000", command=search_frame)
    search_button.place(x=1000, y=140)
    if admin:
        update_button = Button(main_menu_frame, text="Update", command=update_frame)
        update_button.config(bg="#1f1f29", width=14, fg="#ffffff", font=("Arial", 15, "bold"), borderwidth=0,
                             activebackground="#1f1f29", activeforeground="#000000")
        update_button.place(x=1000, y=100)

    main_menu_frame.place(x=0, y=0)


sign_in_frame()
window.mainloop()