from random import *
canBuy = []  # tupla
isFood = False
foods = ["maçã", "melão", "melancia", "banana", "cenoura", "arroz", "feijão"]
products = {"maçã", "banana", "cenoura",
            "arroz", "feijão", "shampoo", "martelo", "música", "carro", "sabonete"}
prices = {}
dinheiro = int(input("Digite o seu montante de dinheiro: R$"))

for x in list(products):
    if x in foods:
        isFood = True
    prices[x] = randint(0, 9)
    if dinheiro >= prices.get(x) and isFood == True or x[0:1] == "m":
        aux = list(canBuy)
        aux.append(["Inicial: ", x[0:1], {x}, {"Preço R$": prices.get(x)},
                    "É comida?: ", isFood])
        canBuy = tuple(aux)

print("Lista de comidas ou produtos com a letra m que você pode comprar: \n")
print(canBuy)
