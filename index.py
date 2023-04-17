from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

jan = Tk()
jan.title("DP Systens - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 10)
jan.iconbitmap(default="icons/LogoIcon.ico")


logoType = PhotoImage(file="icons/logo.png")

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=400, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logoType, bg="MIDNIGHTBLUE")
LogoLabel.place(x=20, y=100)

UserLabel = Label(RightFrame, text="Usuario:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)


def Login():

    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User == ? and Password == ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()

    try:
        if User in VerifyLogin and Pass in VerifyLogin:
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem vindo!")

    except:
        messagebox.showinfo(title="login Info", message="Acesso negado. Verifique se esta cadastrado no site!")


LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=148, y=210)

Pa = Label(RightFrame, text="Não possui cadastro?", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
Pa.place(x=5, y=270)


def Register():
    LoginButton.place(x=601)
    Pa.place(x=601)
    RegisterButton.place(y=500)
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=18)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" and Email == "" and User == "" and Pass == "":
            messagebox.showerror(title="Register Error", message="Nao Deixe nenhum Campo Vazio.Preencha Todos os Campos")

        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()

            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Registrar", width=20, command=RegisterToDataBase)
    Register.place(x=170, y=210)


RegisterButton = ttk.Button(RightFrame, text="Registrar", width=15, command=Register)
RegisterButton.place(x=240, y=274)


jan.mainloop()
