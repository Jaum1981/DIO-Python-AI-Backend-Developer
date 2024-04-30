#Exemplo lista:
frutas = ['banana', 'maçã', 'uva']

frutas = []

letras = list('Python') #>>> ['P', 'y', 't', 'h', 'o', 'n']

numeros = list(range(10)) #>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ['Ferrari', 'F8', 4200000, 2020, True]

#Acesso direto:
frutas = ['banana', 'maçã', 'uva']
frutas[2] #>>> uva
frutas[-2] #>>> maçã

#Lista aninhada:
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 7, 'c']
]

matriz[0] #>>> [1, 'a', 2]
matriz[0][0] #>>> 1
matriz[0][-1] #>>> 2
matriz[-1][-1] #>>> 'c'

#Fatiamento
lista = ['P', 'y', 't',' h', 'o', 'n']

lista[2:] #>>> ['y', 't']
lista[:2] #>>> ['P', 't']
lista[1:3] #>>> ['P', 'y']
lista[0:3:2] #>>> ['P', 't']
lista[::] #>>> ['P', 'y', 't', 'h', 'o', 'n']
lista[::-1] #>>> ['n', 'o', ' h', 't', 'y', 'P']

#iteração de lista:
carros = ['gol', 'celta', 'palio']
for carro in carros:
    print(carro)
    
#Função enumerate:
carros = ['gol', 'celta', 'palio']
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
    
#Compreensão de lista:
numeros = [1, 2, 56, 7654, 7645, 2222, 0]
pares = []

#Versão 1:
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

#Versão 2;       
pares = []
pares = [numero for numero in numeros if numero %2 == 0]
        #retorno| Iteração 

#Modificando lista:
numeros = [1, 2, 56, 7654, 7645, 2222, 0]
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)
