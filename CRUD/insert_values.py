
import MySQLdb
import insert as i


values = [
"DEFAULT, 'Jõao pedro', '2000-01-01', 'Av das pedras, 123', 'Betim','MG', '1233456789'"
]
table = 'alunos';
i.insert(values, table)
