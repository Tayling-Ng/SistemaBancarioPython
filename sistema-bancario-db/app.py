from flask import Flask, render_template, request, redirect, url_for
from transacoes import depositar, sacar, extrato
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=["POST"])
def cadastrar_usuario(nome, cpf, data_nascimento, endereco):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (nome, cpf, data_nascimento, endereco) VALUES (?, ?, ?, ?)",
                   (nome, cpf, data_nascimento, endereco))
    
 
    usuario_id = cursor.lastrowid  # Pega o ID do usuário recém-cadastrado
    cursor.execute("INSERT INTO contas (usuario_id, saldo, numero) VALUES (?, ?, ?)",
                   (usuario_id, 0.0, usuario_id))  # Use o próprio ID como número da conta

    conexao.commit()

    cursor.execute("SELECT numero FROM contas WHERE usuario_id=?", (usuario_id,))
    numero_conta = cursor.fetchone()[0]

    conexao.close()
    return render_template('cadastro.html')


if __name__ == "__main__":
    app.run()

