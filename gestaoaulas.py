from tkinter import Label, ttk, Frame, Entry, Button, Text, Spinbox, messagebox, Scrollbar, Tk, Listbox, MULTIPLE, END
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import datetime
from edicaoaulas import janela_consultar_aulas
#
import mysql.connector
mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="",
database="tf_prog_av"
)

aluno_ids_string = ""
curso_id = ""

#É criada a função gestao_aulas que irá ser executada na frame content_frame
def gestao_aulas(content_frame):
    content_frame.configure(bg="#F0F0F0")
    global curso_id

    # A cada execução da função são destruídos os widgets existentes na frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    #É criado o frame_gestao_a que fará parte de content_frame
    frame_gestao_a = Frame(content_frame)
    frame_gestao_a.pack()

    label = Label(frame_gestao_a, text="Gestão de Aulas", font=('Arial', 14, "bold"))
    label.pack()

    # É criado um objeto cursor que irá ser utilizado para aceder à BD
    mycursor = mydb.cursor()

    #É executada a query abaixo
    mycursor.execute("""
    SELECT q_cursos.curso_id, q_cursos.curso_desc, q_cursos.curso_horas, q_cursos.curso_preco, 
           COUNT(q_alunos_cursos.aluno_id) AS num_alunos,
           TIME_FORMAT(SEC_TO_TIME(SUM(TIME_TO_SEC(TIMEDIFF(q_aulas.aula_termino, q_aulas.aula_inicio)))), '%H:%i') AS horas_ministradas
    FROM q_cursos
    LEFT JOIN q_alunos_cursos ON q_cursos.curso_id = q_alunos_cursos.curso_id
    LEFT JOIN q_aulas ON q_cursos.curso_id = q_aulas.aulas_curso_id
    GROUP BY q_cursos.curso_id, q_cursos.curso_desc, q_cursos.curso_horas, q_cursos.curso_preco
""")

    #Os resultados da query serão passados à variável resultados
    resultados = mycursor.fetchall()

    #É criada a frame frametreeview
    frametreeview = Frame(frame_gestao_a)
    frametreeview.pack()

    #É criada uma TReeview e as correspondentes colunas e cabeçalhos
    tabela = ttk.Treeview(frametreeview, columns=("Descricao", "Horas", "Preco", "Numero de Alunos", "Horas Ministradas"), height=6)
    tabela.heading("#0", text="Numero do Curso")
    tabela.heading("Descricao", text="Descrição do Curso")
    tabela.heading("Horas", text="Horas")
    tabela.heading("Preco", text="Preço")
    tabela.heading("Numero de Alunos", text="Número de Alunos")
    tabela.heading("Horas Ministradas", text="Horas Ministradas")
    tabela.pack(pady=10)

    #É criada e associada uma scrollbar à treeview
    scrollbar = Scrollbar(frametreeview, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)

    #É executado o pack de ambos os widgets
    tabela.pack(side="left", fill="y")
    scrollbar.pack(side="right", fill="y")

    #São inseridas na tabela os valores correspondentes a cada coluna
    for item in resultados:

        #Se o valor de item[5] não for none irá receber o valor correspondente na BD, caso seja none irá receber o valor 0
        horas_ministradas = item[5] if item[5] is not None else "0"
        tabela.insert("", "end", text=item[0], values=(item[1], item[2], item[3], item[4], horas_ministradas))

    #São definidas as configurações das diferentes colunas
    tabela.column("#0", anchor="center", width=150)

    for column in tabela["columns"]:
        tabela.column(column, anchor="center", width=150)

    #É criado o botão que chama a função para a criação de aulas
    botao_marc_aulas = Button(frame_gestao_a, text="Marcação de Aulas", command=lambda: criar_aulas(frame_sec_a), font=('Arial',9, 'bold'))
    botao_marc_aulas.pack(pady=5)

    #É criada a função que permite consultar e editar aulas
    def consultar_editar_aulas():

        #É feita a tentativa de acesso à Treeview
        selected_item = tabela.focus()

        #Se não tiver sido nenhuma opção seleccionada é apresentada uma mensagem de error
        if not selected_item:
            messagebox.showerror("Erro", "Para consultar as aulas por favor seleccione um curso.")
            return

        #Caso haja alguma linha seleccionada na tabela o seu conteúdo é passado a selected_item
        curso_id = tabela.item(selected_item)["text"]

        #É passado o valor de curso_id à função janela_consultar_aulas
        janela_consultar_aulas(curso_id)



    #É criado o botão que chama a função consultar_editar_aulas
    consultar_editar_button = Button(frame_gestao_a, text="Consultar / Editar Aulas", command=consultar_editar_aulas, font=('Arial',9, 'bold'))
    consultar_editar_button.pack(pady=5)

    #É criada uma frame intermedia na frame content_frame (a próxima frame utilizará o método grid em vez de pack)
    frame_intermedia = Frame(content_frame)
    frame_intermedia.pack()

    #É criada a frame frame_sec_a em frame_intermedia (método grid)
    frame_sec_a = Frame(frame_intermedia)
    frame_sec_a.grid(row=1, column=0, padx=10, pady=10)

    #É criada a função criar_aulas
    def criar_aulas(frame_sec_a):

        #É criada a função ativar_fim_aula, que fará a ativação dos widgets relativos ao final da aula calendário e hora e minutos
        def ativar_fim_aula():
            data_fim_picker.configure(state="normal")
            hora_fim_spinbox.configure(state="normal")
            minutos_fim_spinbox.configure(state="normal")

        #Criados widgets Label e Entry
        title_label = Label(frame_sec_a, text="Resumo Aula")
        title_label.grid(row=2, column=0, columnspan=9, sticky="we", pady=2)

        title_entry = Entry(frame_sec_a)
        title_entry.grid(row=3, column=0, columnspan=9, sticky="we")

        #Widget Label
        professor_label = Label(frame_sec_a, text="Selecionar Docente")
        professor_label.grid(row=4, column=0, columnspan=9, sticky="we", pady=2)

        # É criado um objeto cursor que irá ser utilizado para aceder à BD
        cursor = mydb.cursor()

        #Executa a query que irá receber os dados dos professores
        query = "SELECT CONCAT(utilizador_id, ' - ', utilizador_nome) AS professor_info FROM q_utilizadores WHERE utilizador_perfil = 2"
        cursor.execute(query)

        #Passa para a variável profs o resultado do fetchall da query
        profs = cursor.fetchall()

        #Cria uma lista de compreensão com a informação de profs
        dados_professor = [row[0] for row in profs]

        #É criada a combobox professor_combo
        professor_combo = Combobox(frame_sec_a)

        #São passados para a combobox os valores de dados_professor
        professor_combo['values'] = dados_professor
        professor_combo.grid(row=5, column=0, columnspan=9, sticky="we")

        #Label relativa aos widgets de início da aula
        label_inicio = Label(frame_sec_a, text="Start Time")
        label_inicio.grid(row=6, column=0, columnspan=3, sticky="we")

        #É criado um DateEntry configurado com o date_pattern de dd-mm-yyyy
        data_inicio_picker = DateEntry(frame_sec_a, width=12, background='darkblue', foreground='white', borderwidth=2, justify='center', date_pattern='dd-mm-yyyy')
        data_inicio_picker.grid(row=7, column=0, sticky="w")

        #São definidos os spinboxes para a escolha das horas e dos minutos, e feita a chamada da função ativar_fim_aula, é feita a formatação para os números abaixo de 10
        #Serem sempre apresentados com um 0 à esquerda
        hora_inicio_spinbox = Spinbox(frame_sec_a, from_=00, to=23, width=2, format="%02.0f", command=ativar_fim_aula)
        hora_inicio_spinbox.grid(row=7, column=1, sticky="w")

        minutos_inicio_spinbox = Spinbox(frame_sec_a, from_=00, to=59, width=2, format="%02.0f", command=ativar_fim_aula)
        minutos_inicio_spinbox.grid(row=7, column=2, sticky="w")

        frame_sec_a.columnconfigure(3, minsize=20)

        #Label relativa aos widgets de fim da aula
        end_label = Label(frame_sec_a, text="End Time")
        end_label.grid(row=6, column=5, columnspan=3, sticky="we")

        # É criado um DateEntry configurado com o date_pattern de dd-mm-yyyy e inicialmente desativado
        data_fim_picker = DateEntry(frame_sec_a, width=12, background='darkblue', foreground='white', borderwidth=2, justify='center', date_pattern='dd-mm-yyyy', state='disabled')
        data_fim_picker.grid(row=7, column=5, sticky="w")

        # São definidos os spinboxes para a escolha das horas e dos minutos, inicialmente desativados, é feita a formatação para os números abaixo de 10
        #         #Serem sempre apresentados com um 0 à esquerda
        hora_fim_spinbox = Spinbox(frame_sec_a, from_=00, to=23, width=2, format="%02.0f", state='disabled')
        hora_fim_spinbox.grid(row=7, column=6, sticky="w")

        minutos_fim_spinbox = Spinbox(frame_sec_a, from_=00, to=59, width=2, format="%02.0f", state='disabled')
        minutos_fim_spinbox.grid(row=7, column=7, sticky="w")

        #Label do Sumário
        sumario_label = Label(frame_sec_a, text="Sumário")
        sumario_label.grid(row=10, column=0, columnspan=9, pady=2)

        #Text Widget para a inserção do Sumário
        sumario_text = Text(frame_sec_a, height=5, width=30)
        sumario_text.grid(row=11, column=0, columnspan=9, sticky="we", pady=5)

        #Botão que chama a janela das faltas
        faltas_button = Button(frame_sec_a, text="Marcação de Faltas", command=lambda:janela_faltas(tabela))
        faltas_button.grid(row=12, column=0, columnspan=9, pady=5)

        #Ao seleccionar o widget DateEntrySelected é chamada a função ativar_fim_aula
        data_inicio_picker.bind("<<DateEntrySelected>>", lambda event: ativar_fim_aula())

        #É criada a função inserir_valores que irá realizar a inserção dos valores na tabela
        def inserir_valores():
            global aluno_ids_string

            #Caso exista alguma linha seleccionada na Treeview, são passados os valores para selected_item
            selected_item = tabela.focus()

            #Caso exista algo seleccionado, é carregado o valor de "text" a partir da tabela
            if selected_item:
                curso_id = tabela.item(selected_item)["text"]

            #Caso não tenha sido nenhuma opção seleccionada é mostrada uma mensagem de erro e dado o return
            else:
                messagebox.showwarning("Aviso", "Nenhum curso selecionado.")
                return

            #São passadas para as variáveis os valores dos widgets correspondentes
            resumo = title_entry.get()
            professor = professor_combo.get()
            start_hour = hora_inicio_spinbox.get()
            start_minute = minutos_inicio_spinbox.get()
            end_hour = hora_fim_spinbox.get()
            end_minute = minutos_fim_spinbox.get()
            summary = sumario_text.get("1.0", "end-1c")

            #É feita a conversão da informação da tabela para os diferentes widgets
            data_inicio_parts = data_inicio_picker.get().split('-')
            data_inicio_formatted = '-'.join(data_inicio_parts[::-1])
            horario_inicio = datetime.strptime(f"{data_inicio_formatted} {start_hour}:{start_minute}", "%Y-%m-%d %H:%M")

            data_fim_parts = data_fim_picker.get().split('-')
            data_fim_formatted = '-'.join(data_fim_parts[::-1])
            horario_fim = datetime.strptime(f"{data_fim_formatted} {end_hour}:{end_minute}", "%Y-%m-%d %H:%M")

            #É feita a conversão dos dados por forma a facilitar sua inserção na BD
            mysql_horario_inicio = horario_inicio.strftime('%Y-%m-%d %H:%M:%S')
            mysql_horario_fim = horario_fim.strftime('%Y-%m-%d %H:%M:%S')

            #Se o horário de fim for menor ou igual ao de início é apresentada uma mensagem de erro
            if horario_fim <= horario_inicio:
                messagebox.showerror("Error", "End time must be later than start time")
                return


            #Criação de um try para tentar registar os dados na BD
            try:
                mycursor = mydb.cursor()

                #Define a query insert_query
                insert_query = "INSERT INTO q_aulas (aulas_curso_id, aula_desc, aula_prof_id, aula_inicio, aula_termino, aula_sumarios, aula_ausencias) " \
                               "VALUES (%s, %s, %s, %s, %s, %s, %s)"

                #Passa a values os diferente valores que serão utilizados para a query
                values = (curso_id, resumo , professor, mysql_horario_inicio, mysql_horario_fim, summary, aluno_ids_string)

                #É executada a query
                mycursor.execute(insert_query, values)

                #É realizado o commit das alterações
                mydb.commit()

                #É mostrada uma mensagem de confirmação caso a craição tenha sido feita com sucesso
                messagebox.showinfo("Sucesso", "A aula foi criada com sucesso.")
            except Exception as erro:
                messagebox.showerror("Erro", str(erro))

        #É criado o botão que irá chamar a variável inserir_valores
        print_button = Button(frame_sec_a, text="Criar Aula", command=inserir_valores)
        print_button.grid(row=15, column=0, columnspan=9, pady=10)


    #É criada a tabela janela_faltas onde irá ser apresentada a Listbox para a marcação das faltas dos alunos
