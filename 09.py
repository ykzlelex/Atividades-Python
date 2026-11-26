lista_de_compras =[]
for itens in range(1, 6):
    itens = str(input(f"digite o {itens}º da lista: "))
    lista_de_compras.append(itens)
    print(f"o primeiro item da lista foi {lista_de_compras[0]} e o ultimo foi {lista_de_compras[-1]}")