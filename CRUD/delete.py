import ARQconexao as con
cursor = con.connection.cursor()


def delete(table, where):
    global connect, cursor

    query = "DELETE FROM " + table + " WHERE " + where
    cursor.execute(query)
    con.connection.commit()
