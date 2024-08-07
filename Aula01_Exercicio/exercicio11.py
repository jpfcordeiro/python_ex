produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco = float(input("Digite o preço unitário: "))
total = quantidade * preco
print(f"O produto {produto} foi comprado {quantidade} vezes, resultando em R${total}")