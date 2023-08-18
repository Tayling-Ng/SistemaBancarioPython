import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        data_nascimento TEXT,
        endereco TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        saldo REAL,
        numero INTEGER,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
""")

conexao.commit()
conexao.close()
