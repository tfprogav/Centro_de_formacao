import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tf_prog_av"
)



def alunos():
    alunos = []
    mycursor = mydb.cursor()

    mycursor.execute("SELECT utilizador_nome FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_utilizadores = mycursor.fetchall()

    for row in q_utilizadores:
        aluno = row[0]
        alunos.append(aluno)
    return alunos

def alunos_id():
    alunos_info = {}
    mycursor = mydb.cursor()

    mycursor.execute("SELECT  utilizador_id, utilizador_nome FROM q_utilizadores WHERE utilizador_perfil = 1")

    q_utilizadores = mycursor.fetchall()

    for row in q_utilizadores:
        utilizador_id = row[0]
        utilizador_nome = row[1]
        alunos_info[utilizador_id] = utilizador_nome
    return alunos_info







