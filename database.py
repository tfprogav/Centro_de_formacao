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

    mycursor.execute("SELECT aluno_nome FROM q_alunos")

    q_alunos = mycursor.fetchall()

    for row in q_alunos:
        aluno = row[0]
        alunos.append(aluno)
    return alunos

def alunos_id():
    alunos_info = {}
    mycursor = mydb.cursor()

    mycursor.execute("SELECT  aluno_id, aluno_nome FROM q_alunos")

    q_alunos = mycursor.fetchall()

    for row in q_alunos:
        aluno_id = row[0]
        aluno_nome = row[1]
        alunos_info[aluno_id] = aluno_nome
    return alunos_info







