def exibir_mensagem():
    print("Hello World!")
    
def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}")
    
def exibir_mensagem3(nome= "Victor"):
    print(f"Seja bem vindo {nome}!!!")

exibir_mensagem()
exibir_mensagem2("Victor")
exibir_mensagem3()
exibir_mensagem3("Pedro")

#Retornando valores:
def calcula_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

calcula_total([10, 20, 30]) #>>> 60
retorna_antecessor_e_sucessor(10) #>>> (9, 11)

#Argumentos nomeados:
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Fiat","Palio", 1999,"FDS-2345") #>>> Carro inserido com sucesso: Fiat/Palio/1999/FDS-2345
salvar_carro(**{"marca": "fiat", "modelo": "palio", "ano": 1998, "placa": "ABC-1234"}) 
#>>> Carro inserido com sucesso: fiat/palio/1998/ABC-1234
print()

#Args e Kwargs (*args e **kwargs) tupla e dict respectivamente
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
    
exibir_poema(
    "Quarta-feira, 01 de maio de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)