tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da conexão em Mbps: "))
tempo = (tamanho * 8) / velocidade
minutos =  tempo // 60
segundos = tempo % 60
print("{} Minutos e {} Segundos".format(minutos,segundos))