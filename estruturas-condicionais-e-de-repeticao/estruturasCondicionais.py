import sys

saldo = 2000.0
saque = float(input("Informe o valor que deseja sacar: "))

#Estrutura condicional IF:
if saque <= saldo:
    print("Realizando saque")
    
if saque > saldo:
    print("Saldo insuficiente")
    
#Estrutura condicional IF/ELSE:
if saque <= saldo:
    print("Realizando saque")
else:
    print("Saldo insuficiente")
    
#Estrutura condicional IF/ELIF/ELSE:
opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extrato "))

if opcao == 1:
    valor = float(input("Informe o valor que deseja sacar"))
    #...
elif opcao == 2:
    print("Exibindo Extrato...")
    #...
else:
    sys.exit("Opção inválida")
    
#IF aninhado
conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 200
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado")
    elif saque >= saldo:
        print("Saldo realizado com uso de cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
    elif saque >= saldo:
        print("Saldo insuficiente")