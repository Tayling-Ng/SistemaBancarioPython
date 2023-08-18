from cadastro_usuario import cadastrar_usuario
from transacoes import depositar, sacar, extrato
import os

# Executar o script de configuração do banco de dados se as tabelas ainda não foram criadas
if not os.path.exists("clientes.db"):
    print("Configurando o banco de dados...")
    import setup_db  # Importa e executa o script setup_db.py

def menu_principal():
    while True:
        print("[1] Cadastrar usuário")
        print("[2] Realizar transações")
        print("[0] Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereço: ")

            cadastrar_usuario(nome, cpf, data_nascimento, endereco)

        elif opcao == "2":
            numero_conta = int(input("Número da conta: "))
            print("[1] Depositar")
            print("[2] Sacar")
            print("[3] Extrato")
            opcao_transacao = input("\nEscolha uma transação: ")

            if opcao_transacao == "1":
                valor = float(input("Valor do depósito: "))
                depositar(numero_conta, valor)
            elif opcao_transacao == "2":
                valor = float(input("Valor do saque: "))
                sacar(numero_conta, valor)
            elif opcao_transacao == "3":
                extrato(numero_conta)
            else:
                print("Opção de transação inválida")

        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu_principal()
