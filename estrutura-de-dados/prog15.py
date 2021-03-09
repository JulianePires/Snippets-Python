salarioPorHora = float(input("Quanto você ganha por hora?"))
horasTrabalhadas = int(input("Quantas horas você trabalhou no mês?"))

salarioBruto = salarioPorHora * horasTrabalhadas
descontoImposto = salarioBruto * 0.11
descontoINSS = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - descontoImposto - descontoINSS - descontoSindicato

print(f"Salário Bruto : R${salarioBruto:.2f}")
print(f"IR (11%) : R${descontoImposto:.2f}")
print(f"INSS : R${descontoINSS:.2f}")
print(f"Sindicato : R${descontoSindicato:.2f}")
print(f"Salário Líquido : R${salarioLiquido:.2f}")
