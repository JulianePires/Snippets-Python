peso = float(input("Digite o peso total de peixes (KG): "))
peso_max = 50.0
excesso = 0
multa = 0

if peso > peso_max:
    excesso = peso - peso_max
    multa = 4 * excesso

print(f"O valor do peso em excesso é {excesso:.1f}KG\n")
print(f"O valor da multa a ser paga é de R${multa:.2f}")
