from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #install pillow
import database
import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tf_prog_av"
    )

root = Tk()
root.title('Centro de formação')
root.geometry('1280x720+280+150')
root.resizable(0, 0)


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
    clear_content_frame(main_frame)
    alunos = database.alunos()
    def person_info():
        password_origi = None
        mycursor = mydb.cursor()
        nome_aux = change_person.get()

        if nome_aux:
            mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")

            password_in_lista = mycursor.fetchall()
            for row in password_in_lista:
                password_origi = row[0]

            if password_origi:

                password = simpledialog.askstring("Senha", "Digite a sua senha:")

                if password is not None:
                    if password == password_origi:
                        person_curso()
                        mycursor = mydb.cursor()

                        mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

                        q_alunos = mycursor.fetchall()
                        nome_selecionado = change_person.get()
                        for rows in q_alunos:
                            if rows[1] == nome_selecionado:
                                aluno_nome_aux = rows[1]
                                aluno_email_aux = rows[2]
                                aluno_phone_aux = rows[3]
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
        info_person_courses.delete(0, last=6)

        nome_selecionado = change_person.get()
        mycursor = mydb.cursor()
        alunos_dict = database.alunos_id()

        for key, value in alunos_dict.items():
            if value == nome_selecionado:
                id = key
        mycursor.execute(
            f"SELECT q_utilizadores.utilizador_id, q_cursos.curso_desc FROM q_utilizadores JOIN q_alunos_cursos ON q_utilizadores.utilizador_id = q_alunos_cursos.aluno_id JOIN q_cursos ON q_alunos_cursos.curso_id = q_cursos.curso_id WHERE q_utilizadores.utilizador_id = {id};")

        cursos_alunos = mycursor.fetchall()

        alunos_cursos_lista = []
        for row in cursos_alunos:
            curso_desc = row[1]
            alunos_cursos_lista.append(curso_desc)

        for value in alunos_cursos_lista:
            info_person_courses.insert(END, value)
        return alunos_cursos_lista


    def delete_aluno():

        nome_aux = aluno_nome.get()
        nome_aux = nome_aux.removeprefix('Nome: ')

        mycursor = mydb.cursor()

        if nome_aux:
            response = messagebox.askyesno('Tem a certeza?', 'Tem a certeza que quer eliminar este aluno?')
            if response:
                mycursor.execute(f"DELETE FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")
                mydb.commit()
                messagebox.showinfo('Sucesso', 'O seu aluno foi eliminado')
            else:
                pass
        else:
            messagebox.showerror('Erro', 'Selecione um aluno antes de eliminá-lo')

    def ignore_click(event):
        return "break"

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



    LEFTFRAME = Frame(main_frame) #--------------------------------left frame---------------------------------
    LEFTFRAME.pack(side='left', padx=50, fill='both', expand=True)

    image_person_frame = Frame(LEFTFRAME) #--------------------------------left frame(left side) image section----------
    image_person_frame.pack(pady=20, side='left', anchor='n')

    icon_person_original = Image.open('person_icon.png').resize((200, 200))
    icon_person_tk = ImageTk.PhotoImage(icon_person_original)

    icon_person = Label(image_person_frame, image=icon_person_tk)
    icon_person.pack(padx=10, pady=5)




    change_person = ttk.Combobox(image_person_frame, values=alunos, font='RArial 14', justify='center', state='readonly')
    change_person.pack(pady=5)

    select_button = ttk.Button(image_person_frame, text='Selecionar aluno acima', command=person_info, width=40)
    select_button.pack(pady=5)

    delete_person = Button(image_person_frame, text='Eliminar Aluno', takefocus=False, cursor='hand2', font='Arial 12',
                           bg='#87232d', fg='white', command=delete_aluno)
    delete_person.pack(pady=10)


    info_person = Frame(LEFTFRAME)#--------------------------------left frame(right side) info section------------------
    info_person.pack(pady=20, side='left', anchor='n')

    white_space = Label(info_person)
    white_space.pack(pady=5)

    aluno_nome = StringVar()
    aluno_phone = StringVar()
    aluno_email = StringVar()


    aluno_nome.set('Nome: ')
    aluno_phone.set('Telemóvel: ')
    aluno_email.set('Email: ')

    info_person_name = Label(info_person, textvariable=aluno_nome, font='Arial 16')
    info_person_name.pack(padx=30, pady=15, anchor='w')

    info_person_email = Label(info_person, textvariable=aluno_email, font='Arial 16')
    info_person_email.pack(padx=30, pady=15, anchor='w')

    info_person_phone = Label(info_person, textvariable=aluno_phone, font='Arial 16')
    info_person_phone.pack(padx=30, pady=15, anchor='w')

    white_space = Label(info_person)
    white_space.pack(pady=50)




    cursos_text = Label(info_person, text='Cursos Inscritos:', font='Arial 16')
    cursos_text.pack(padx=30, pady=15, anchor='w')



    info_person_courses = Listbox(info_person, font='Arial 14', width=30, borderwidth=0)
    info_person_courses.pack(padx=30, pady=15, anchor='w')
    info_person_courses.bind("<Button-1>", ignore_click)




    RIGHTFRAME = Frame(main_frame)#--------------------------------rigth frame------------------------------------------
    RIGHTFRAME.pack(side='left', fill='both', anchor='e', expand=True)



    menu_alunos = Frame(RIGHTFRAME, bg='#b3b5b4', width=150, height=50)
    menu_alunos.pack(anchor='ne', expand=True)


    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu)
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Alterar dados de Aluno', **button_styles_mini_menu, command=update_info_user)
    button2.pack(pady=10, padx=10, fill='x')

    button3 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu, command=add_course)
    button3.pack(pady=10, padx=10, fill='x')

    button4 = Button(menu_alunos, text='Remover Aluno de um Curso', **button_styles_mini_menu, command=remove_course)
    button4.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Informação Pessoal', font='Arial 16 bold')
    title_page.place(x=540, y=5)

    root.mainloop()



