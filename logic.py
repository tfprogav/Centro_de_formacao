import database
from tkinter import messagebox
from tkinter import simpledialog

def person_curso(nome_selecionado):
    global id

    alunos_dict = database.alunos_id()

    for key, value in alunos_dict.items(): #Confirmar se o nome selecionado é igual ao retirado da base de dados, se sim**
        if value == nome_selecionado:
            id = key # **associa o seu id para a variavel id e executa a procura dos cursos por id

    alunos_cursos_lista = database.cursos_por_id(id) #Lista de cursos por id do aluno

    return alunos_cursos_lista


def delete_aluno(nome_aux):
    try:
        if nome_aux:
            response = messagebox.askyesno('Tem a certeza?', 'Tem a certeza que quer eliminar este aluno?')
            if response: #Se confirmar que quer eliminar
                database.delete_aluno(nome_aux) #Elimina o aluno
                messagebox.showinfo('Sucesso', 'O seu aluno foi eliminado')
            else:
                pass
        else:
            messagebox.showerror('Erro', 'Selecione um aluno antes de eliminá-lo')
    except:
        messagebox.showerror('Erro', 'Erro na base de dados, por favor tente novamente mais tarde, obrigado')


def ignore_click(event): #Ao clicar na lista de cursos não acontece nada(readonly)
    return "break"


def update_info(nome_aux, nome, email, email_aux, telemovel, phone_aux, morada, address_aux):
    data_change = 0
    nome_aux = nome_aux.removeprefix('Nome: ') #Formatação

    password_origi = database.password_original(nome_aux)

    password = simpledialog.askstring("Senha", "Digite a sua senha:")

    if password is not None:
        if password == password_origi:
            if nome:
                data_change = 1

                database.update_nome(nome, nome_aux) #Atualiza o nome

            if email:
                data_change = 1

                email_aux = email_aux.removeprefix('Email: ') #Formatação

                database.update_email(email, email_aux) #Atualiza o email

            if telemovel:
                data_change = 1

                phone_aux = phone_aux.removeprefix('Telemóvel: ') #Formatação

                database.update_phone(telemovel, phone_aux) #Atualiza o telemóvel

            if morada:
                data_change = 1

                address_aux = address_aux.removeprefix('Morada: ') #Formatação

                database.update_address(morada, address_aux) #Atualiza a morada

        else:
            messagebox.showerror('Erro!', 'Senha Incorreta')

        if data_change == 1: #Se algum dos campos foi atualizado aparece a seguinte mensagem:
            messagebox.showinfo('Sucesso', 'Os seus dados foram alterados!')
        elif data_change == 0:
            messagebox.showerror('Erro!', 'Nenhuma alteração foi inserida, verifique os novos dados')


def curso_desc_get(cursoDesc):
    cursoDesc = cursoDesc.split(' --- ') #Formatação
    cursoDesc = cursoDesc[0]
    return cursoDesc


def insert_course(aluno_id, curso_id, cursoDesc):
    found = database.verify_if_in_course(aluno_id, curso_id) #Verifica se o aluno está inscrito no curso

    if found:
        cursoInscrito = 1
    else:
        cursoInscrito = 0

    password_origi = database.password_original_por_id(aluno_id)

    password = simpledialog.askstring("Senha", "Digite a sua senha:")

    if password is not None:
        if password == password_origi:
            if cursoInscrito == 0: #Se não estiver inscrito**

                database.insert_in_course(aluno_id, curso_id) #**então inscreve o aluno

                messagebox.showinfo('Sucesso', f'O seu aluno foi inserido no curso: {cursoDesc}')
                messagebox.showinfo('Pagamento', 'Depois não se esqueça de pagar a incrição do curso..')
            else:
                messagebox.showerror('Erro', 'O aluno selecionado já está inscrito nesse curso!')
        else:
            messagebox.showerror('Erro!', 'Senha Incorreta')



def remove_course(aluno_id, curso_id, cursoDesc):
    found = database.verify_if_in_course(aluno_id, curso_id) #Verifica se o aluno está inscrito no curso

    if found:
        cursoInscrito = 1
    else:
        cursoInscrito = 0

    password_origi = database.password_original_por_id(aluno_id)

    password = simpledialog.askstring("Senha", "Digite a sua senha:")

    if password is not None:
        if password == password_origi:
            if cursoInscrito == 1: #Se estiver inscrito**

                database.remove_from_course(aluno_id, curso_id) #**então remove o aluno

                messagebox.showinfo('Sucesso', f'O seu aluno foi removido do curso: {cursoDesc}')

            else:
                messagebox.showerror('Erro', 'O aluno selecionado não está inscrito nesse curso!')
        else:
            messagebox.showerror('Erro!', 'Senha Incorreta')


def clear_content_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy() #Destruir os elementos criados para quando ir para outra página adicionar e não subrepor os anteriores