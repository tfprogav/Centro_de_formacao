#Importa as biblotecas ou funções necessárias
from tkinter import Label, ttk, Frame, Entry, Button, messagebox, Scrollbar

#É aberta a ligação à base de dados
import mysql.connector
mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="",
database="tf_prog_av")

#É criada a função gestao_cursos que irá ser executada no frame content_frame
def gestao_cursos(content_frame):
    content_frame.configure(bg="#F0F0F0")
    #A cada execução da função são destruídos os widgets existentes na frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    #É criada na content_frame a frame frame_gestao_c
    frame_gestao_c = Frame(content_frame)
    frame_gestao_c.pack()

    #É criada a Label da página
    label = Label(frame_gestao_c, text='Gestão de Cursos', font=('Arial', 14, "bold"))
    label.pack(pady=5)

    # É criado um objeto cursor que irá ser utilizado para aceder à BD
    # É criada a query que irá preencher a treeview com a informação relativa aos cursos
    mycursor = mydb.cursor()
    mycursor.execute("SELECT curso_id, curso_desc, curso_horas, curso_preco FROM q_cursos")

    #Para resultado irão ser carregados todos os dados obtidos por mycursor
    resultado = mycursor.fetchall()

    #É criada uma frame que irá ser executada na frame frame_gestao_c
    frametreeview = Frame(frame_gestao_c)
    frametreeview.pack()

    #É criada uma Treeview na frame frametreeview e atribuída a informação relativa a cabeçalhos e colunas
    tabela = ttk.Treeview(frametreeview, columns=("Descricao", "Horas", "Preco"), height=6)
    tabela.heading("#0", text="ID")
    tabela.heading("Descricao", text="Descrição do Curso")
    tabela.heading("Horas", text="Horas")
    tabela.heading("Preco", text="Preço")
    tabela.pack(pady=10)

    #É criada uma scrollbar que irá ficar associada à Treeview tabela
    scrollbar = Scrollbar(frametreeview, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)

    #São atribuidas as posições à Treeview e à scrollbar
    tabela.pack(side="left", fill="y")
    scrollbar.pack(side="right", fill="y")

    #É executado um ciclo for que irá popular a Treeview através da informação existente em resultado
    for item in resultado:
        tabela.insert("", "end", text=item[0], values=(item[1], item[2], item[3]))

    #É formatada a primeira coluna do Treeview para centrar o seu conteúdo
    tabela.column("#0", anchor="center")

    #É executada a mesma formatação das restantes colunas
    for column in tabela["columns"]:
        tabela.column(column, anchor="center")


    #São criados os botões que irão respetivamente chamar as variáveis para a criação, edição e remoção de cursos (funções essas que serão executadas na frame frame_sec_c)
    button_criar_curso = Button(frame_gestao_c, text="Criar Curso", command=lambda: criar_curso(frame_sec_c), font=('Arial',9, 'bold'))
    button_criar_curso.pack(pady=5)

    button_editar_dados = Button(frame_gestao_c, text="Editar Dados", command=lambda: editar_curso(frame_sec_c), font=('Arial',9, 'bold'))
    button_editar_dados.pack(pady=5)

    button_apagar_curso = Button(frame_gestao_c, text="Apagar Curso", command=lambda: apagar_curso(frame_sec_c), font=('Arial',9, 'bold'))
    button_apagar_curso.pack(pady=5)

    #É criada a frame frame_sec_c
    frame_sec_c = Frame(content_frame, borderwidth=1, relief="solid")
    frame_sec_c.pack(pady=10)

    #É criada a função que irá permitir a criação de cursos
    def criar_curso(frame_sec_c):

        # A cada execução da função são destruídos os widgets existentes na frame
        for widget in frame_sec_c.winfo_children():
            widget.destroy()

        #São criados os widgets existentes na frame (Labels e Entries)
        label = Label(frame_sec_c, text='Criação de Curso', font=('Arial', 12, "bold"))
        label.pack(pady=5)

        desc_label = Label(frame_sec_c, text="Descrição:")
        desc_label.pack(padx=10, pady=5)

        desc_entry = Entry(frame_sec_c, width=50, justify="center")
        desc_entry.pack(padx=10, pady=5)

        horas_label = Label(frame_sec_c, text="Horas:")
        horas_label.pack(padx=10, pady=5)

        horas_entry = Entry(frame_sec_c, width=30, justify="center")
        horas_entry.pack(padx=10, pady=5)

        preco_label = Label(frame_sec_c, text="Preço:")
        preco_label.pack(padx=10, pady=5)

        preco_entry = Entry(frame_sec_c, width=30, justify="center")
        preco_entry.pack(padx=10, pady=5)

        # É criado um objeto cursor que irá ser utilizado para aceder à BD
        mycursor = mydb.cursor()

        #É criada a função guardar_curso que irá permitir a gravação dos dados na BD
        def guardar_curso():

            #São passadas às variáveis os conteúdos dos respetivos widgets
            descricao = desc_entry.get()
            horas = horas_entry.get()
            preco = preco_entry.get()

            #Se o conteúdo de horas não for um valor inteiro, é apresentada uma mensagem de erro
            if not horas.isdigit():
                messagebox.showerror("Erro", "As horas devem ser um número inteiro.")
                return

            # Se o conteúdo de preço não for um valor numérico, é apresentada uma mensagem de erro
            if not preco.replace('.', '', 1).isnumeric():
                messagebox.showerror("Erro", "O preço deve ser um número válido.")
                return

            #A variável valores irá receber os valores de: descricao, horas e preco
            values = (descricao, horas, preco)

            #a variável sql irá receber a string correspondente à Query
            sql = "INSERT INTO q_cursos (curso_desc, curso_horas, curso_preco) VALUES (%s, %s, %s);"

            #Irá ser executao um try- except para tentar a inserção dos dados
            try:

                #Caso seja bem sucedido, são passados os dados e realizado o commit e apresentada uma mensagem de suscesso
                mycursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Sucesso", "O curso foi criado com sucesso.")

                #É chamada novamente a função gestao_cursos, que fará com que a Treeview seja atualizada
                gestao_cursos(content_frame)

            #Caso o try não seja bem sucedido é apresentada uma mensagem de erro
            except Exception as erro:
                # Display an error message box
                messagebox.showerror("Erro", str(erro))

        #É criado o botão que irá chamar a função guardar_curso
        confirmar_button = Button(frame_sec_c, text="Confirmar", command=guardar_curso)
        confirmar_button.pack(padx=10, pady=10)

    #É crida a função editar_curso que permitirá a edição dos dados dos cursos já existentes
    def editar_curso(frame_sec_c):

        # A cada execução da função são destruídos os widgets existentes na frame
        for widget in frame_sec_c.winfo_children():
            widget.destroy()

        #São criados os widgets existentes na frame (Labels e Entries)
        label = Label(frame_sec_c, text='Editar Curso', font=('Arial', 12, "bold"))
        label.pack(pady=5)

        desc_label = Label(frame_sec_c, text="Descrição:")
        desc_label.pack(padx=10, pady=5)

        desc_entry = Entry(frame_sec_c, width=50, justify="center")
        desc_entry.pack(padx=10, pady=5)

        horas_label = Label(frame_sec_c, text="Horas:")
        horas_label.pack(padx=10, pady=5)

        horas_entry = Entry(frame_sec_c, width=30, justify="center")
        horas_entry.pack(padx=10, pady=5)

        preco_label = Label(frame_sec_c, text="Preço:")
        preco_label.pack(padx=10, pady=5)

        preco_entry = Entry(frame_sec_c, width=30, justify="center")
        preco_entry.pack(padx=10, pady=5)

        #Caso esteja algum valor na treeview seleccionado, é realizado o carregamento dos dados correspondentes a essa linha
        seleccionado = tabela.focus()
        if seleccionado:
            item_data = tabela.item(seleccionado)
            values = item_data["values"]
            desc_entry.insert(0, values[0])  # Set the value from the treeview
            horas_entry.insert(0, values[1])  # Set the value from the treeview
            preco_entry.insert(0, values[2])  # Set the value from the treeview

        #caso nenhuma opção tenha sido seleccionada é apresentado um aviso
        else:
            messagebox.showwarning("Seleção Inválida", "Por favor seleccione um valor na tabela.")

        #É criada uma função para permitir guardas as alterações
        def guardar_alteracoes():

            # São passadas às variáveis os conteúdos dos respetivos widgets
            novo_desc = desc_entry.get()
            novo_horas = horas_entry.get()
            novo_preco = preco_entry.get()

            # Se o conteúdo de novo_horas não for um valor inteiro, é apresentada uma mensagem de erro
            if not novo_horas.isdigit():
                messagebox.showerror("Erro", "As horas devem ser um número inteiro.")
                return

            # Se o conteúdo de novo_preco não for um valor numérico, é apresentada uma mensagem de erro
            if not novo_preco.replace('.', '', 1).isnumeric():
                messagebox.showerror("Erro", "O preço deve ser um número válido.")
                return



            # É criado um objeto cursor que irá ser utilizado para aceder à BD
            mycursor = mydb.cursor()

            #O conteúdo da linha seleccionada na tabela é passado a seleccionado
            seleccionado = tabela.item(tabela.focus())

            #É carregado para curso_id o valor da variável text da Treeview
            curso_id = seleccionado['text']

            #É passado a sql o valor da Query
            sql = "UPDATE q_cursos SET curso_desc = %s, curso_horas = %s, curso_preco = %s WHERE curso_id = %s"

            #São passados para values os valores correspondentes à informação a ser alterada na BD
            values = (novo_desc, novo_horas, novo_preco, curso_id)

            #É executado um try que irá tentar enviar a informação para a BD
            try:
                mycursor.execute(sql, values)
                mydb.commit()

                #Caso seja enviada a informação com sucesso é mostrada uma mensagem, e chamada novamente a função gestao_cursos(content_frame) (irá realizar o refresh à Treeview)
                messagebox.showinfo("Sucesso", "Os dados do curso foram editados com sucesso.")
                gestao_cursos(content_frame)

            #Caso o except não seja bem sucesido é apresentada uma mensagem de erro
            except Exception as erro:
                # Display an error message box
                messagebox.showerror("Erro", str(erro))

        #É criado um botão que irá chamar a função guardar_alteracoes
        confirmar_button = Button(frame_sec_c, text="Confirmar", command=guardar_alteracoes)
        confirmar_button.pack(padx=10, pady=10)

    #É definida a função que irá permitir apagar cursos
    def apagar_curso(frame_sec_c):

        #caso exista algum valor seleccionado na tabela, é passado o conteúdo dessa linha para seleccionado
        seleccionado = tabela.focus()

        if seleccionado:

            #curso_id recebe o valor de "text" do item da tabela seleccionado
            curso_id = tabela.item(seleccionado)["text"]

            # É criado um objeto cursor que irá ser utilizado para aceder à BD
            mycursor = mydb.cursor()

            #sql_contagem irá receber a query que irá ser utilizada (quantidade de alunos do curso seleccionado)
            sql_contagem = "SELECT COUNT(*) FROM q_alunos_cursos WHERE curso_id = %s"

            #valores_contagem irá receber o valor de curso_id
            valores_contagem = (curso_id,)

            #Será executada a query
            mycursor.execute(sql_contagem, valores_contagem)

            #Irá ser carregado para contagem o valor do primeiro resultado da query
            contagem = mycursor.fetchone()[0]

            #Se a contagem for igual a 0 (0 utilizadores)
            if contagem == 0:
                #É apresentada uma messagebox de confirmação
                confirmed = messagebox.askyesno("Confirmar Remoção", "De certeza que deseja apagar este curso?")

                #Se o utilziador confirmar
                if confirmed:

                    #É carregado para sql_apagar a query
                    sql_apagar = "DELETE FROM q_cursos WHERE curso_id = %s"

                    #PAra valores_apagar o curso_id
                    valores_apagar = (curso_id,)

                    #Irá ser tentada a execução da Query, e em caso positivo será mostrada uma mensagem e feito o refresh à Treeview
                    try:
                        mycursor.execute(sql_apagar, valores_apagar)
                        mydb.commit()
                        messagebox.showinfo("Sucesso", "O curso foi apagado com sucesso.")
                        gestao_cursos(content_frame)

                    #Caso não seja possível a execução da Query, será apresentada uma mensagem de erro
                    except Exception as erro:
                        # Display an error message box
                        messagebox.showerror("Erro", str(erro))

            #Caso a contagem seja superior a 0, não é possível apagar o curso, e é apresentada uma mensagem de aviso
            else:
                messagebox.showinfo("Aviso", "O curso possui alunos matriculados e não pode ser apagado.")

        #Caso não se encontre nenhuma opção seleccionada no Treeview, é apresentada a mensagem com o aviso
        else:
            messagebox.showinfo("Aviso", "Nenhum curso selecionado.")