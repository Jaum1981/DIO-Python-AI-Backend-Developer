#Método append()
lista = []

lista.append(1)
lista.append('Python')
lista.append(True)
lista.append([10, 45, 6])

print(lista) #>>> [1, 'Python', True, [10, 45, 6]]

#Método clear():
lista = [1, 'Python', True, [10, 45, 6]]
lista.clear()
print(lista) #>>> []

#Método copy():
lista = [1, 'Python', True, [10, 45, 6]]
lista.copy()
print(lista) #>>> [1, 'Python', True, [10, 45, 6]]

#Método count():
cores = ['vermelho', 'verde', 'azul', 'verde']
cores.count('vermelho') #>>> 1
cores.count('verde') #>>> 2
cores.count('azul') #>>> 1

#Método extend():
linguagens = ['Python', 'C++', 'Java']
linguagens.extend(['C#', 'Js'])
print(linguagens) #>>> ['Python', 'C++', 'Java', 'C#', 'Js']

#Método index():
linguagens = ['Python', 'C++', 'Java', 'Python']
linguagens.index('Python') #>>> 0
linguagens.index('C++') #>>> 2

#Método pop():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
linguagens.pop() #Js
linguagens.pop() #C#
linguagens.pop() #Java
linguagens.pop(0) #Python

#Método remove():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js', 'Java']
linguagens.remove('Java') #>>> ['Python', 'C++', 'C#', 'Js', 'Java']

#Método reverse():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
linguagens.reverse() #>>> ['Js', 'C#', 'Java', 'C++', 'Python']

#Método sort():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
linguagens.sort() #>>> ['C#', 'C++', 'Java', 'Js', 'Python']
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
linguagens.sort(reverse=True) #>>> ['Python', 'Js', 'Java', 'C++', 'C#']
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
linguagens.sort(key=lambda x: len(x)) #>>> ['C#', 'Js', 'C++', 'Java', 'Python']

#Método sorted():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
sorted(linguagens, key=lambda x: len(x)) #>>> ['C#', 'Js', 'C++', 'Java', 'Python']

#Método len():
linguagens = ['Python', 'C++', 'Java', 'C#', 'Js']
len(linguagens) #5