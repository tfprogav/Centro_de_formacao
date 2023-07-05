from tkinter import * #Interface
from tkinter import ttk #Interface
from PIL import Image, ImageTk #Interface (imagens)
import database #Ficheiro com as querys sql
import mysql.connector #Para conectar á base de dados para não haver problemas
from tkinter import messagebox #Interface
from tkinter import simpledialog #Interface
import logic #Ficheiro com a lógica do programa

mydb = mysql.connector.connect( #Conexão á base de dados
        host="localhost",
        user="root",
        password="",
        database="tf_prog_av"
    )

root = Tk() #Criação da janela
root.title('Centro de formação')
root.geometry('1280x720+280+150')
root.resizable(FALSE, FALSE)


FONT = 'Arial 12'

button_styles = {
        'bg': '#008080',
        'fg': 'white',
        'activebackground': '#4C4C4C',
        'activeforeground': 'white',
        'font': FONT,
        'borderwidth': 0,
        'highlightthickness': 0,
        'relief': 'flat',
        'cursor': 'hand2',
    }

button_styles_mini_menu = {
        'bg': '#c9c9c9',
        'fg': 'black',
        'activebackground': '#4C4C4C',
        'activeforeground': 'white',
        'font': FONT,
        'borderwidth': 0,
        'highlightthickness': 0,
        'relief': 'flat',
        'cursor': 'hand2',
    }

main_frame = Frame(root, width=1280, height=720)
main_frame.pack(expand=True, fill='both')

