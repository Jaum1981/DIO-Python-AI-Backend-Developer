class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
        
def mostrar_valores(*objs):
    for _ in objs:
        print(_)        

        
gui = Estudante("Guilherme", 51044)
gigi = Estudante("Giovana", 59324)

mostrar_valores(gui, gigi)

gui.matricula = 99999
Estudante.escola = "Pyhton"
gigi.escola = "Dio"
mostrar_valores(gui, gigi)