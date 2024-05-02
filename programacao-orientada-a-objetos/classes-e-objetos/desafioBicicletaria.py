class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BIBIBIBIBIBI")

    def correr(self):
        print("correndo")

    def parar(self):
        print("Bicicleta parada")
        
    # def __str__(self):
    #     return f"Bicicleta {self.modelo}, da cor {self.cor}, ano: {self.ano}, R$: {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("azul", "Caloi", 2022, 900)

caloi.buzinar()
caloi.correr()
caloi.parar()
print(caloi)