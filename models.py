import sqlite3


def conectar():
    return sqlite3.connect("database.db")


def inserir_pessoa(nome, dia, mes, whatsapp, instagram):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pessoas (nome, dia, mes, whatsapp, instagram)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, dia, mes, whatsapp, instagram))

    conn.commit()
    conn.close()


def buscar_por_mes(mes):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, dia FROM pessoas
        WHERE mes = ?
        ORDER BY dia
    """, (mes,))

    dados = cursor.fetchall()

    conn.close()

    return dados