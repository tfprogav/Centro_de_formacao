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

    for rows in q_alunos:
        aluno = rows[0]
        alunos.append(aluno)
    return alunos




