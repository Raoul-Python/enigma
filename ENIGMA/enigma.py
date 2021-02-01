import random

class Rotor():

    def __init__(self, abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):

        self.abecedario = abecedario
        self.rotor =  []
        otrasLetras = list(self.abecedario)

        for l in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)


    def codifica(self, letra):
        for t in self.rotor: # t es un tupla
            if letra == t[0]:
                return t[1]
        raise ValueError("{} no pertenece al abecedario.".format(letra))


rotor = Rotor()

print(rotor.resultado)
print(rotor.codifica("A"))
        
