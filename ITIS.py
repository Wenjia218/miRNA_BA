import sqlite3

con = sqlite3.connect(<pfad zum datenbankpfad)

cur = con.cursor()

cur.execute("SHOW TABLES;")