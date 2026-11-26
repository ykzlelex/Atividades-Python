def filtar_numeros_pares(lista):

    return [num for num in lista if num % 2 == 0]

num= [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

pares= filtar_numeros_pares(num)

print(f'os numeros pares da lista {num} são {pares}')