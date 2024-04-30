menu = """
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Encerrar
"""

saldo = 3000.00
saques_diarios = 0  # máximo de 3
extrato = ""
LIMITE_MAXIMO = 500.00

print(menu)

while True:
    
    opcao = int(input('Selecione a opção do menu que deseja: '))
    

    if opcao == 1:  # Depósito
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        saldo += valor_deposito
    elif opcao == 2:  # Saque
        valor_do_saque = float(input('Digite o valor que deseja sacar: '))
        if valor_do_saque > 0:
            if saques_diarios < 3:
                if valor_do_saque <= saldo and valor_do_saque <= LIMITE_MAXIMO:
                    saques_diarios += 1
                    saldo -= valor_do_saque
                    extrato += f'Saque do valor de R${valor_do_saque:.2f} realizado com sucesso!\n'
                elif valor_do_saque >= saldo:
                    print('Não será possível sacar o dinheiro por falta de saldo')
                else:
                    print('Valor incompatível')
            else:
                print('Limite diário de saques atingido')
    elif opcao == 3:  # Exibir extrato
        print(extrato)
    elif opcao == 0:  # Sair
        break
    else:
        print('Opção Inválida')

    print(menu)
