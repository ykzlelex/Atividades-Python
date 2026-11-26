lista_de_convidades = []
for nome in range (1, 4):
    nome = input(f"digite o nome do {nome}° convidado: ")
    lista_de_convidades.append(nome)
lista_de_convidades.pop(2)
print(lista_de_convidades)