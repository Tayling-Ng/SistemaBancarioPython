import sqlite3


def cadastrar_usuario(nome, cpf, data_nascimento, endereco):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (nome, cpf, data_nascimento, endereco) VALUES (?, ?, ?, ?)",
                   (nome, cpf, data_nascimento, endereco))
    
    # Após cadastrar o usuário, criar uma conta associada a ele
    usuario_id = cursor.lastrowid  # Pega o ID do usuário recém-cadastrado
    cursor.execute("INSERT INTO contas (usuario_id, saldo, numero) VALUES (?, ?, ?)",
                   (usuario_id, 0.0, usuario_id))  # Use o próprio ID como número da conta

    conexao.commit()

    # Recupera o número da conta recém-criada
    cursor.execute("SELECT numero FROM contas WHERE usuario_id=?", (usuario_id,))
    numero_conta = cursor.fetchone()[0]

    conexao.close()

    print("Usuário cadastrado com sucesso!")
    print(f"Informações do usuário:")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Endereço: {endereco}")
    print(f"Número da Conta: {numero_conta}")
    print("                                                                        ")





    