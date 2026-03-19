import sqlite3

def conectar():
    return sqlite3.connect("database.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dia INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    whatsapp TEXT,
    instagram TEXT
)
""")
    
    conn.commit()
    conn.close()