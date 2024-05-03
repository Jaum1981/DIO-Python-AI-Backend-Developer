class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        print(Ornitorrinco.__mro__) #Exibe a ordem de pesquisa da classe
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

cachorro1 = Cachorro(nro_patas=4, cor_pelo="Branco")
print(cachorro1)

ornitorrinco1 = Ornitorrinco(nro_patas=2, cor_pelo="Marrom", cor_bico="Vermelho")
print(ornitorrinco1)