def gestao_alunos():
    clear_content_frame(main_frame) #Eliminar tudo o conteúdo para adicionar os novos
    alunos = database.alunos() #Receber uma lista dos alunos criados
    def person_info():
        nome_aux = change_person.get()

        if nome_aux:
            password_origi = database.password_original(nome_aux) #Receber a password do aluno
            if password_origi:
                password = simpledialog.askstring("Senha", "Digite a sua senha:")
                if password is not None:
                    if password == password_origi: #Comparar a password do aluno com a inserida do utilizadorwww
                        person_curso() #Busca dos cursos do aluno

                        aluno_nome_aux = database.aluno_nome(nome_aux) #Busca dos dados do aluno
                        aluno_phone_aux = database.aluno_phone(nome_aux) #Busca dos dados do aluno
                        aluno_email_aux = database.aluno_email(nome_aux) #Busca dos dados do aluno

                        aluno_nome.set(f'Nome: {aluno_nome_aux}')
                        aluno_phone.set(f'Telemóvel: {aluno_phone_aux}')
                        aluno_email.set(f'Email: {aluno_email_aux}')

                    else:
                        messagebox.showerror('Erro!', 'Senha Incorreta')
            else:
                messagebox.showerror('Erro!', 'Erro na base de dados, por favor tente novamente mais tarde, obrigado')
        else:
            messagebox.showerror('Erro!', 'Selecione um aluno')

    def person_curso():
        info_person_courses.delete(0, last=6) #Reset na lista de cursos (texto)

        nome_selecionado = change_person.get()

        alunos_cursos_lista = logic.person_curso(nome_selecionado) #Vai buscar uma lista dos cursos do aluno

        for curso in alunos_cursos_lista: #Vai buscar o curso na lista de cursos do aluno e insere na ListBox 1 a 1
            info_person_courses.insert(END, curso)

    def delete_aluno():
        nome_aux = aluno_nome.get()
        nome_aux = nome_aux.removeprefix('Nome: ')

        logic.delete_aluno(nome_aux) #Elimina o aluno da Base de dados

    menu_frame = Frame(main_frame, bg='#383838', width=200, height=720) #Menu da esquerda
    menu_frame.pack(side='left', fill='y')

    button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles) #Botão do menu para aceder às outras páginas
    button1.pack(pady=10, padx=20, fill='x')

    button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles) #Botão do menu para aceder às outras páginas
    button2.pack(pady=10, padx=20, fill='x')

    button3 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles) #Botão do menu para aceder às outras páginas
    button3.pack(pady=10, padx=20, fill='both')

    button4 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles) #Botão do menu para aceder às outras páginas
    button4.pack(pady=10, padx=20, fill='x')

    button5 = Button(menu_frame, text='Performance de Alunos', **button_styles) #Botão do menu para aceder às outras páginas
    button5.pack(pady=10, padx=20, fill='x')

    LEFTFRAME = Frame(main_frame)#--------------------------------Frame da esquerda-------------------------------------
    LEFTFRAME.pack(side='left', padx=50, fill='both', expand=True)

    image_person_frame = Frame(LEFTFRAME)#--------------Frame da esquerda(Lado esquerdo do frame)parte com a imagem-----
    image_person_frame.pack(pady=20, side='left', anchor='n')

    icon_person_original = Image.open('person_icon.png').resize((200, 200)) #Imagem default
    icon_person_tk = ImageTk.PhotoImage(icon_person_original) #Imagem default

    icon_person = Label(image_person_frame, image=icon_person_tk) #Imagem default
    icon_person.pack(padx=10, pady=5)

    change_person = ttk.Combobox(image_person_frame, values=alunos, font='RArial 14', justify='center', state='readonly') #ComboBox com os nomes dos alunos
    change_person.pack(pady=5)

    select_button = ttk.Button(image_person_frame, text='Selecionar aluno acima', command=person_info, width=40) #Chamar a func
    select_button.pack(pady=5)

    delete_person = Button(image_person_frame, text='Eliminar Aluno', takefocus=False, cursor='hand2', font='Arial 12', bg='#87232d', fg='white', command=delete_aluno) #Chamar a func
    delete_person.pack(pady=10)

    info_person = Frame(LEFTFRAME)#--------------Frame da esquerda(Lado direito do frame)parte com as informações-------
    info_person.pack(pady=20, side='left', anchor='n')

    white_space = Label(info_person) #Margem
    white_space.pack(pady=5)

    aluno_nome = StringVar()
    aluno_phone = StringVar()
    aluno_email = StringVar()

    aluno_nome.set('Nome: ')
    aluno_phone.set('Telemóvel: ')
    aluno_email.set('Email: ')

    info_person_name = Label(info_person, textvariable=aluno_nome, font='Arial 16') #Nome do aluno
    info_person_name.pack(padx=30, pady=15, anchor='w')

    info_person_email = Label(info_person, textvariable=aluno_email, font='Arial 16') #Email do aluno
    info_person_email.pack(padx=30, pady=15, anchor='w')

    info_person_phone = Label(info_person, textvariable=aluno_phone, font='Arial 16') #Telemóvel do aluno
    info_person_phone.pack(padx=30, pady=15, anchor='w')

    white_space = Label(info_person) #Margem
    white_space.pack(pady=50)

    cursos_text = Label(info_person, text='Cursos Inscritos:', font='Arial 16') #Titulo
    cursos_text.pack(padx=30, pady=15, anchor='w')

    info_person_courses = Listbox(info_person, font='Arial 14', width=30, borderwidth=0, bg='white') #Lista com os cursos do aluno
    info_person_courses.pack(padx=30, pady=15, anchor='w')
    info_person_courses.bind("<Button-1>", logic.ignore_click) #Ao clicar num elemento da lista não acontece nada(readonly)

    RIGHTFRAME = Frame(main_frame)#--------------------------------Frame da direita-------------------------------------
    RIGHTFRAME.pack(side='left', fill='both', anchor='e', expand=True)

    menu_alunos = Frame(RIGHTFRAME, bg='#b3b5b4', width=150, height=50) #Menu próprio da gestão de alunos
    menu_alunos.pack(anchor='ne', expand=True)

    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu) #Botão do menu para aceder às outras páginas
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Alterar dados de Aluno', **button_styles_mini_menu, command=update_info_user) #Botão do menu para aceder às outras páginas
    button2.pack(pady=10, padx=10, fill='x')

    button3 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu, command=add_course) #Botão do menu para aceder às outras páginas
    button3.pack(pady=10, padx=10, fill='x')

    button4 = Button(menu_alunos, text='Remover Aluno de um Curso', **button_styles_mini_menu, command=remove_course) #Botão do menu para aceder às outras páginas
    button4.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Informação Pessoal', font='Arial 16 bold') #Titulo da página
    title_page.place(x=540, y=5)

    root.mainloop()

