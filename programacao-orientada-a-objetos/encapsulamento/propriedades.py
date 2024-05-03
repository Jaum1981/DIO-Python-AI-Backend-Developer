#Exemplo

class Foo:
    def __init__(self, x=None):
        self._x = x
        
    @property #transforma um metodo em propriedade
    def x(self):
        return self._x or 0
    
    @x.setter #so assim para a linha23 funcionar daquele jeito
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
        
    @x.deleter
    def x(self):
        self._x = -1
        
foo = Foo(10)
print(foo.x) #se eu nao tivesse colocado o @property retornaria o endereço
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)