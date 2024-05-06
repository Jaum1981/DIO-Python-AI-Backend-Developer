class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
        
    @classmethod    
    def criar_a_partir_da_data_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    
# p1 = Pessoa("Victor", 21)
# print(p1.nome, p1.idade)

p2 = Pessoa.criar_a_partir_da_data_de_nascimento(2002, 9, 28, "Victor")
print(p2.nome, p2.idade)