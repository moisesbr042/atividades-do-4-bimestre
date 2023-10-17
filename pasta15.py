PH = float(input("Digite quanto você ganha por hora: "))
HT = float(input("Digite quantas horas você trabalhou esse mês: "))
SB = PH*HT
IR = SB*(11/100)
INSS = SB*(8/100)
SIN = SB*(5/100)
SL = SB - IR - INSS - SIN
print("Salário bruto: R${}\n IR (11%): R${}\n INSS (8%): R${}\n sindicato (5%): R${}\n Salário Liquido: R${}".format(SB,IR,INSS,SIN,SL))