def janela_faltas(tabela):
    #São definidas as características da janela
    faltas = Tk()
    faltas.title("Marcação de Faltas")
    faltas.geometry('400x250')
    faltas.resizable(0, 0)

    label = Label(faltas, text="Marcação de Faltas", font=('Arial', 12, "bold"))
    label.pack(pady=5)

    #É criada a frame que irá conter a listbox e a scrollbar
    framelistbox = Frame(faltas)
    framelistbox.pack()

    #É criada a listbox
    listaalunos = Listbox(framelistbox, selectmode=MULTIPLE, width=50, justify="center")
    listaalunos.pack()

    #É criada a scrollbar e associada à listbox
    scrollbar = Scrollbar(framelistbox, orient="vertical", command=listaalunos.yview)
    listaalunos.configure(yscrollcommand=scrollbar.set)

    listaalunos.pack(side="left", fill="y")
    scrollbar.pack(side="right", fill="y")

    #É carregado o conteúdo da linha seleccionada da tabela para seleccionado
    seleccionado = tabela.focus()
    if seleccionado:

        #Curso_id irá receber o valor "text" da tabela
        curso_id = tabela.item(seleccionado)["text"]

        # É criado um objeto cursor que irá ser utilizado para aceder à BD
        mycursor = mydb.cursor()

        #É passada a query para a variável query
        query = "SELECT q_utilizadores.utilizador_id, q_utilizadores.utilizador_nome FROM q_alunos_cursos JOIN q_utilizadores ON q_alunos_cursos.aluno_id = q_utilizadores.utilizador_id WHERE q_alunos_cursos.curso_id = %s"

        #Executa a query
        mycursor.execute(query, (curso_id,))

        #Passa para a variável alunos os resultados recolhidos pela query
        alunos = mycursor.fetchall()

        #Insere os dados dos alunos na Listbox
        for aluno in alunos:
            aluno_id = aluno[0]
            nome = aluno[1]
            listaalunos.insert(END, f"Aluno: {aluno_id} - Nome: {nome}")

    #Cria o botão que chama a função marcar faltas
    registar_faltas_button = Button(faltas, text="Registar Faltas", command=lambda:marcar_faltas())
    registar_faltas_button.pack(pady=10)

    #Cria a função marcar_faltas
    def marcar_faltas():
        global aluno_ids_string

        #Passa para selected_indices os índices dos items seleccionados na listbox
        selected_indices = listaalunos.curselection()

        #Cria uma lista dos ids dos alunos pertencentes a selected_indices
        selected_aluno_ids = [alunos[index][0] for index in selected_indices]

        #Cria uma string com os ids dos alunos pertencentes a selected_aluno_ids e separa-os com virgulas
        aluno_ids_string = ", ".join(str(aluno_id) for aluno_id in selected_aluno_ids)

        #Mostra uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "As ausências foram registadas com sucesso.")

        #Fecha a janela faltas
        faltas.destroy()

    faltas.mainloop()