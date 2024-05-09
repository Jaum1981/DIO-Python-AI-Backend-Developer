import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        result = funcao(*args, **kwargs)
        return result
    
    return envelope


@meu_decorador
def ola(nome):
    print(f"Olá {nome}!")
    return nome.upper()

print(ola.__name__)