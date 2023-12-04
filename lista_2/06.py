n1 = float(input("digite o primeiro número: "))
n2 = float(input("digiteo segundo número: "))
n3 = float(input("digite o terceiro número: "))
if n1 >= n2 >= n3 or n1 >= n3 >= n2:
    print(n1)
elif n2 >= n1 >= n3 or n2 >= n3 >= n1:
    print(n2)
elif n3 >= n1 >= n2 or n3 >= n2 >= n1:
    print(n3)