def update_info_user(): #-----------------------------add course-------------------------
    clear_content_frame(main_frame)
    alunos = database.alunos()

    def person_info():
        password_origi = None
        mycursor = mydb.cursor()
        nome_aux = change_person.get()

        if nome_aux:
            mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")

            password_in_lista = mycursor.fetchall()
            for row in password_in_lista:
                password_origi = row[0]

            if password_origi:
                password = simpledialog.askstring("Senha", "Digite a sua senha:")

                if password is not None:
                    if password == password_origi:
                        mycursor = mydb.cursor()

                        mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

                        q_alunos = mycursor.fetchall()
                        nome_selecionado = change_person.get()
                        for rows in q_alunos:
                            if rows[1] == nome_selecionado:
                                aluno_nome_aux = rows[1]
                                aluno_email_aux = rows[2]
                                aluno_phone_aux = rows[3]
                                aluno_address_aux = rows[4]
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
        password_origi = None
        data_change = 0

        nome = name_entry.get()
        email = email_entry.get()
        telemovel = phone_entry.get()
        morada = address_entry.get()

        nome_aux = aluno_nome.get()
        nome_aux = nome_aux.removeprefix('Nome: ')

        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")

        password_in_lista = mycursor.fetchall()
        for row in password_in_lista:
            password_origi = row[0]

        password = simpledialog.askstring("Senha", "Digite a sua senha:")

        if password is not None:
            if password == password_origi:
                if nome:
                    data_change = 1
                    mycursor = mydb.cursor()

                    mycursor.execute(
                        f"UPDATE q_utilizadores SET utilizador_nome = '{nome}' WHERE utilizador_nome = '{nome_aux}'")

                    mydb.commit()

                if email:
                    data_change = 1
                    email_aux = aluno_email.get()
                    email_aux = email_aux.removeprefix('Email: ')

                    mycursor = mydb.cursor()

                    mycursor.execute(
                        f"UPDATE q_utilizadores SET utilizador_email = '{email}' WHERE utilizador_email = '{email_aux}'")

                    mydb.commit()

                if telemovel:
                    data_change = 1
                    phone_aux = aluno_phone.get()
                    phone_aux = phone_aux.removeprefix('Telemóvel: ')

                    mycursor = mydb.cursor()

                    mycursor.execute(
                        f"UPDATE q_utilizadores SET utilizador_contacto = '{telemovel}' WHERE utilizador_contacto = '{phone_aux}'")

                    mydb.commit()

                if morada:
                    data_change = 1
                    address_aux = aluno_morada.get()
                    address_aux = address_aux.removeprefix('Morada: ')

                    mycursor = mydb.cursor()

                    mycursor.execute(
                        f"UPDATE q_utilizadores SET utilizador_morada = '{morada}' WHERE utilizador_morada = '{address_aux}'")

                    mydb.commit()
            else:
                messagebox.showerror('Erro!', 'Senha Incorreta')

            if data_change == 1:
                messagebox.showinfo('Sucesso', 'Os seus dados foram alterados!')
            elif data_change == 0:
                messagebox.showerror('Erro!', 'Nenhuma alteração foi inserida, verifique os novos dados')




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

    LEFTFRAME = Frame(main_frame)  # --------------------------------left frame---------------------------------
    LEFTFRAME.pack(side='left', padx=50, fill='both', expand=True)

    old_info_person_frame = Frame(LEFTFRAME)  # --------------------------------left frame(left side) image section----------
    old_info_person_frame.pack(pady=20, side='left', anchor='n')




    white_space = Label(old_info_person_frame)
    white_space.pack(pady=5)


    title_old_info = Label(old_info_person_frame, text='Dados Atuais:', font='Arial 18 bold')
    title_old_info.pack(pady=25)


    aluno_nome = StringVar()
    aluno_phone = StringVar()
    aluno_email = StringVar()
    aluno_morada = StringVar()

    aluno_nome.set('Nome: ')
    aluno_phone.set('Telemóvel: ')
    aluno_email.set('Email: ')
    aluno_morada.set('Morada: ')

    info_person_name = Label(old_info_person_frame, textvariable=aluno_nome, font='Arial 16')
    info_person_name.pack(padx=30, pady=25, anchor='w')

    info_person_email = Label(old_info_person_frame, textvariable=aluno_email, font='Arial 16')
    info_person_email.pack(padx=30, pady=25, anchor='w')

    info_person_phone = Label(old_info_person_frame, textvariable=aluno_phone, font='Arial 16')
    info_person_phone.pack(padx=30, pady=25, anchor='w')

    info_person_address = Label(old_info_person_frame, textvariable=aluno_morada, font='Arial 16')
    info_person_address.pack(padx=30, pady=25, anchor='w')



    change_person = ttk.Combobox(old_info_person_frame, values=alunos, font='RArial 14', justify='center',state='readonly')
    change_person.pack(pady=15)

    select_button = ttk.Button(old_info_person_frame, text='Selecionar aluno acima', width=40, command=person_info)
    select_button.pack(pady=5)


    new_info_person = Frame(LEFTFRAME)  # --------------------------------left frame(right side) info section------------------
    new_info_person.pack(pady=20, side='left', anchor='n')

    white_space = Label(new_info_person)
    white_space.pack(pady=5)

    title_new_info = Label(new_info_person, text='Novos dados:', font='Arial 18 bold')
    title_new_info.pack(pady=25)


    name_entry = ttk.Entry(new_info_person, font='Arial 16')
    name_entry.pack(padx=30, pady=25, anchor='w')

    email_entry = ttk.Entry(new_info_person, font='Arial 16')
    email_entry.pack(padx=30, pady=25, anchor='w')

    phone_entry = ttk.Entry(new_info_person, font='Arial 16')
    phone_entry.pack(padx=30, pady=25, anchor='w')

    address_entry = ttk.Entry(new_info_person, font='Arial 16')
    address_entry.pack(padx=30, pady=25, anchor='w')

    update_button = Button(new_info_person, text='Atualizar dados', width=20, command=update_info, fg='white', bg='#6686ba', font=FONT, height=1, cursor='hand2')
    update_button.pack(pady=25)


    RIGHTFRAME = Frame(main_frame)  # --------------------------------rigth frame------------------------------------------
    RIGHTFRAME.pack(side='left', fill='both', anchor='e', expand=True)

    menu_alunos = Frame(RIGHTFRAME, bg='#b3b5b4', width=150, height=50)
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



