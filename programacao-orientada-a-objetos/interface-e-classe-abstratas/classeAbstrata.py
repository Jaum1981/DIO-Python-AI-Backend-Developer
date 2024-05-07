from abc import ABC, abstractmethod
class controleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass
    
    

class controleTV(controleRemoto):
    
    def ligar(self):
        print("Ligando")
        
    def desligar(self):
        print("Desligando")
        
    @property
    def marca(self):
        return "LG"


controle = controleTV()
controle.ligar()
controle.desligar()
print(controle.marca)