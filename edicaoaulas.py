from tkinter import Label, ttk, Frame, Entry, Button, Text, Spinbox, messagebox, Scrollbar, Tk, Listbox, MULTIPLE, END
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

#É aberta a ligação à base de dados
import mysql.connector
mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="",
database="tf_prog_av"
)

#É criada a janela janela_consultar_aulas onde irão ser executadas as funções relativas
#À edição e remoção de aulas
def janela_consultar_aulas(curso_id):
    #Cria a janela e atribui os parâmetros relativamente ao funcionamento da janela
    consult_aulas = Tk()
    consult_aulas.title("Marcação de Faltas")
    consult_aulas.geometry('1280x720')
    consult_aulas.resizable(0, 0)

    #É criado o label da janela
    label = Label(consult_aulas, text="Consulta e Edição de Aulas", font=('Arial', 14, "bold"))
    label.pack()

    #É criado um objeto cursor que irá ser utilizado para aceder à BD
    #É criada a query que irá preencher a treeview relativamente às aulas correspondentes ao curso seleccionado
    mycursor = mydb.cursor()
    mycursor.execute("""
    SELECT aula_id, aula_desc, CONCAT(aula_prof_id, ' - ', utilizador_nome) AS professor, aula_inicio, aula_termino, aula_sumarios, aula_ausencias
    FROM q_aulas
    JOIN q_utilizadores ON q_aulas.aula_prof_id = q_utilizadores.utilizador_id
    WHERE aulas_curso_id = %s;
""", (curso_id,))
    resultado = mycursor.fetchall()

    #E criada a frame que irá conter a treeview e a scrollbar
    frametreeview = Frame(consult_aulas)
    frametreeview.pack()

    #É definida a estrutura do Treeview
    tabela = ttk.Treeview(frametreeview, columns=("Descricao", "Professor", "Inicio", "Termino", "Sumarios", "Ausencias"), height=6)
    tabela.heading("#0", text="ID")
    tabela.heading("Descricao", text="Descrição da Aula")
    tabela.heading("Professor", text="Professor")
    tabela.heading("Inicio", text="Início")
    tabela.heading("Termino", text="Término")
    tabela.heading("Sumarios", text="Sumários")
    tabela.heading("Ausencias", text="Ausências")
    tabela.pack(pady=10)

    #É criada uma scrollbal e efetuada a sua configuração
    scrollbar = Scrollbar(frametreeview, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)

    #É chamado o geometry manager pack e efetuada a definição da localização dos widgets
    tabela.pack(side="left", fill="y")
    scrollbar.pack(side="right", fill="y")

    #É efetuado o preenchimento e a a configuração do conteúdo que irá popular a tabela
    for item in resultado:
        tabela.insert("", "end", text=item[0], values=(item[1], item[2], item[3], item[4], item[5], item[6]))
    tabela.column("#0", width=50, anchor="center")

    for column in tabela["columns"]:
        tabela.column(column, anchor="center")

    #É criada uma frame intermédia (necessária visto a frame seguinte utilizar um geometry manager diferente)
    frame_intermedia = Frame(consult_aulas)
    frame_intermedia.pack()

    #É criada a frame_sec_a, utilizado o geometry manager grid
    frame_sec_a = Frame(frame_intermedia)
    frame_sec_a.grid(row=1, column=0, padx=10, pady=10)

    #É criada a função editar_aula, que irá ser executada na frame frame_sec_a, e que irá receber o conteúdo de tabela (Treeview)
    def editar_aula(frame_sec_a, tabela):
        #Cria o Widget Label relativo à descrição geral da aula
        descricao_label = Label(frame_sec_a, text="Resumo Aula")
        descricao_label.grid(row=2, column=0, columnspan=9, sticky="we", pady=2)

        #Cria o Widget Entry relativo à descrição da aula
        descricao_entry = Entry(frame_sec_a)
        descricao_entry.grid(row=3, column=0, columnspan=9, sticky="we")

        #Cria o Widget Label para a selecção do docente
        professor_label = Label(frame_sec_a, text="Selecionar Docente")
        professor_label.grid(row=4, column=0, columnspan=9, sticky="we", pady=2)

        #Cria o objeto de classe cursor para interagir com a BD
        cursor = mydb.cursor()

        #Executa a query SQL que irá ser utilizada para popular a ComboBox dos docentes
        #Irá receber como valores utilizador_id e utilizador_nome e concatenar os 2 (referente aos utilizadores que tenham perfil = 2)
        query = "SELECT CONCAT(utilizador_id, ' - ', utilizador_nome) AS professor_info FROM q_utilizadores WHERE utilizador_perfil = 2"
        cursor.execute(query)

        #Executa o comando fetchall para carregar todas as entradas correspondentes à Query
        rows = cursor.fetchall()

        #Realiza uma List Comprehension para popular a variável dados_professor
        dados_professor = [row[0] for row in rows]

        #Carrega os valores de dados_professor para a combobox professor_combo
        professor_combo = Combobox(frame_sec_a)
        professor_combo['values'] = dados_professor
        professor_combo.grid(row=5, column=0, columnspan=9, sticky="we")

        #Cria a Label indicada
        label_inicio = Label(frame_sec_a, text="Início da Aula")
        label_inicio.grid(row=6, column=0, columnspan=3, sticky="we")

        #É criada a DateEntry indicada e alterada o modo de visualização para dd-mm-yyyy
        data_inicio_picker = DateEntry(frame_sec_a, width=12, background='darkblue', foreground='white', borderwidth=2,
                                       justify='center', date_pattern='dd-mm-yyyy')
        data_inicio_picker.grid(row=7, column=0, sticky="w")

        #São criadas duas Spinbox, correspondentes às horas e minutos, e realizado o format para que os valores apresentados tenham
        #Sempre 2 algarismos (valores abaixo de 10 recebem o 0 à esquerda
        hora_inicio_spinbox = Spinbox(frame_sec_a, from_=00, to=23, width=2, format="%02.0f")
        hora_inicio_spinbox.grid(row=7, column=1, sticky="w")

        minutos_inicio_spinbox = Spinbox(frame_sec_a, from_=00, to=59, width=2, format="%02.0f")
        minutos_inicio_spinbox.grid(row=7, column=2, sticky="w")

        frame_sec_a.columnconfigure(3, minsize=20)

        # Cria a Label indicada
        end_label = Label(frame_sec_a, text="Fim da Aula")
        end_label.grid(row=6, column=5, columnspan=3, sticky="we")

        # É criada a DateEntry indicada e alterada o modo de visualização para dd-mm-yyyy
        data_fim_picker = DateEntry(frame_sec_a, width=12, background='darkblue', foreground='white', borderwidth=2,
                                    justify='center', date_pattern='dd-mm-yyyy')
        data_fim_picker.grid(row=7, column=5, sticky="w")

        # São criadas duas Spinbox, correspondentes às horas e minutos, e realizado o format para que os valores apresentados tenham
        # Sempre 2 algarismos (valores abaixo de 10 recebem o 0 à esquerda
        hora_fim_spinbox = Spinbox(frame_sec_a, from_=00, to=23, width=2, format="%02.0f")
        hora_fim_spinbox.grid(row=7, column=6, sticky="w")

        minutos_fim_spinbox = Spinbox(frame_sec_a, from_=00, to=59, width=2, format="%02.0f")
        minutos_fim_spinbox.grid(row=7, column=7, sticky="w")

        #Cria a Label indicada
        sumario_label = Label(frame_sec_a, text="Sumário")
        sumario_label.grid(row=10, column=0, columnspan=9, pady=2)

        #Cria um widget to tipo Text (Caixa de Texto)
        sumario_text = Text(frame_sec_a, height=5, width=30)
        sumario_text.grid(row=11, column=0, columnspan=9, sticky="we", pady=5)

        # Cria a Label indicada
        alunos_label = Label(frame_sec_a, text="Lista de Alunos")
        alunos_label.grid(row=12, column=0, columnspan=9, pady=2)

        #Cria o Widget Listbox, com a funcionalidade de seleção múltipla ativada
        listaalunos = Listbox(frame_sec_a, selectmode=MULTIPLE, width=50, justify="center")
        listaalunos.grid(row=13, column=0, columnspan=8, sticky="nsew")

        #Cria uma Scrollbar associada ao Widget Listbox
        scrollbar = Scrollbar(frame_sec_a, orient="vertical", command=listaalunos.yview)
        scrollbar.grid(row=13, column=9, sticky="ns")

        #Configura a Listbox para utilizar a Scrollbar
        listaalunos.configure(yscrollcommand=scrollbar.set)

        #É criada a função preencher_widgets, que irá realizar o preenchimento dos Widgets com os dados da
        #Tabela, e é ativado pelo event tabela.bind("<<TreeviewSelect>>", preencher_widgets)
        def preencher_widgets(event):
            #É efetuado o acesso à tabela através da opção seleccionada no Treeview
            #E carregados para a lista values os valores correspondentes à linha seleccionada no Treeview
            selected_item = tabela.focus()
            values = tabela.item(selected_item)['values']

            #É efetuada a limpeza do conteúdo do widget descricao_entry
            descricao_entry.delete(0, 'end')
            #E a inserção de values[0] no final do texto existente (deverá estar vazio devido à opção acima)
            descricao_entry.insert('end', values[0])

            #Popula a Combobox professor_combo com o conteúdo de values[1]
            professor_combo.set(values[1])

            #Carrega para as variáveis correspondentes os valores de valuess
            aula_inicio = values[2]
            aula_termino = values[3]

            #Realiza o split para atribuir às variáveis os valores das datas e horas
            data_inicio, hora_inicio = aula_inicio.split(' ')
            data_fim, hora_fim = aula_termino.split(' ')

            #Converte o formato de yyyy-mm-dd para dd-mm-yyyy, carregado o valor de data_inicio, realizando o
            #split através dos '-' e passa para data_inicio_formatted os valores separados por '-'
            data_inicio_formatted = '-'.join(data_inicio.split('-')[::-1])
            data_fim_formatted = '-'.join(data_fim.split('-')[::-1])

            #É passador para o Widget data_inicio_picker o valor de data_inicio_formatted
            data_inicio_picker.set_date(data_inicio_formatted)

            #É realizado o delete ao conteúdo de hora_inicio_spinbox
            hora_inicio_spinbox.delete(0, 'end')

            #É inserido no widget hora_inicio_spinbox os 2 primeiros valores de hora_inicio
            hora_inicio_spinbox.insert('end', hora_inicio[:2])

            # É realizado o delete ao conteúdo de minutos_inicio_spinbox
            minutos_inicio_spinbox.delete(0, 'end')

            #É inserido no widget hora_inicio_spinbox os 3o e 4o valores de hora_inicio
            minutos_inicio_spinbox.insert('end', hora_inicio[3:5])

            # É passador para o Widget data_fim_picker o valor de data_fim_formatted
            data_fim_picker.set_date(data_fim_formatted)

            # É realizado o delete ao conteúdo de hora_fim_spinbox
            hora_fim_spinbox.delete(0, 'end')

            # É inserido no widget hora_fim_spinbox os 2 primeiros valores de hora_fim
            hora_fim_spinbox.insert('end', hora_fim[:2])

            # É realizado o delete ao conteúdo de minutos_fim_spinbox
            minutos_fim_spinbox.delete(0, 'end')

            # É inserido no widget minutos_fim_spinbox os 3o e 4o valores de hora_fim
            minutos_fim_spinbox.insert('end', hora_fim[3:5])

            #É limpo o conteúdo de sumario_text desde o primeiro caractere até ao último
            sumario_text.delete('1.0', 'end')
            sumario_text.insert('1.0', values[4])

            # É criado um objeto cursor que irá ser utilizado para aceder à BD
            mycursor = mydb.cursor()

            #É carregada a query que irá receber os dados dos utilizadores pertencentes a um determinado curso
            query = "SELECT q_utilizadores.utilizador_id, q_utilizadores.utilizador_nome FROM q_alunos_cursos JOIN q_utilizadores ON q_alunos_cursos.aluno_id = q_utilizadores.utilizador_id WHERE q_alunos_cursos.curso_id = %s"

            #É passado para o cursor a query e o valor de curso_id
            mycursor.execute(query, (curso_id,))

            #São passados para a variável alunos a informação recolhida pela Query
            alunos = mycursor.fetchall()

            #É efetuado o delete do conteúdo de delete desde o início até ao final
            listaalunos.delete(0, 'end')

            #É utilizado um ciclo for para passar para a tabela o conteúdo de aluno_id e nome através de
            #Um formatted print
            for aluno in alunos:
                aluno_id = aluno[0]
                nome = aluno[1]
                listaalunos.insert(END, f"Aluno: {aluno_id} - Nome: {nome}")

            #Acede ao valor seleccionado na Treeview
            selected_item = tabela.focus()

            #Passa para values uma comprehension list com os valores da linha da tabela seleccionada
            values = tabela.item(selected_item)['values']

            #Se a quantidade (length) de valores da variavel valores for superior a 5
            #A variavel ausencias ira receber os valores de values na sua posição 5
            if len(values) > 5:
                ausencias = values[5]

                #Verifica se ausencias é uma string e caso seja é realizado o split através das ','
                if isinstance(ausencias, str):
                    ausencias_list = [x.strip() for x in ausencias.split(',')]

                #Se ausencias não for uma string, irá ser convertido para string
                else:
                    ausencias_list = [str(ausencias).strip()]

                #Executa um ciclo for no range da listaalunos
                for i in range(listaalunos.size()):

                    #A variavel aluno irá receber o valor de i de lista de alunos
                    aluno = listaalunos.get(i)

                    #Aluno_id irá receber o resultado do split da variável aluno
                    aluno_id = aluno.split(' - ')[0].split(': ')[1].strip()

                    #Se aluno_id existir na lista de ausencias é selecionada a entrada correspondente
                    #Na listbox listaalunos
                    if aluno_id in ausencias_list:
                        listaalunos.selection_set(i)
                    else:
                        listaalunos.selection_clear(i)
            else:
                #Se não existir ninguém, limpa a selecção da Listbox
                listaalunos.selection_clear(0, 'end')

        #Função que irá guardar as alterações efetuadas
        def guardar_alteracoes():

            #Irá efetuar um try- except que irá tentar submeter as alterações efetuadas para a BD
            try:
                #Caso tenha sido seleccionada alguma entrada na Treeview
                selected_item = tabela.focus()

                #Se não tiver sido seleccionada nenuma entrada na Treeview apresenta uma mensagem de erro
                if not selected_item:
                    messagebox.showwarning("Aviso", "Nenhuma aula selecionada.")
                    return

                #Caso tenha sido seleccionada alguma opção no Treeview, é carregado o valor indicado
                aula_id = tabela.item(selected_item)["text"]

                #Recebe os valores de cada um dos widgets apresentados
                descricao = descricao_entry.get()
                professor_info = professor_combo.get()
                inicio_data = data_inicio_picker.get_date().strftime('%Y-%m-%d')
                inicio_hora = f"{hora_inicio_spinbox.get()}:{minutos_inicio_spinbox.get()}"
                termino_data = data_fim_picker.get_date().strftime('%Y-%m-%d')
                termino_hora = f"{hora_fim_spinbox.get()}:{minutos_fim_spinbox.get()}"
                sumario = sumario_text.get('1.0', 'end').strip()

                #Acede à variável professor_info e executa um split para separar o numero do docente do nome e passa à variável professor_id o resultado
                professor_id = professor_info.split(' - ')[0]

                #Cria o objeto de classe cursor para interagir com a BD
                mycursor = mydb.cursor()

                query = """
                UPDATE q_aulas
                SET aula_desc = %s,
                    aula_prof_id = %s,
                    aula_inicio = %s,
                    aula_termino = %s,
                    aula_sumarios = %s
                WHERE aula_id = %s
                """
                #É criada a tupla values, que irá receber as variáveis que necessitarão de ser passadas para a query
                values = (descricao, professor_id, f"{inicio_data} {inicio_hora}", f"{termino_data} {termino_hora}", sumario, aula_id)

                #Executa a query passando os valores correspondentes
                mycursor.execute(query, values)

                #Passa para a variável selected_alunos as opções atualmente seleccionadas na listbox listaalunos
                selected_alunos = listaalunos.curselection()

                #É criada uma lista vazia chamada ausencias_list
                ausencias_list = []

                #É executado um ciclo for aos valores de selected_alunos
                #Irá passar para aluno o item associado à posição i
                #Recebe o aluno_id ao efetuar o strip ao valor de aluno (contém o aluno_id e o noem do aluno)
                for i in selected_alunos:
                    aluno = listaalunos.get(i)
                    aluno_id = aluno.split(' - ')[0].split(': ')[1].strip()

                    #Realiza o append do valor de aluno_id à lista ausencias_list
                    ausencias_list.append(aluno_id)

                #Cria a variável ausencias ao realizar o join dos valores de ausencias_list, separando-os por vírgulas
                ausencias = ','.join(ausencias_list)

                #Cria a variável query_ausencias que irá receber a query que será utilizada para enviar para a BD a lista de ausencias
                query_ausencias = "UPDATE q_aulas SET aula_ausencias = %s WHERE aula_id = %s"

                #Executa a query
                mycursor.execute(query_ausencias, (ausencias, aula_id))

                #Realiza o commit dos dados
                mydb.commit()

                #Apresenta uma mensagem de sucesso
                messagebox.showinfo("Sucesso", "As alterações foram salvas com sucesso!")

                #Fecha a frame atual
                consult_aulas.destroy()

                #Chama a janela onde se encontra o Treeview, realizando a sua atualização
                janela_consultar_aulas(curso_id)


            #Caso o try criado anteriormente não tinha sido bem sucedido, é executada a excepção
            except Exception as e:

                #Reverte as alterações pendentes de ser efetuadas
                mydb.rollback()

                #Mostra uma janela de erro com o erro apresentado
                messagebox.showerror("Erro", str(e))

        #É criado o evento TreeviewSelect, que leva a que cada vez que seja selecionada uma opção no Treeview, os widgets da função preencher_widgets sejam preenchidos
        tabela.bind("<<TreeviewSelect>>", preencher_widgets)

        #É criado o botão que irá chamar a variável guardar_alteracoes
        guardar_btn = Button(frame_sec_a, text="Guardar Alterações", command=guardar_alteracoes)
        guardar_btn.grid(row=14, column=0, columnspan=9, pady=5)

        #É criada a função que permitirá apagar os dados existentes na base de dados
        def eliminar_aula():

            #Caso tenha sido seleccionada alguma entrada na Treeview
            selected_item = tabela.focus()

            # Se não tiver sido seleccionada nenuma entrada na Treeview apresenta uma mensagem de erro
            if not selected_item:
                messagebox.showwarning("Aviso", "Nenhuma aula selecionada.")
                return

            # Caso tenha sido seleccionada alguma opção no Treeview, é carregado o valor indicado
            aula_id = tabela.item(selected_item)["text"]

            #cria o objeto confirmacao, que é uma messagebox com confirmação de Sim/Não
            confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar esta aula?")
            if not confirmacao:
                return

            #Caso a resposta seja positiva
            try:

                #Cria o objeto de classe cursor para interagir com a BD
                mycursor = mydb.cursor()

                #query recebe uma string com a query que irá ser executada
                query = "DELETE FROM q_aulas WHERE aula_id = %s"

                #Executa a query passando o valor de query, e a aula_id
                mycursor.execute(query, (aula_id,))

                #Executa o commit
                mydb.commit()

                #Apaga a linha seleccionada da tabela
                tabela.delete(selected_item)

                messagebox.showinfo("Sucesso", "A aula foi apagada com sucesso!")

            # Caso o try criado anteriormente não tinha sido bem sucedido, é executada a excepção
            except Exception as e:

                #Reverte as alterações pendentes de ser efetuadas
                mydb.rollback()

                #Mostra uma janela de erro com o erro apresentado
                messagebox.showerror("Erro", str(e))

        #Cria o botão que irá chamar a função eliminar_aula
        delete_btn = Button(frame_sec_a, text="Apagar Aula", command=eliminar_aula)
        delete_btn.grid(row=15, column=0, columnspan=9, pady=5)


    #Chama a função editar_aula
    editar_aula(frame_sec_a, tabela)



    #Cria o loop de consult_aulas
    consult_aulas.mainloop()