def update_info_user():#-----------------------------Página de atualizar dados do aluno---------------------------------
    clear_content_frame(main_frame)
    alunos = database.alunos()

    def person_info():
        nome_aux = change_person.get()

        if nome_aux:
            password_origi = database.password_original(nome_aux)

            if password_origi:
                password = simpledialog.askstring("Senha", "Digite a sua senha:")

                if password is not None:
                    if password == password_origi:

                        aluno_nome_aux = database.aluno_nome(nome_aux) #Busca dos dados do aluno
                        aluno_phone_aux = database.aluno_phone(nome_aux) #Busca dos dados do aluno
                        aluno_email_aux = database.aluno_email(nome_aux) #Busca dos dados do aluno
                        aluno_address_aux = database.aluno_address(nome_aux) #Busca dos dados do aluno

                        aluno_nome.set(f'Nome: {aluno_nome_aux}')
                        aluno_phone.set(f'Telemóvel: {aluno_phone_aux}')
                        aluno_email.set(f'Email: {aluno_email_aux}')
                        aluno_morada.set(f'Morada: {aluno_address_aux}')
                    else:
                        messagebox.showerror('Erro!', 'Senha Incorreta')
            else:
                messagebox.showerror('Erro!', 'Erro na base de dados, por favor tente novamente mais tarde, obrigado')
        else:
            messagebox.showerror('Erro!', 'Selecione um aluno')

    def update_info():

        nome = name_entry.get() #Dados do utilizador novos
        email = email_entry.get() #Dados do utilizador novos
        telemovel = phone_entry.get() #Dados do utilizador novos
        morada = address_entry.get() #Dados do utilizador novos

        nome_aux = aluno_nome.get() #Dados do utilizador antigos
        email_aux = aluno_email.get() #Dados do utilizador antigos
        phone_aux = aluno_phone.get() #Dados do utilizador antigos
        address_aux = aluno_morada.get() #Dados do utilizador antigos

        logic.update_info(nome_aux, nome, email, email_aux, telemovel, phone_aux, morada, address_aux)

    menu_frame = Frame(main_frame, bg='#383838', width=200, height=720)
    menu_frame.pack(side='left', fill='y')

    button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles)
    button1.pack(pady=10, padx=20, fill='x')

    button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles)
    button2.pack(pady=10, padx=20, fill='x')

    button3 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles)
    button3.pack(pady=10, padx=20, fill='both')

    button4 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles)
    button4.pack(pady=10, padx=20, fill='x')

    button5 = Button(menu_frame, text='Performance de Alunos', **button_styles)
    button5.pack(pady=10, padx=20, fill='x')

    LEFTFRAME = Frame(main_frame) #---------------------------------Frame da esquerda-----------------------------------
    LEFTFRAME.pack(side='left', padx=50, fill='both', expand=True)

    old_info_person_frame = Frame(LEFTFRAME) #----------Frame da esquerda(Lado esquerdo do frame)informação atual-------
    old_info_person_frame.pack(pady=20, side='left', anchor='n')

    white_space = Label(old_info_person_frame) #Margem
    white_space.pack(pady=5)

    title_old_info = Label(old_info_person_frame, text='Dados Atuais:', font='Arial 18 bold') #Titulo
    title_old_info.pack(pady=25)

    aluno_nome = StringVar()
    aluno_phone = StringVar()
    aluno_email = StringVar()
    aluno_morada = StringVar()

    aluno_nome.set('Nome: ')
    aluno_phone.set('Telemóvel: ')
    aluno_email.set('Email: ')
    aluno_morada.set('Morada: ')

    info_person_name = Label(old_info_person_frame, textvariable=aluno_nome, font='Arial 16') #Nome do aluno
    info_person_name.pack(padx=30, pady=25, anchor='w')

    info_person_email = Label(old_info_person_frame, textvariable=aluno_email, font='Arial 16') #Email do aluno
    info_person_email.pack(padx=30, pady=25, anchor='w')

    info_person_phone = Label(old_info_person_frame, textvariable=aluno_phone, font='Arial 16') #Telemóvel do aluno
    info_person_phone.pack(padx=30, pady=25, anchor='w')

    info_person_address = Label(old_info_person_frame, textvariable=aluno_morada, font='Arial 16') #Morada do aluno
    info_person_address.pack(padx=30, pady=25, anchor='w')

    change_person = ttk.Combobox(old_info_person_frame, values=alunos, font='RArial 14', justify='center', state='readonly') #Lista com os alunos
    change_person.pack(pady=15)

    select_button = ttk.Button(old_info_person_frame, text='Selecionar aluno acima', width=40, command=person_info) #Chamar a func
    select_button.pack(pady=5)

    new_info_person = Frame(LEFTFRAME)#--Frame da esquerda(Lado direito do frame)parte para inserir a nova informação---
    new_info_person.pack(pady=20, side='left', anchor='n')

    white_space = Label(new_info_person) #Margem
    white_space.pack(pady=5)

    title_new_info = Label(new_info_person, text='Novos dados:', font='Arial 18 bold') #Titulo
    title_new_info.pack(pady=25)

    name_entry = ttk.Entry(new_info_person, font='Arial 16') #Entrada para o nome
    name_entry.pack(padx=30, pady=25, anchor='w')

    email_entry = ttk.Entry(new_info_person, font='Arial 16') #Entrada para o email
    email_entry.pack(padx=30, pady=25, anchor='w')

    phone_entry = ttk.Entry(new_info_person, font='Arial 16') #Entrada para o telemóvel
    phone_entry.pack(padx=30, pady=25, anchor='w')

    address_entry = ttk.Entry(new_info_person, font='Arial 16') #Entrada para a morada
    address_entry.pack(padx=30, pady=25, anchor='w')

    update_button = Button(new_info_person, text='Atualizar dados', width=20, command=update_info, fg='white', bg='#6686ba', font=FONT, height=1, cursor='hand2') #Chamar a func
    update_button.pack(pady=25)

    RIGHTFRAME = Frame(main_frame)  # --------------------------------Frame da direita------------------------------------------
    RIGHTFRAME.pack(side='left', fill='both', anchor='e', expand=True)

    menu_alunos = Frame(RIGHTFRAME, bg='#b3b5b4', width=150, height=50) #Menu próprio da gestão de alunos
    menu_alunos.pack(anchor='ne', expand=True)

    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu, command=gestao_alunos)
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Alterar dados de Aluno', **button_styles_mini_menu)
    button2.pack(pady=10, padx=10, fill='x')

    button3 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu, command=add_course)
    button3.pack(pady=10, padx=10, fill='x')

    button4 = Button(menu_alunos, text='Remover Aluno de um Curso', **button_styles_mini_menu, command=remove_course)
    button4.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Alterar dados de Aluno', font='Arial 16 bold')
    title_page.place(x=540, y=5)


