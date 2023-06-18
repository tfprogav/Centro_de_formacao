from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #install pillow


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



    main_frame = Frame(root, width=800, height=800)
    main_frame.pack(expand=True, fill='both')


    LEFTFRAME = Frame(main_frame)                  #left frame
    LEFTFRAME.pack(side='left', padx=50, fill='both')



    image_person = Frame(LEFTFRAME)
    image_person.pack(pady=20, side='left', fill='both')

    icon_person_original = Image.open('person_icon.png').resize((200, 200))
    icon_person_tk = ImageTk.PhotoImage(icon_person_original)

    icon_person = Label(image_person, image=icon_person_tk)
    icon_person.pack(padx=10)




    info_person = Frame(LEFTFRAME)
    info_person.pack(pady=20, side='left', fill='both')

    white_space = Label(info_person)
    white_space.pack(pady=5)

    info_person_name = Label(info_person, text='Nome: André', font='Roboto 18')
    info_person_name.pack(padx=30, pady=15)

    info_person_email = Label(info_person, text='Email: andremontoito@gmail.com', font='Roboto 18')
    info_person_email.pack(padx=30, pady=15)




    RIGHTFRAME = Frame(main_frame)                  #rigth frame
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



