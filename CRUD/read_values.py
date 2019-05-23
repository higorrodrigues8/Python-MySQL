import MySQLdb

import read as r


consulta = r.select("nome, cpf", "alunos") #selecione os parametros)
print(consulta)
