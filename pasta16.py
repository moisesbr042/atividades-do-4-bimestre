import math

MQ = float(input("Digite quantos metros quadrados você vai pintar: "))
latas = math.ceil(MQ/54)
preço = latas * 80
print("Você precisrá de {} lata(s) de tinta, custando R${}".format(latas,preço))