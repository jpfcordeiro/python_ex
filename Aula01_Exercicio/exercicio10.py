from math import pi
raio = int(input("Digite o raio do cilindro: "))
altura = int(input("Digite o valor da altura do cilindro: "))
volume = pi* (raio**2) * altura
print(f"O valor do volume do cilindro é: {volume:.2f}")