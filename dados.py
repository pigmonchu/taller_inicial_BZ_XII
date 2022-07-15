from ast import comprehension
from random import randint

rondas = {}
for i in range(2, 13):
    rondas[i] = 0

esperado = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

def tiradaDoble():
    return randint(1, 6) + randint(1, 6)

for i in range(1000):
    puntos = tiradaDoble()
    rondas[puntos] = rondas[puntos] + 1

print(rondas)
