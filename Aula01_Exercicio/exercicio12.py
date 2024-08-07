alt_parede = float(input("Digite a altura da parede: "))
larg_parede = float(input("Digite a largura da parede: "))
alt_azulejo = float(input("Digite a altura do azulejo: "))
larg_azulejo = float(input("Digite a largura do azulejo: "))
area_parede = alt_parede * larg_parede
area_azulejo = alt_azulejo * larg_azulejo
total_azulejos = area_parede / area_azulejo
print(f"O total de azulejo necessários é: {total_azulejos}")