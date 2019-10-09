class  calculoRet:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def areaRet(self, x, y):
        self.x = x
        self.y = y
        self.c = self.x*y
        return self.c

    #def AreaRet2(self):
    #    return self.x * self.y

class Main:
    x = int(input('Digite o valor da Base: '))
    y = int(input('Digite o valor da Altura: '))
    c = calculoRet(x,y)
    print('Valor da Área = ', c.areaRet(x,y))
    input("Aperte qualquer botão para finalizar")
    