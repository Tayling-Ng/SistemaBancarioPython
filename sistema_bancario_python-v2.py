# Usuários
usuarios = []

def cadastrar_usuario(nome, cpf, data_nascimento, endereco):
    if buscar_usuario(cpf):
        print("Usuário já cadastrado")
        return

    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def buscar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Contas
contas = []
contador_contas = 1

def criar_conta(usuario):
    global contador_contas
    conta = {
        "numero": contador_contas,
        "saldo": 0,
        "usuario": usuario
    }
    contas.append(conta)
    contador_contas += 1

def obter_conta(numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None

def depositar(numero, valor):
    conta = obter_conta(numero)
    if conta:
        conta["saldo"] += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada")

def sacar(numero, valor):
    conta = obter_conta(numero)
    if conta:
        if conta["saldo"] >= valor:
            conta["saldo"] -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")
    else:
        print("Conta não encontrada")

def extrato(numero):
    conta = obter_conta(numero)
    if conta:
        print(f"Numero: {conta['numero']}")
        print(f"Saldo: {conta['saldo']}")
    else:
        print("Conta não encontrada")

# Interface
print("=== ByteBank ===\n")

while True:
    print("[1] Cadastrar usuário")
    print("[2] Fazer login")
    print("[0] Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")

        # Cadastrar o usuário
        cadastrar_usuario(nome, cpf, data_nascimento, endereco)

    elif opcao == "2":
        cpf = input("\nDigite o CPF para fazer login: ")
        usuario = buscar_usuario(cpf)
        if usuario:
            print(f"\nSeja bem-vindo(a) {usuario['nome']}!")

            # Verifica se o usuário já tem uma conta
            if not any(conta["usuario"]["cpf"] == usuario["cpf"] for conta in contas):
                criar_conta(usuario)
                print("Conta criada automaticamente.")

            numero_conta = next(conta["numero"] for conta in contas if conta["usuario"]["cpf"] == usuario["cpf"])
            print(f"Número da sua conta: {numero_conta}")

            while True:
                print("\n[1] Menu Usuário")
                print("[2] Depositar")
                print("[3] Sacar")
                print("[4] Extrato")
                print("[0] Sair do menu usuário")
                opcao_menu_usuario = input("\nDigite a opção desejada: ")

                if opcao_menu_usuario == "1":
                    break  # Retorna ao início do loop "while True"

                elif opcao_menu_usuario == "2":
                    numero = int(input("Número da conta: "))
                    valor = float(input("Valor do depósito: "))
                    depositar(numero, valor)

                elif opcao_menu_usuario == "3":
                    numero = int(input("Número da conta: "))
                    valor = float(input("Valor do saque: "))
                    sacar(numero, valor)

                elif opcao_menu_usuario == "4":
                    numero = int(input("Número da conta: "))
                    extrato(numero)

                elif opcao_menu_usuario == "0":
                    print("\nSaindo do menu usuário.")
                    break  # Sai do loop "while True"
                

                else:
                    print("Opção inválida.")

            print("Retornando ao menu principal.")
        else:
            print("Usuário não encontrado")

    elif opcao == "0":
        print("Até logo!")
        break
