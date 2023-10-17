import math

MQ = float(input("Digite os m²: "))
MQ_MAIS_DEZ = MQ * 1.0

RL = 6
LL = 18
PL = 80
RLA = RL * LL
LG = 3.6
PG = 25
RG = RL * LG

somente_latas = math.ceil(MQ / RL)
somente_galoes = math.ceil(MQ / RG)
latas = math.floor(MQ_MAIS_DEZ / RLA )
galoes= math.ceil((MQ_MAIS_DEZ % RL) / RG )

print("Somente latas: {}\nCustando R${}\nSomente galões: {}\nCustando R${}\nLatas: {} , galões: {}\n Custando: R${}".format(somente_latas,somente_latas*PL,somente_galoes,somente_galoes*PG,latas,galoes,(latas*PL)+(galoes*PG)))