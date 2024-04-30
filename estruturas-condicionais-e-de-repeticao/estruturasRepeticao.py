#Estrutura de repetição For:
texto = input("Informe um texto: ")
VOGAIS = "AIEOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") #end="" substitui a quebra de texto por um string vazia
        
print() #Quebra de linha

#Função built-in Range():
list(range(4)) #>>>[0, 1, 2, 3]

#Utilizando o range com for:
for numero in range(0, 11):
    print(numero, end="")

for numero in range(0, 51, 5):
    print(numero, end="") #exibe de 5 em 5
    
#Estrutura de repetição While:

opcao = -1

while opcao !=0:
    opcao = int(input("Digite a opcao: [1] Sacar\n[2] Extrato\n[0] Sair\n"))
    
    if opcao == 1:
        print("Sacando")
        #...
    elif opcao == 2:
        print("Exibindo Extrato")