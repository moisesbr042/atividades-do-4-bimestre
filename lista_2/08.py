p1 =float(input("ESCREVA QUAL É O PREÇO DO PRODUTO 1: "))
p2 =float(input("ESCREVA QUAL É O PREÇO DO PRODUTO 2: "))
p3 =float(input("ESCREVA QUAL É O PREÇO DO PRODUTO 3: "))
if p1 <= p2 <= p3 or p1 <= p3 <= p2:
    print("A melhor opção é o produto 1")
elif p2 <= p1 <= p3 or p2 <= p3 <= p1:
    print("A melhor opção é o produto 2")
elif p3 <= p1 <= p2 or p3 <= p2 <= p1:
    print("A melhor opção é o produto 3")