nome = str(input("Informe o seu nome: "))
idade = int(input("Informe a sua idade: "))
sexo = str(input("Informe o sexo M ou F: "))
rendaAtual = float(input("Informe a sua renda atual: "))

if rendaAtual == 0.0:
    print("Renda inválida, por favor, informe novamente o valor da sua renda.")

if sexo == 'F' and idade > 65:
    print("Obrigado {nome}, sua aposentadoria foi liberada no valor R${:.2f}".format(
        rendaAtual*0.7))
else:
    print(
        f"Obrigado {nome}, sua aposentadoria não foi liberada, faltam {65 - idade} anos.")
