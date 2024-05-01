#Metodo clear()
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

contatos.clear() #>>> {}

#Metodo copy():
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

copia = contatos.copy() #>>> copia == contatos

#Metodo fromkeys()
dict.fromkeys(["nome", "idade"]) #>>> {"nome" : None, "Idade": None}
dict.fromkeys(["nome", "idade"], "vazio") #>>> {"nome" : "vazio", "Idade": "vazio"}

#Metodo get():
contatos = {
    "joao@gmail.com" : {
        'Nome': 'João',
        'Idade': 21,
        'Nacionalidade': 'Brasileiro',
        'Telefone': '4002-8922'
    }
}

contatos["chave"] #>>> KeyError

contatos.get("chave") #>>>None
contatos.get("chave", {}) #>>> {}
contatos.get("joao@gmail.com") #>>> {'Nome': 'João Victor', 'Idade': 21,
                                     #'Nacionalidade': 'Brasileiro', 'telefone': '4002-8922'}

#Metodo items():
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)

#Metodo keys():
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

#Metodo pop():
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)

#Metodo popitem():
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError

#Metodo setdefault():
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

#Metodo update():
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)

#Metodo values():
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)

#Metodo in:
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

#Metodo del:
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 
# 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
# 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}
print(contatos)