class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def mostrar_nome(self):
        print(f"Olá, meu nome é {self.nome}")

    def mostrar_idade (self):
        print (f"Tenho {self.idade} anos")

class Estudante(Pessoa):
    def __init__(self, nome, idade, sexo):
        Pessoa.__init__(self, nome, idade)
        self.sexo = sexo

    def mostrar_sexo(self):
        print(f"Sou do Sexo {self.sexo}")

class Adulto(Pessoa):
    def __init__(self, nome, idade, trabalho):
        Pessoa.__init__(self, nome, idade)
        self.trabalho = trabalho
        
    def mostrar_trabalho(self):
        print(f"Eu trabalho como {self.trabalho}")
    
p = Pessoa("Carlos", 25)
p.mostrar_nome()
p.mostrar_idade()

p2 = Estudante ("Sergio", 18, "Masculino")
p2.mostrar_nome()
p2.mostrar_idade()
p2.mostrar_sexo()

p3 = Adulto ("Antonio", 42, "Cientista da Computação")
p3.mostrar_nome()
p3.mostrar_idade()
p3.mostrar_trabalho()
