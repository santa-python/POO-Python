class Animal:
    def __init__(self, cor, nome):
        self._cor = cor
        self._nome = nome


#definindo a classe Mamifero, herdando de Animal
class Mamifero(Animal):
    def __init__(self, cor, nome, comida):
        Animal.__init__(self, cor, nome)
        self._comida = comida
    def Alimento(self):
            print(f"{self._nome} É um Mamífero, ou seja, ele se alimenta de {self._comida}")
        
  
# definindo Felino
class Felino(Mamifero):
    def __init__(self, cor, nome, ataque):
        self._ataque = ataque
        Animal.__init__(self, cor, nome)
    def Tipo(self):
            print(f"{self._nome} é do tipo Felino e ataca com {self._ataque}")

# definindo Gato
class Gato(Felino):
    def __init__(self, cor, nome, fofura):
        self._fofura = fofura
        Animal.__init__(self, cor, nome)
    def Fofo(self):
            print(f"{self._nome} é um Gato {self._cor}, então é {self._fofura}")


p = Mamifero("branco", "Luci", "leite")
p.Alimento()


p2 = Felino("Cinza", "Sandy", "Garras")
p2.Tipo()

p3 = Gato("Tigrado", "Mel", "Arisco")
p3.Fofo()
   