def add_course():#-----------------------------Adicionar aluno a um curso-------------------------
    clear_content_frame(main_frame)
    alunos = database.alunos()
    cursos = database.cursos()

    def cursoId():
        global cursoID
        cursoDesc = change_course.get()

        cursoDesc = logic.curso_desc_get(cursoDesc) #Formatar o nome do curso

        if cursoDesc:
            cursoID = database.course_id(cursoDesc) #Receber o id do curso
            return cursoID

        else:
            messagebox.showerror('Erro', 'Insira um curso')


    def alunoId():
        global alunoID
        personName = change_person.get()

        if personName:
            alunoID = database.aluno_id(personName) #Receber o id do aluno
            return alunoID

        else:
            messagebox.showerror('Erro', 'Insira um aluno')

    def insert_course():
        aluno_id = alunoId()
        curso_id = cursoId()

        cursoDesc = change_course.get()

        cursoDesc = logic.curso_desc_get(cursoDesc) #Formatar o nome do curso

        logic.insert_course(aluno_id, curso_id, cursoDesc) #Inserir aluno no curso

    menu_frame = Frame(main_frame, bg='#383838', width=200, height=720)
    menu_frame.pack(side='left', fill='y')

    button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles)
    button1.pack(pady=10, padx=20, fill='x')

    button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles)
    button2.pack(pady=10, padx=20, fill='x')

    button3 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles)
    button3.pack(pady=10, padx=20, fill='both')

    button4 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles)
    button4.pack(pady=10, padx=20, fill='x')

    button5 = Button(menu_frame, text='Performance de Alunos', **button_styles)
    button5.pack(pady=10, padx=20, fill='x')

    center_frame = Frame(main_frame) #--------------------------------Frame principal(lado esquerdo)--------------------
    center_frame.pack(side='left', fill='both', expand=True)

    white_space = Label(center_frame) #Margem
    white_space.pack(pady=45)

    person_title = Label(center_frame, text='Selecione o Aluno:', font='Arial 17') #Titulo
    person_title.pack()

    change_person = ttk.Combobox(center_frame, values=alunos, font='Arial 14', justify='center', state='readonly') #Lista com os alunos
    change_person.pack(pady=25)

    cursos_text = Label(center_frame, text='Selecione o Curso:', font='Arial 17') #Titulo
    cursos_text.pack()

    change_course = ttk.Combobox(center_frame, values=cursos, font='Arial 14', justify='center', state='readonly', width=30) #Lista com os cursos
    change_course.pack(pady=25)

    add_to_course = Button(center_frame, text='Adicionar Aluno ao Curso', fg='white', bg='green', font='Arial 16', cursor='hand2', command=insert_course) #Chamar a func
    add_to_course.pack(pady=25)

    RIGHTMENU_FRAME = Frame(main_frame) #--------------------------------Frame secundário(lado direito)-----------------
    RIGHTMENU_FRAME.pack(side='left', fill='both')

    menu_alunos = Frame(RIGHTMENU_FRAME, bg='#b3b5b4', width=150, height=50) #Menu próprio da gestão de alunos
    menu_alunos.pack(anchor='ne', expand=True)

    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu, command=gestao_alunos)
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Alterar dados de Aluno', **button_styles_mini_menu, command=update_info_user)
    button2.pack(pady=10, padx=10, fill='x')

    button3 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu)
    button3.pack(pady=10, padx=10, fill='x')

    button4 = Button(menu_alunos, text='Remover Aluno de um Curso', **button_styles_mini_menu, command=remove_course)
    button4.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Adicionar a Curso', font='Arial 16 bold')
    title_page.place(x=540, y=5)


