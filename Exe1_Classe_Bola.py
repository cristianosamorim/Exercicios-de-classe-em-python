"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

import math

class Bola:
    def __init__(self,Cor,raio):
        self.cor = Cor
        self.raio = raio
    
    def trocaCor(self,cor2):
        self.cor = cor

    def mostraCor(self):
        print(f"Cor: {self.cor}")

    def Area(self):
        return 4 * math.pi * math.pow(self.raio,2)


cor = input("Qual a cor da bola?: ")
raio = int(input("Digite o raio: "))
bola = Bola(cor,raio)
Bola.mostraCor()
Bola.trocaCor("azul")
Bola.mostraCor()
print(f"Area: {Bola.Area}")