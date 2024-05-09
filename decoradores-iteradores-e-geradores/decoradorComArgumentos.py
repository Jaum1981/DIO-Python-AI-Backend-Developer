def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope
#para mais de um parametro na funcao ola_mundo

@meu_decorador
def ola_mundo(nome):
    print(f"Olá {nome}!")


ola_mundo("joao")



def meu_decorador2(funcao):
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado
    
    return envelope

@meu_decorador2
def linguagem(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

a = linguagem("python")
print(a) 