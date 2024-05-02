def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #somente nomeado
    #esta funcao 
    return saldo, extrato

def depositar(saldo, valor, extrato, /): #somente posicional
    #esta funcao
    
    
    
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato): #saldo posicional, extrato nomeado
    #esta funcao
    return extrato

def cadastrar_usuario(nome, data_de_nascimento, cpf, endereco): #dict
    #esta funcao armazena os usuarios em uma lista
    #endereco e uma string com o formato: logradouro - bairro - cidade/sigla do estado
    #nao podemos armazenar 2 usuarios com mesmo CPF
    pass

def cadastrar_conta_bancaria(agencia, numero_da_conta, usuario):
    #esta funcao armazena conta em uma lista
    #o numero da conta e sequencial, iniciando em 1
    #o numero da agencia 'e fixo: "0001"
    #o usuario pode ter mais de uma conta, mas a conta so pertence a um unico usuario
    pass

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")