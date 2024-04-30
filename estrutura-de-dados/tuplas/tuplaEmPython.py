#Criando tupla:
frutas = ('laranja', 'maçã', 'uva',)
letras = tuple('Python')
numeros = tuple([1, 2, 3])
pais = ('Brasil',)

#Tupla aninhadas
matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 7, 'c'),
)

matriz[0] #>>> (1, 'a', 2)
matriz[0][0] #>>> 1
matriz[0][-1] #>>> 2
matriz[-1][-1] #>>> 'c'

#Fatiamento de tuplas:
tupla = ('P', 'y', 't',' h', 'o', 'n')

tupla[2:] #>>> ('y', 't')
tupla[:2] #>>> ('P', 't')
tupla[1:3] #>>> ('P', 'y')
tupla[0:3:2] #>>> ('P', 't')
tupla[::] #>>> ('P', 'y', 't', 'h', 'o', 'n')
tupla[::-1] #>>> ('n', 'o', ' h', 't', 'y', 'P')

#Método count():
frutas = ('laranja', 'maçã', 'uva', 'laranja',)
frutas.count('laranja') # 2

#Método len():
frutas = ('laranja', 'maçã', 'uva',)
len(frutas) # 3

#Método index()
frutas = ('laranja', 'maçã', 'uva',)
frutas.index('maçã') # 1