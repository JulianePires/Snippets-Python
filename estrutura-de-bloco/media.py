import math

notas = []

for x in range(4):
    notas.append(float(input("Insira uma nota: ")))

media = math.fsum(notas)//len(notas)

if media >= 7:
    print(f"Parabéns! Você foi aprovado com média {media:.1f}")
elif media >= 3:
    print(f"Você foi para a final com média {media:.1f}")
else:
    print(f"Sentimos muito, você foi reprovado com média {media:.1f}")
