import database
from tkinter import messagebox
from tkinter import simpledialog

def person_curso(nome_selecionado):
    global id

    alunos_dict = database.alunos_id()

    for key, value in alunos_dict.items(): #Confirmar se o nome selecionado é igual ao retirado da base de dados se sim*
        if value == nome_selecionado:
            id = key # * Associa o seu id para a variavel id e executa a procura dos cursos por id

    alunos_cursos_lista = database.cursos_por_id(id)

    return alunos_cursos_lista


def delete_aluno(nome_aux):
    try:
        if nome_aux:
            response = messagebox.askyesno('Tem a certeza?', 'Tem a certeza que quer eliminar este aluno?')
            if response:
                database.delete_aluno(nome_aux)
                messagebox.showinfo('Sucesso', 'O seu aluno foi eliminado')
            else:
                pass
        else:
            messagebox.showerror('Erro', 'Selecione um aluno antes de eliminá-lo')
    except:
        messagebox.showerror('Erro', 'Erro na base de dados, por favor tente novamente mais tarde, obrigado')


def ignore_click(event):
    return "break"


def update_info(nome_aux, nome, email, email_aux, telemovel, phone_aux, morada, address_aux):
    data_change = 0
    password_origi = database.password_original(nome_aux)

    password = simpledialog.askstring("Senha", "Digite a sua senha:")

    if password is not None:
        if password == password_origi:
            if nome:
                data_change = 1

                database.update_nome(nome, nome_aux)

            if email:
                data_change = 1

                email_aux = email_aux.removeprefix('Email: ')

                database.update_email(email, email_aux)

            if telemovel:
                data_change = 1

                phone_aux = phone_aux.removeprefix('Telemóvel: ')

                database.update_phone(telemovel, phone_aux)

            if morada:
                data_change = 1

                address_aux = address_aux.removeprefix('Morada: ')

                database.update_address(morada, address_aux)

        else:
            messagebox.showerror('Erro!', 'Senha Incorreta')

        if data_change == 1:
            messagebox.showinfo('Sucesso', 'Os seus dados foram alterados!')
        elif data_change == 0:
            messagebox.showerror('Erro!', 'Nenhuma alteração foi inserida, verifique os novos dados')


def curso_desc_get(cursoDesc):
    cursoDesc = cursoDesc.split(' --- ')
    cursoDesc = cursoDesc[0]
    return cursoDesc