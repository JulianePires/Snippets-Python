import math

area = float(input("Informe o tamanho da área a ser pintada em m²: "))
cobertura = (area/6)
coberturaTotal = cobertura * 1.1
latasTinta = math.ceil(coberturaTotal/18)
galoesTinta = math.ceil(coberturaTotal/3.6)

print(f"Valor em latas de 18l: R${latasTinta*80:.2f}")
print(f"Valor em galões de 3,6l: R${latasTinta*25:.2f}")
