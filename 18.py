def maior_de_tres (a,b,c):

    return maior

a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))

maior= a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f'o maior numero entre {a}, {b}, {c} é: {maior_de_tres(a,b,c)}')