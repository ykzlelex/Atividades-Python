def somar_todos(*numeros):

    return sum(numeros)

numeros = [1, 2, 3, 4, 5]

print(f'a soma de todos os numeros  é {somar_todos(*numeros)}')