nulos = int(input("Digite a quantidade de votos nulos: "))
brancos = int(input("Digite a quantidade de votos brancos: "))
validos = int(input("Digite a quantidade de votos válidos: "))
total = nulos + brancos + validos
per_nulos = (nulos * 100)/total
per_brancos = (brancos * 100)/total
per_validos = (validos * 100)/total

print(f"O total de votos é {total}, onde {per_nulos:.2f}% são nulos, {per_brancos:.2f}% são brancos e {per_validos:.2f}% são válidos.")