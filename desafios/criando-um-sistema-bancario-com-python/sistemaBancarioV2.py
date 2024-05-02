import textwrap

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #somente nomeado
    #esta funcao verifica os parametros para realizar o saque da conta, depois disso executa o saque
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\t@@@Operação falhou! Você não tem saldo suficiente.@@@")

        elif excedeu_limite:
            print("\t@@@Operação falhou! O valor do saque excede o limite.@@@")

        elif excedeu_saques:
            print("\t@@@Operação falhou! Número máximo de saques excedido.@@@")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\t===Saque realizado com sucesso===")
        else:
            print("\t@@@Operação falhou! O valor informado é inválido.@@@")
            
        return saldo, extrato

def depositar(saldo, valor, extrato, /): #somente posicional
    #esta funcao verifica o valor depositado, e atualiza o saldo da conta
    if valor > 0:
        saldo += valor
        extrato += f"\tDeposito no valor de: R$ {valor:.2f}\n"
        print(f"\t\n===Deposito realizado com sucesso!===")
    else:
        print("@@@Valor invalido! Operação cancelada.@@@")
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato): #saldo posicional, extrato nomeado
    #esta funcao permite que seja o extrato da conta seja exibido na tela do usuario
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return extrato

def verifica_usuario(usuarios, cpf):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None
    
def cadastrar_usuario(usuarios): #dict
    #esta funcao armazena os usuarios em uma lista
    #endereco e uma string com o formato: logradouro, numero - bairro - cidade/sigla do estado
    #nao podemos armazenar 2 usuarios com mesmo CPF
    cpf = input("Digite seu CPF(somente numero): ")
    usuario = verifica_usuario(usuarios, cpf)
    
    if usuario:
        print("@@@Usuario com este CPF ja existe!@@@")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereco com o formato: logradouro, numero - bairro - cidade/sigla do estado: ")
    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n===Usuario criado com sucesso!===")

def cadastrar_conta_bancaria(agencia, numero_da_conta, usuarios):
    #esta funcao armazena conta em uma lista
    #o numero da conta e sequencial, iniciando em 1
    #o numero da agencia 'e fixo: "0001"
    #o usuario pode ter mais de uma conta, mas a conta so pertence a um unico usuario
    cpf = input("Informe o CPF do usuario(somente numeros): ")
    usuario = verifica_usuario(usuarios, cpf)
    if usuario:
        print("\n===Conta criada com sucesso!===")
        return {"agencia": agencia, "numero da conta": numero_da_conta, "usuario": usuario}
    
    print("@@@Usuario nao encontrado@@@")
    return
    

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def menu():
    menu = """\n
    =============Menu=============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tNovo Usuario
    [6]\tListar Usuarios
    [0]\tSair

    => """
    return input(textwrap.dedent(menu))

def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
    
        opcao = menu()
      
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                numero_saques= numero_saques,
                limite_saques= LIMITE_SAQUES,
            )

        elif opcao == "3":
            visualizar_extrato(saldo, extrato= extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "5":
            cadastrar_usuario(usuarios)

        elif opcao == "6":
            listar_usuarios(usuarios)
            
        elif opcao == "0":
            break
    
        else:
           print("Operação inválida, por favor selecione novamente a operação desejada.")
           
main()