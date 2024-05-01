#Set(Conjunto)
#nao tem index
set([1, 2, 3, 1, 3, 4]) #>>> {1, 2, 3, 4}
set("abacaxi") #>>> ["b", "a", "c", "x", "i"]
set(("palio", "celta", "gol", "palio")) #>>> {"gol", "celta", palio}
linguagens = {"Python", "Java", "Python"}

#Acessando dados
numeros = {1, 2, 3, 4, 2}
numeros = list(numeros)
numeros[1] #>>> 2

#Usando o enumerate:
carros = {"Palio", "Celta", "Siena"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
#Metodo union():
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) #>>> {1, 2, 3, 4}

#Metodo intersection():
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.intersection(conjunto_b) #>>> {2, 3}

#Metodo diference():
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_a.difference(conjunto_b) #>>> {1, 2}

#Metodo symmetric_difference():
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_a.symmetric_difference(conjunto_b) #>>> {1, 2, 4, 5}

#Metodo issubset():
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issubset(conjunto_b) #>>> True
conjunto_b.issubset(conjunto_a) #>>> False

#Metodo issuperset():
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issuperset(conjunto_b) #>>> False
conjunto_b.issuperset(conjunto_a) #>>> True

#Metodo isdisjoint():
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
conjunto_a.isdisjoint(conjunto_b) #>>> True
conjunto_a.isdisjoint(conjunto_c) #>>> False

#Metodo add():
sorteio = {1, 23}

sorteio.add(25) #>>> {1, 23, 25}
sorteio.add(42) #>>> {1, 23, 25, 42}
sorteio.add(25) #>>> {1, 23, 25, 42}

#Metodo clear():
sorteio = {1, 23, 25, 42}

sorteio.clear(25) #>>> {1, 23, 42}
sorteio.add(42) #>>> {1, 23}


#Metodo copy():
sorteio = {1, 23, 25, 42}

sorteio.copy() #>>> {1, 23, 25, 42}

#Metodo discard():
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1) #>>> {0, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(67) #>>> {0, 2, 3, 4, 5, 6, 7, 8, 9}

#Metodo pop():
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.pop() #>>> 0
numeros.pop() #>>> 1
print(numeros) #>>> {2, 3, 4, 5, 6, 7, 8, 9}

#Metodo remove():
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.remove(1) #>>> 1
numeros.remove(67) #>>> Error

#Metodo len():
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros) #>>> 10

#Metodo in():
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
1 in numeros #>>> True
99 in numeros #>>> False