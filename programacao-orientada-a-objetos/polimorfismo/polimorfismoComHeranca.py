class Passaro:
    def voar(self):
        print("Voando...")
        
class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao voa")
        
def plano_voo(obj):
    obj.voar()
    
pardal = Pardal()
avestruz = Avestruz()

plano_voo(pardal)
plano_voo(avestruz)