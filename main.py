from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #install pillow
import database
import mysql.connector

menu_x = 0

def gestao_alunos():

    root = Tk()
    root.title('Centro de formação')
    root.geometry('1280x720+280+150')
    root.resizable(0, 0)

    FONT = 'Roboto 12'
    BG = '#545454'


    def movemenu():
        global menu_x
        menu_x += 0.001
        menu_panel.place(relx=menu_x, rely=0.095)

        if menu_x < 0.1625:
            root.after(1, movemenu)
        hamburguer_button.configure(command=goback)
        hamburguer_button.configure(image=goBack_tk)

    def goback():
        global menu_x
        menu_x -= 0.001
        menu_panel.place(relx=menu_x, rely=0.095)

        if menu_x > -0.1625:
            root.after(1, goback)
        hamburguer_button.configure(command=movemenu)
        hamburguer_button.configure(image=hamburguer_tk)


    def person_info():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tf_prog_av"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM q_alunos")

        q_alunos = mycursor.fetchall()
        nome_selecionado = change_person.get()
        for rows in q_alunos:
            if rows[1] == nome_selecionado:
                aluno_nome_aux = rows[1]
                aluno_phone_aux = rows[2]
                aluno_email_aux = rows[3]
                aluno_nome.set(f'Nome: {aluno_nome_aux}')
                aluno_phone.set(f'Telemóvel: {aluno_phone_aux}')
                aluno_email.set(f'Email: {aluno_email_aux}')

    main_frame = Frame(root, width=800, height=800)
    main_frame.pack(expand=True, fill='both')

    LEFTFRAME = Frame(main_frame) #--------------------------------left frame------------------------------
    LEFTFRAME.pack(side='left', padx=50, fill='both')

    image_person_frame = Frame(LEFTFRAME) #--------------------------------left frame image section--------
    image_person_frame.pack(pady=20, side='left', fill='both')

    icon_person_original = Image.open('person_icon.png').resize((200, 200))
    icon_person_tk = ImageTk.PhotoImage(icon_person_original)

    icon_person = Label(image_person_frame, image=icon_person_tk)
    icon_person.pack(padx=10, pady=5)


    alunos = database.alunos()

    change_person = ttk.Combobox(image_person_frame, values=alunos, font='Roboto 14', justify='center')
    change_person.pack(pady=5)

    select_button = ttk.Button(image_person_frame, text='Selecionar aluno acima', command=person_info, width=40)
    select_button.pack(pady=5)






    info_person = Frame(LEFTFRAME)#--------------------------------left frame info section--------
    info_person.pack(pady=20, side='left', fill='both')

    white_space = Label(info_person)
    white_space.pack(pady=5)

    aluno_nome = StringVar()
    aluno_phone = StringVar()
    aluno_email = StringVar()

    aluno_nome.set('Nome: ')
    aluno_phone.set('Telemóvel: ')
    aluno_email.set('Email: ')

    info_person_name = Label(info_person, textvariable=aluno_nome, font='Roboto 16')
    info_person_name.pack(padx=30, pady=15, anchor='w')

    info_person_email = Label(info_person, textvariable=aluno_email, font='Roboto 16')
    info_person_email.pack(padx=30, pady=15, anchor='w')

    info_person_phone = Label(info_person, textvariable=aluno_phone, font='Roboto 16')
    info_person_phone.pack(padx=30, pady=15, anchor='w')




    RIGHTFRAME = Frame(main_frame)#--------------------------------rigth frame------------------------------
    RIGHTFRAME.pack(side='left', padx=50, fill='both')









    # menu
    menu_panel = Frame(main_frame, bg='grey')
    menu_panel.place(x=-210, y=0.01)

    button1 = Button(menu_panel, text='Gestão de Utilizadores', takefocus=False, borderwidth=0,
                     fg='white', anchor='w', font=FONT, cursor='hand2', bg=BG)
    button1.pack(pady=5, fill='both', anchor='e')

    button2 = Button(menu_panel, text='Gestão de alunos', takefocus=False, borderwidth=0, fg='white',
                     anchor='w', font=FONT, cursor='hand2', bg=BG)
    button2.pack(pady=5, fill='both')

    button3 = Button(menu_panel, text='Gestão de aulas e horários', takefocus=False, borderwidth=0,
                     fg='white', anchor='w', font=FONT, cursor='hand2', bg=BG)
    button3.pack(pady=5, fill='both')

    button4 = Button(menu_panel, text='Gestão de pagamentos', takefocus=False, borderwidth=0, fg='white',
                     anchor='w', font=FONT, cursor='hand2', bg=BG)
    button4.pack(pady=5, fill='both')

    button5 = Button(menu_panel, text='Performance de alunos', takefocus=False, borderwidth=0, fg='white',
                     anchor='w', font=FONT, cursor='hand2', bg=BG)
    button5.pack(pady=5, fill='both')

    # hambuerguer menu
    hamburguer_original = Image.open('menu_hamburguer.png').resize((35, 35))
    hamburguer_tk = ImageTk.PhotoImage(hamburguer_original)

    goBack_original = Image.open('go_back.png').resize((35, 35))
    goBack_tk = ImageTk.PhotoImage(goBack_original)

    hamburguer_button = Button(main_frame, image=hamburguer_tk, takefocus=False,
                               borderwidth=0, cursor='hand2', command=movemenu)
    hamburguer_button.place(x=5, y=5, bordermode='ignore')

    root.mainloop()

if __name__ == '__main__':
    gestao_alunos()



