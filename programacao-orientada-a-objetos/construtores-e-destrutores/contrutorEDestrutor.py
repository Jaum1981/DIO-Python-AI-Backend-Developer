class Cachorro:
    #Metodo construtor
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        print("Criando a instancia")
    
    #Metodo destrutor:
    def __del__(self):
        print("Destruindo a instancia")
        
    
def criar_cachorro(nome, cor):
    cachorro1 = Cachorro(nome, cor)
    print(cachorro1.nome)
    
criar_cachorro("Chipi chipi", "preto")
criar_cachorro("Chapa chapa", "branco")