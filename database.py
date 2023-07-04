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
        utilizador_id = row[0]
        utilizador_nome = row[1]
        alunos_info[utilizador_id] = utilizador_nome
    return alunos_info




def cursos(): #lista de cursos com as suas horas e preço
    cursos = []
    mycursor = mydb.cursor()

    mycursor.execute("SELECT curso_desc, curso_horas, curso_preco, CONCAT(curso_desc, ' --- ', curso_horas, ' horas', ' --- ', curso_preco, ' €') FROM q_cursos")

    q_cursos = mycursor.fetchall()
    for row in q_cursos:
        curso = row[3]
        cursos.append(curso)
    return cursos


def password_original(nome_aux):
    global password_origi
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT utilizador_senha FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")

    password_in_lista = mycursor.fetchall()
    for row in password_in_lista:
        password_origi = row[0]
    return password_origi


def aluno_nome(nome_selecionado):
    global aluno_nome_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_nome_aux = rows[1]
    return aluno_nome_aux


def aluno_phone(nome_selecionado):
    global aluno_email_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_email_aux = rows[2]
    return aluno_email_aux


def aluno_email(nome_selecionado):
    global aluno_phone_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_phone_aux = rows[3]

    return aluno_phone_aux


def aluno_address(nome_selecionado):
    global aluno_address_aux
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_alunos = mycursor.fetchall()
    for rows in q_alunos:
        if rows[1] == nome_selecionado:
            aluno_address_aux = rows[4]

    return aluno_address_aux


def cursos_por_id(id):
    alunos_cursos_lista = []

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT q_utilizadores.utilizador_id, q_cursos.curso_desc FROM q_utilizadores JOIN q_alunos_cursos ON q_utilizadores.utilizador_id = q_alunos_cursos.aluno_id JOIN q_cursos ON q_alunos_cursos.curso_id = q_cursos.curso_id WHERE q_utilizadores.utilizador_id = {id};")
    cursos_alunos = mycursor.fetchall()

    for row in cursos_alunos:
        curso_desc = row[1]
        alunos_cursos_lista.append(curso_desc)

    return alunos_cursos_lista


def delete_aluno(nome_aux):
    mycursor = mydb.cursor()

    mycursor.execute(f"DELETE FROM q_utilizadores WHERE utilizador_nome = '{nome_aux}'")
    mydb.commit()