def add_course(): #-----------------------------add course-------------------------
    clear_content_frame(main_frame)
    alunos = database.alunos()
    cursos = database.cursos()

    def cursoId():
        global cursoID
        cursoDesc = change_course.get()
        cursoDesc = cursoDesc.split(' --- ')
        cursoDesc = cursoDesc[0]

        if cursoDesc:
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT curso_id FROM q_cursos WHERE curso_desc = '{cursoDesc}'")

            q_curso_id = mycursor.fetchall()
            for row in q_curso_id:
                cursoID = row[0]

            return cursoID

        else:
            messagebox.showerror('Erro', 'Insira um curso')

    def alunoId():
        global alunoID
        personName = change_person.get()

        if personName:
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT utilizador_id FROM q_utilizadores WHERE utilizador_nome = '{personName}'")

            q_aluno_id = mycursor.fetchall()
            for row in q_aluno_id:
                alunoID = row[0]
            return alunoID
        else:
            messagebox.showerror('Erro', 'Insira um aluno')


    def insert_course():
        global password_origi
        aluno_id = alunoId()
        curso_id = cursoId()
        cursoDesc = change_course.get()
        cursoDesc = cursoDesc.split(' --- ')
        cursoDesc = cursoDesc[0]
        cursoInscrito = 0

        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT aluno_id, curso_id FROM q_alunos_cursos WHERE aluno_id = {aluno_id} AND curso_id = {curso_id}")
        found = mycursor.fetchall()

        if found:
            cursoInscrito = 1
        else:
            cursoInscrito = 0

        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_id = '{aluno_id}'")

        password_in_lista = mycursor.fetchall()
        for row in password_in_lista:
            password_origi = row[0]

        password = simpledialog.askstring("Senha", "Digite a sua senha:")

        if password is not None:
            if password == password_origi:
                if cursoInscrito == 0:
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        f"INSERT INTO q_alunos_cursos (aluno_id, curso_id) VALUES ({aluno_id}, {curso_id})")
                    mydb.commit()
                    messagebox.showinfo('Sucesso', f'O seu aluno foi inserido no curso: {cursoDesc}')
                    messagebox.showinfo('Pagamento', 'Depois não se esqueça de pagar a incrição do curso..')
                else:
                    messagebox.showerror('Erro', 'O aluno selecionado já está inscrito nesse curso!')
            else:
                messagebox.showerror('Erro!', 'Senha Incorreta')


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


    center_frame = Frame(main_frame)  # --------------------------------left frame---------------------------------
    center_frame.pack(side='left', fill='both', expand=True)



    white_space = Label(center_frame)
    white_space.pack(pady=45)




    person_title = Label(center_frame, text= 'Selecione o Aluno:', font='Arial 17')
    person_title.pack()

    change_person = ttk.Combobox(center_frame, values=alunos, font='Arial 14', justify='center', state='readonly')
    change_person.pack(pady=25)


    cursos_text = Label(center_frame, text='Selecione o Curso:', font='Arial 17')
    cursos_text.pack()

    change_course = ttk.Combobox(center_frame, values=cursos, font='Arial 14', justify='center', state='readonly', width=30)
    change_course.pack(pady=25)



    add_to_course = Button(center_frame, text='Adicionar Aluno ao Curso', fg='white', bg='green', font='Arial 16', cursor='hand2', command=insert_course)
    add_to_course.pack(pady=25)

    RIGHTMENU_FRAME = Frame(main_frame)
    RIGHTMENU_FRAME.pack(side='left', fill='both')

    menu_alunos = Frame(RIGHTMENU_FRAME, bg='#b3b5b4', width=150, height=50)
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
    cursos = database.cursos()

    def cursoId():
        global cursoID
        cursoDesc = change_course.get()
        cursoDesc = cursoDesc.split(' --- ')
        cursoDesc = cursoDesc[0]

        if cursoDesc:
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT curso_id FROM q_cursos WHERE curso_desc = '{cursoDesc}'")

            q_curso_id = mycursor.fetchall()
            for row in q_curso_id:
                cursoID = row[0]

            return cursoID

        else:
            messagebox.showerror('Erro', 'Insira um curso')

    def alunoId():
        global alunoID
        personName = change_person.get()

        if personName:
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT utilizador_id FROM q_utilizadores WHERE utilizador_nome = '{personName}'")

            q_aluno_id = mycursor.fetchall()
            for row in q_aluno_id:
                alunoID = row[0]
            return alunoID
        else:
            messagebox.showerror('Erro', 'Insira um aluno')

    def remove_course():
        global password_origi
        aluno_id = alunoId()
        curso_id = cursoId()
        cursoDesc = change_course.get()
        cursoDesc = cursoDesc.split(' --- ')
        cursoDesc = cursoDesc[0]
        cursoInscrito = 0

        mycursor = mydb.cursor()
        mycursor.execute(
            f"SELECT aluno_id, curso_id FROM q_alunos_cursos WHERE aluno_id = {aluno_id} AND curso_id = {curso_id}")
        found = mycursor.fetchall()

        if found:
            cursoInscrito = 1
        else:
            cursoInscrito = 0

        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_id = '{aluno_id}'")

        password_in_lista = mycursor.fetchall()
        for row in password_in_lista:
            password_origi = row[0]

        password = simpledialog.askstring("Senha", "Digite a sua senha:")

        if password is not None:
            if password == password_origi:
                if cursoInscrito == 1:
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        f"DELETE FROM q_alunos_cursos WHERE aluno_id = ({aluno_id} AND curso_id = {curso_id})")
                    mydb.commit()
                    messagebox.showinfo('Sucesso', f'O seu aluno foi removido do curso: {cursoDesc}')

                else:
                    messagebox.showerror('Erro', 'O aluno selecionado não está inscrito nesse curso!')
            else:
                messagebox.showerror('Erro!', 'Senha Incorreta')


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

    center_frame = Frame(main_frame)  # --------------------------------left frame---------------------------------
    center_frame.pack(side='left', fill='both', expand=True)

    white_space = Label(center_frame)
    white_space.pack(pady=45)

    person_title = Label(center_frame, text='Selecione o Aluno:', font='Arial 17')
    person_title.pack()

    change_person = ttk.Combobox(center_frame, values=alunos, font='Arial 14', justify='center', state='readonly')
    change_person.pack(pady=25)

    cursos_text = Label(center_frame, text='Selecione o Curso:', font='Arial 17')
    cursos_text.pack()

    change_course = ttk.Combobox(center_frame, values=cursos, font='Arial 14', justify='center', state='readonly',
                                 width=30)
    change_course.pack(pady=25)

    add_to_course = Button(center_frame, text='Remover Aluno do Curso', fg='white', bg='red', font='Arial 16',
                           cursor='hand2', command=remove_course)
    add_to_course.pack(pady=25)

    RIGHTMENU_FRAME = Frame(main_frame)
    RIGHTMENU_FRAME.pack(side='left', fill='both')

    menu_alunos = Frame(RIGHTMENU_FRAME, bg='#b3b5b4', width=150, height=50)
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
        widget.destroy()

if __name__ == '__main__':
    gestao_alunos()



