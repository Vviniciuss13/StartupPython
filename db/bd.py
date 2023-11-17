#pip install mysql-connector-python
from mysql.connector import (connection)
from classes import Candidato

#DATABASE CONEXÃO
db_conexao = connection.MySQLConnection(host='localhost',
                                        user='root',
                                        password='',
                                        database='startup_av')    


#INSERIR CANDIDATO
def inserirCandidato(Candidato):
    cursor = db_conexao.cursor()
    try:
        cursor.execute("INSERT INTO candidato VALUES(NULL, '"+ Candidato.nome + "' , '"+ Candidato.telefone + "', '"+ Candidato.minibio + 
                   "', " + Candidato.getEntrevista() + ", " + Candidato.getTeorico() + ", " + Candidato.getPratico() + ", " 
                   + Candidato.getSkill() + ");")
        return True
    except:
        return False
    db_conexao.commit()

#PESQUISAR CANDIDATO PELAS NOTAS
def pesquisarCandidato(entrevista, teorico, pratico, softSkill):
    cursor = db_conexao.cursor()

    cursor.execute("SELECT * FROM candidato WHERE entrevista >= " + entrevista + " AND teorico >= " + teorico + " AND pratico >= " + pratico + " AND softSkill >= " + softSkill)

    return cursor.fetchall()

#EXIBIR TODOS OS CANDIDATOS
def exibirTodos():
    cursor = db_conexao.cursor()

    cursor.execute("SELECT * FROM candidato")

    return cursor.fetchall()