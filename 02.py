x = 1
while x<=10:
    valor=int(input("digite um valor: "))
    if valor>=10:
        print("não é aceito maior que 10")
    else:
        produto = x*valor
        print(f"tabuada do {valor} x {x} = {produto} ")
        x = x + 1

          