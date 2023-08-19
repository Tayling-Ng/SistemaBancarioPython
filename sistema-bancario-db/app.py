from flask import Flask, render_template, request, redirect, url_for
from cadastro_usuario import cadastrar_usuario
from transacoes import depositar, sacar, extrato

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

@app.route('/faleconosco.html')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
