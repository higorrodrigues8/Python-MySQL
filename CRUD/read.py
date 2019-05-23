import MySQLdb
import ARQconexao as con
cursor = con.connection.cursor()


def select(fields, tables, where=None):#funcao para consultar
    global cursor

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where
    cursor.execute(query)
    return cursor.fetchall()
