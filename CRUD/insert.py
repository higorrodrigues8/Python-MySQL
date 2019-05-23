import ARQconexao as con
cursor = con.connection.cursor()
def insert(values, table, fields=None):
    global cursor, connection

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = "INSERT INTO " + table + " VALUES " + ",".join(["(" + v + ")" for v in values])
    print(query)
    cursor.execute(query)
    con.connection.commit()
