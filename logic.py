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