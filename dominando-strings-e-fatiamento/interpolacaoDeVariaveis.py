#Interpolação por metodo format:
nome = "João Victor"
idade = 21
profissao = "Programador"
curso = "Ciência da Coputação"

print("Olá me chamo {}. Eu tenho {} anos e estudo {}, estou matriculado no curso de {}.".format(
    nome, idade, profissao, curso))

print("Olá me chamo {2}. Eu tenho {1} anos e estudo {0}, estou matriculado no curso de {3}.".format(
    profissao, idade, nome, curso))

print("Olá me chamo {nome}. Eu tenho {idade} anos e estudo {profissao}, estou matriculado no curso de {curso}.".format(
    nome=nome, idade=idade, profissao=profissao, curso=curso))

pessoa = {"nome" : "João Victor",
    "idade" : 21,
    "profissao" : "Programador",
    "curso" : "Ciência da Coputação"}

print("Olá me chamo {nome}. Eu tenho {idade} anos e estudo {profissao}, estou matriculado no curso de {curso}.".format(**pessoa))

#Interpolação por metodo f-string:

nome = "João Victor"
idade = 21
profissao = "Programador"
curso = "Ciência da Coputação"

print(f"Olá me chamo {nome}. Eu tenho {idade} anos e estudo {profissao}, estou matriculado no curso de {curso}.")

#Formatando f-strings:
PI = 3.14159

print(f"O valor de PI é: {PI:.2f}") #>>> O valor de PI é: 3.14

print(f"O valor de PI é: {PI:10.2f}") #>>> O valor de PI é:       3.14