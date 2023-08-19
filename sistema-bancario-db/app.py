from flask import Flask, render_template, request, redirect, url_for
from transacoes import depositar, sacar, extrato
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']
    
    cadastrar_usuario(nome, cpf, data_nascimento, endereco)
    
    return redirect(url_for('index'))

@app.route('/transacoes', methods=['POST'])
def transacoes():
    numero_conta = int(request.form['numero_conta'])
    opcao_transacao = request.form['opcao_transacao']
    valor_str = request.form['valor']
    
    if not valor_str:
        return "Valor não pode ser vazio. <a href='/'>Voltar</a>"
    
    try:
        valor = float(valor_str)
    except ValueError:
        return "Valor inválido. <a href='/'>Voltar</a>"
    
    if opcao_transacao == '1':
        depositar(numero_conta, valor)
    elif opcao_transacao == '2':
        sacar(numero_conta, valor)
    elif opcao_transacao == '3':
        extrato(numero_conta)
    
    return redirect(url_for('index'))

