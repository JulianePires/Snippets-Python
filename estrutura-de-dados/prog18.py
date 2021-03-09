tamanhoArquivo = float(
    input("Informe o tamanho de arquivo para download em MB: "))
velocidadeInternet = float(input("Informe a velocidade da internet em Mbps: "))

tempoDownload = tamanhoArquivo//velocidadeInternet

print(f"Tempo de download aproximado: {tempoDownload} minutos")
