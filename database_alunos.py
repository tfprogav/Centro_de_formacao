import mysql.connector

mydb = mysql.connector.connect( #ligação á database
    host="localhost",
    user="root",
    password="",
    database="tf_prog_av"
)


def alunos(): #lista de utilizadores com perfil 1 = aluno
    alunos = []
    mycursor = mydb.cursor()

    mycursor.execute("SELECT utilizador_nome FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_utilizadores = mycursor.fetchall()

    for row in q_utilizadores:
        aluno = row[0]
        alunos.append(aluno)
    return alunos

def alunos_id(): #dicionário com alunos e o seu id
    alunos_info = {}
    mycursor = mydb.cursor()

    mycursor.execute("SELECT  utilizador_id, utilizador_nome FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_utilizadores = mycursor.fetchall()

    for row in q_utilizadores:
        utilizador_id = row[0] #Key
        utilizador_nome = row[1] #Value
        alunos_info[utilizador_id] = utilizador_nome
    return alunos_info

def cursos():#lista de cursos com as suas horas e preço
    cursos = []
    mycursor = mydb.cursor()

    mycursor.execute("SELECT curso_desc, curso_horas, curso_preco, CONCAT(curso_desc, ' --- ', curso_horas, ' horas', ' --- ', curso_preco, ' €') FROM q_cursos")

    q_cursos = mycursor.fetchall()
    for row in q_cursos:
        curso = row[3] # O terceiro elemento é o concat
        cursos.append(curso)
    return cursos


def password_original(nome_aux): #Busca da senha do aluno
    global password_origi
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")

    password_in_lista = mycursor.fetchall()
    for row in password_in_lista:
        password_origi = row[0]
    return password_origi


def password_original_por_id(aluno_id): #Busca da senha do aluno por id
    global password_origi
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_id = '{aluno_id}'")

    password_in_lista = mycursor.fetchall()
    for row in password_in_lista:
        password_origi = row[0]
    return password_origi


def aluno_nome(nome_selecionado): #Vai buscar o nome do aluno selecionado
    global aluno_nome_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_nome_aux = rows[1]
    return aluno_nome_aux


def aluno_phone(nome_selecionado): #Vai buscar o telemóvel do aluno selecionado
    global aluno_phone_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_phone_aux = rows[3]
    return aluno_phone_aux


def aluno_email(nome_selecionado): #Vai buscar o email do aluno selecionado
    global aluno_email_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_email_aux = rows[2]

    return aluno_email_aux


def aluno_address(nome_selecionado): #Vai buscar a morada do aluno selecionado
    global aluno_address_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_address_aux = rows[4]

    return aluno_address_aux


def cursos_por_id(id): #Vai buscar os cursos em que o aluno está inscrito por id
    alunos_cursos_lista = []

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT q_utilizadores.utilizador_id, q_cursos.curso_desc FROM q_utilizadores JOIN q_alunos_cursos ON q_utilizadores.utilizador_id = q_alunos_cursos.aluno_id JOIN q_cursos ON q_alunos_cursos.curso_id = q_cursos.curso_id WHERE q_utilizadores.utilizador_id = {id};")
    cursos_alunos = mycursor.fetchall()

    for row in cursos_alunos:
        curso_desc = row[1]
        alunos_cursos_lista.append(curso_desc)

    return alunos_cursos_lista


def delete_aluno(nome_aux): #Eliminar o aluno
    mycursor = mydb.cursor()

    mycursor.execute(f"DELETE FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")
    mydb.commit()


def update_nome(nome, nome_aux): #Atualizar o nome do aluno
    mycursor = mydb.cursor()

    mycursor.execute(f"UPDATE q_utilizadores SET utilizador_nome = '{nome}' WHERE utilizador_nome = '{nome_aux}'")

    mydb.commit()


def update_email(email, email_aux): #Atualizar o email do aluno
    mycursor = mydb.cursor()

    mycursor.execute(f"UPDATE q_utilizadores SET utilizador_email = '{email}' WHERE utilizador_email = '{email_aux}'")

    mydb.commit()


def update_phone(telemovel, phone_aux): #Atualizar o telemóvel do aluno
    mycursor = mydb.cursor()

    mycursor.execute(f"UPDATE q_utilizadores SET utilizador_contacto = '{telemovel}' WHERE utilizador_contacto = '{phone_aux}'")

    mydb.commit()


def update_address(morada, address_aux): #Atualizar a morada do aluno
    mycursor = mydb.cursor()

    mycursor.execute(f"UPDATE q_utilizadores SET utilizador_morada = '{morada}' WHERE utilizador_morada = '{address_aux}'")

    mydb.commit()


def course_id(cursoDesc): #Vai buscar o id do curso por nome
    global cursoID
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT curso_id FROM q_cursos WHERE curso_desc = '{cursoDesc}'")

    q_curso_id = mycursor.fetchall()
    for row in q_curso_id:
        cursoID = row[0]

    return cursoID


def aluno_id(personName): #Vai buscar o id do aluno
    global alunoID
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT utilizador_id FROM q_utilizadores WHERE utilizador_nome = '{personName}'")

    q_aluno_id = mycursor.fetchall()
    for row in q_aluno_id:
        alunoID = row[0]

    return alunoID


def verify_if_in_course(aluno_id, curso_id): #Verifica se o aluno está inscrito no curso
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT aluno_id, curso_id FROM q_alunos_cursos WHERE aluno_id = {aluno_id} AND curso_id = {curso_id}")
    found = mycursor.fetchall()

    return found


def insert_in_course(aluno_id, curso_id): #Insere aluno no respetivo curso
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO q_alunos_cursos (aluno_id, curso_id) VALUES ({aluno_id}, {curso_id})")
    mydb.commit()


def remove_from_course(aluno_id, curso_id): #Remove o aluno do respetivo curso
    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM q_alunos_cursos WHERE aluno_id = ({aluno_id} AND curso_id = {curso_id})")
    mydb.commit()