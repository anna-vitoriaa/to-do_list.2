import sqlite3
conn = sqlite3.connect("To-do_list.db")
crs = conn.cursor()

crs.execute('''
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        situacao INTEGER DEFAULT 0)''')

conn.commit()

def criar_tarefa_db(nome, data_str):
    crs.execute("INSERT INTO Tarefas (nome, data) VALUES (?, ?)", (nome, data_str))
    conn.commit()