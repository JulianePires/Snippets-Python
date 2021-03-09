import math

area = float(input("Informe o tamanho da área a ser pintada em m²: "))
cobertura = (area/3)  # litros/m²
latasTinta = math.ceil(cobertura/18)
precoTotal = latasTinta * 80

print(f"Latas de tinta: {latasTinta}")
print(f"Valor total: R${precoTotal:.2f}")
