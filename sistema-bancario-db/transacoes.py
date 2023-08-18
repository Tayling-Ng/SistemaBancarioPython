import sqlite3

def obter_saldo(usuario_id):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT saldo FROM contas WHERE usuario_id=?", (usuario_id,))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        return resultado[0]
    else:
        return 0.0

def depositar(usuario_id, valor):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    saldo_atual = obter_saldo(usuario_id)
    novo_saldo = saldo_atual + valor

    cursor.execute("UPDATE contas SET saldo=? WHERE usuario_id=?", (novo_saldo, usuario_id))
    conexao.commit()
    conexao.close()

    print("Depósito realizado com sucesso!")

def sacar(usuario_id, valor):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    saldo_atual = obter_saldo(usuario_id)

    if saldo_atual >= valor:
        novo_saldo = saldo_atual - valor
        cursor.execute("UPDATE contas SET saldo=? WHERE usuario_id=?", (novo_saldo, usuario_id))
        conexao.commit()
        conexao.close()
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")

        
def extrato(usuario_id):
    saldo_atual = obter_saldo(usuario_id)
    if saldo_atual is not None:
        print(f"Saldo: {saldo_atual}")
    else:
        print("Conta não encontrada")
