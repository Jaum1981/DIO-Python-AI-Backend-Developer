#publico: Pode ser acessado de fora da classe
#privado: So pode ser adessado pela classe
#Exemplo:
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo #privado
        self.nro_agencia = nro_agencia
        
    def sacar(self, valor):
        self._saldo -= valor
    
    def depositar(self, valor):
        self._saldo += valor

    def mostrar_saldo(self):
        return f"Saldo de : {self._saldo}"
        
conta = Conta("001", 100)
print(conta._saldo)#Errado
print(conta.mostrar_saldo())