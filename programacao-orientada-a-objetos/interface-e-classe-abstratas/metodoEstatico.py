class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
        
    @staticmethod #Quando nao preciso de contexto
    def e_maior_de_idade(idade):
        return idade >= 18
    

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(15))

