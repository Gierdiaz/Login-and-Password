from tkinter import *

base_de_dados = []

def logando():
    for dados in base_de_dados:
        if cax_user.get() == dados[0] and cax_senha.get() == dados[1]:
            men["text"] = "Logando com sucesso!"
            men["foreground"] = "blue"
            break
        else:
            men["text"] = "Usuário ou Senha Inválida!"
            men["foregound"] = "red"

def cadastrando():
    user = cax_user.get()
    senha = cax_senha.get()
    base_de_dados.append([user, senha])
    print(base_de_dados)


i = Tk()
i.geometry("400x200")
i.title("Login")

"""USER Widgets"""
Label_user = Label(i, text = "User", foreground = "blue")
Label_user.pack()

cax_user = Entry(i)
cax_user.pack()

"""SENHA Widgets"""
Label_senha = Label(i, text = "Senha", foreground = "blue")
Label_senha.pack()

cax_senha = Entry(i)
cax_senha.pack()

"""BOTÕES"""
bt_login = Button(i, text = "Cadastrar", command = logando)
bt_login.pack()

bt_cadas = Button(i, text = "Cadastrar", command = cadastrando)
bt_cadas.pack()

"""MENSAGEM"""
men = Label(i, text = "Introduza os seus dados", foreground = "grey")
men.pack()

teste = Label(i, text = "Testando...", foreground = "orange")
teste.pack()


i.mainloop()
