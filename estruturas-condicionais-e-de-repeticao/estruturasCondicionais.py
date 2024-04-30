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