def remove_course():
    clear_content_frame(main_frame)
    alunos = database.alunos()
    cursos = []

    def person_cursos(event):
        personName = change_person.get()
        cursos = logic.person_curso(personName)  # Vai buscar uma lista dos cursos do aluno
        change_course.configure(values=cursos) # Atualiza a lista dos cursos

    def cursoId():
        global cursoID
        cursoDesc = change_course.get()

        cursoDesc = logic.curso_desc_get(cursoDesc)

        if cursoDesc:
            cursoID = database.course_id(cursoDesc) #Receber o id do curso
            return cursoID

        else:
            messagebox.showerror('Erro', 'Insira um curso')

    def alunoId():
        global alunoID
        personName = change_person.get()

        if personName:
            alunoID = database.aluno_id(personName) #Receber o id do aluno
            return alunoID

        else:
            messagebox.showerror('Erro', 'Insira um aluno')

    def remove_course():
        aluno_id = alunoId()
        curso_id = cursoId()

        cursoDesc = change_course.get()

        cursoDesc = logic.curso_desc_get(cursoDesc)

        logic.remove_course(aluno_id, curso_id, cursoDesc) #Remover aluno do curso

    menu_frame = Frame(main_frame, bg='#383838', width=200, height=720)
    menu_frame.pack(side='left', fill='y')

    button1 = Button(menu_frame, text='Gestão de Utilizadores', **button_styles)
    button1.pack(pady=10, padx=20, fill='x')

    button2 = Button(menu_frame, text='Gestão de Alunos', **button_styles)
    button2.pack(pady=10, padx=20, fill='x')

    button3 = Button(menu_frame, text='Gestão de Aulas e Horários', **button_styles)
    button3.pack(pady=10, padx=20, fill='both')

    button4 = Button(menu_frame, text='Gestão de Pagamentos', **button_styles)
    button4.pack(pady=10, padx=20, fill='x')

    button5 = Button(menu_frame, text='Performance de Alunos', **button_styles)
    button5.pack(pady=10, padx=20, fill='x')

    center_frame = Frame(main_frame) #--------------------Frame principal(lado esquerdo)--------------------------------
    center_frame.pack(side='left', fill='both', expand=True)

    white_space = Label(center_frame) #Margem
    white_space.pack(pady=45)

    person_title = Label(center_frame, text='Selecione o Aluno:', font='Arial 17') #Titulo
    person_title.pack()

    change_person = ttk.Combobox(center_frame, values=alunos, font='Arial 14', justify='center', state='readonly') #Lista com os alunos
    change_person.pack(pady=25)
    change_person.bind("<<ComboboxSelected>>", person_cursos) #Ao mudar de aluno atualiza a lista dos cursos em que está inscrito

    cursos_text = Label(center_frame, text='Selecione o Curso:', font='Arial 17') #Titulo
    cursos_text.pack()

    change_course = ttk.Combobox(center_frame, values=cursos, font='Arial 14', justify='center', state='readonly', width=30) #Lista com os cursos
    change_course.pack(pady=25)


    add_to_course = Button(center_frame, text='Remover Aluno do Curso', fg='white', bg='red', font='Arial 16', cursor='hand2', command=remove_course) #Chamar a func
    add_to_course.pack(pady=25)

    RIGHTMENU_FRAME = Frame(main_frame) #--------------------------------Frame secundário(lado direito)-----------------
    RIGHTMENU_FRAME.pack(side='left', fill='both')

    menu_alunos = Frame(RIGHTMENU_FRAME, bg='#b3b5b4', width=150, height=50) #Menu próprio da gestão de alunos
    menu_alunos.pack(anchor='ne', expand=True)

    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu, command=gestao_alunos)
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Alterar dados de Aluno', **button_styles_mini_menu, command=update_info_user)
    button2.pack(pady=10, padx=10, fill='x')

    button3 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu, command=add_course)
    button3.pack(pady=10, padx=10, fill='x')

    button4 = Button(menu_alunos, text='Remover Aluno de um Curso', **button_styles_mini_menu)
    button4.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Remover do Curso', font='Arial 16 bold')
    title_page.place(x=540, y=5)


def clear_content_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy() #Destruir os elementos criados para quando ir para outra página adicionar e não subrepor os anteriores

if __name__ == '__main__':
    gestao_alunos()
