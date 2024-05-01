#Dicionario:
pessoa = {
    "Nome": "João Vicor",
    "Idade": 21,
    "Nacionalidade": "Brasileiro"
}
pessoa = dict(Nome="João Victor", Idade= 21, Nacionalidade= "Brasileiro")
pessoa["telefone"] = "4002-8922" #>>> {'Nome': 'João Victor', 'Idade': 21,
                                     #'Nacionalidade': 'Brasileiro', 'telefone': '4002-8922'}

#Acessando dados:
dados = {'Nome': 'João Victor',
         'Idade': 21,
         'Nacionalidade': 'Brasileiro',
         'telefone': '4002-8922'}

dados["Nome"] #>>> 'João Victor'
dados["Idade"] #>>> 21
dados["Nacionalidade"] #>>> 'Brasileiro'


dados["Nome"] = "Pedro"
dados["Idade"] = 20
dados["Nacionalidade"] = "Português"
print(dados) #>>> {'Nome': 'Pedro', 'Idade': 20,
                #'Nacionalidade': 'Português', 'telefone': '4002-8922'}
                
#Dicionario aninhado:
contatos = {
    "joao@gmail.com" : {
        'Nome': 'João',
        'Idade': 21,
        'Nacionalidade': 'Brasileiro',
        'Telefone': '4002-8922'
    },
    "victor@gmail.com" : {
        'Nome': 'Victor',
        'Idade': 19,
        'Nacionalidade': 'Brasileiro',
        'Telefone': '2004-2298'
    }
}

contatos["victor@gmail.com"]["Telefone"] = "2459-8922"

#iterar
contatos = {
    "joao@gmail.com" : {
        'Nome': 'João',
        'Idade': 21,
        'Nacionalidade': 'Brasileiro',
        'Telefone': '4002-8922'
    },
    "victor@gmail.com" : {
        'Nome': 'Victor',
        'Idade': 19,
        'Nacionalidade': 'Brasileiro',
        'Telefone': '2004-2298'
    }
}

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)