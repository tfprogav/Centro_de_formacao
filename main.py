from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #install pillow
import database
import mysql.connector
from tkinter import messagebox


def gestao_alunos():

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

    def person_info():
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
        mycursor = mydb.cursor()
        aluno = change_person.get()
        if aluno:
            response = messagebox.askyesno('Tem a certeza?', 'Tem a certeza que quer eliminar este aluno?')
            if response:
                mycursor.execute(f"DELETE FROM q_utilizadores WHERE utilizador_nome = '{aluno}'")
                mydb.commit()
                messagebox.showinfo('Sucesso', 'O seu aluno foi eliminado')
            else:
                pass
        else:
            messagebox.showerror('Erro', 'Selecione um aluno antes de eliminá-lo')



    main_frame = Frame(root, width=800, height=800)
    main_frame.pack(expand=True, fill='both')


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


    alunos = database.alunos()

    change_person = ttk.Combobox(image_person_frame, values=alunos, font='RArial 14', justify='center')
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




    RIGHTFRAME = Frame(main_frame)#--------------------------------rigth frame------------------------------------------
    RIGHTFRAME.pack(side='left', padx=50, fill='both', anchor='e', expand=True)



    menu_alunos = Frame(main_frame, bg='#b3b5b4', width=150, height=50)
    menu_alunos.pack(anchor='ne', expand=True)


    button1 = Button(menu_alunos, text='Informação Pessoal', **button_styles_mini_menu)
    button1.pack(pady=10, padx=10, fill='x')

    button2 = Button(menu_alunos, text='Adicionar Aluno a Curso', **button_styles_mini_menu)
    button2.pack(pady=10, padx=10, fill='x')

    title_page = Label(main_frame, text='Informação Pessoal', font='Arial 16 bold')
    title_page.place(x=540, y=5)

    root.mainloop()

if __name__ == '__main__':
    gestao_alunos()



