import MySQLdb
import ARQconexao as con

cursor = con.connection.cursor()
def update(sets, table, where=None):
    global cursor, connection

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    print("update with id sucessed!")
    if (where):
        query = query + " WHERE " + where
        print("update with id sucessed!")
    cursor.execute(query)
    con.connection.commit()
