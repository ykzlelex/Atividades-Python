def compras(dinheiro, custo):
    if (dinheiro >= custo):
        return ("comprado com sucesso! Carla pod comprar o que ela quiser")
    else:
        falta = custo - dinheiro
        return (f"ops! dimheiro insuficiente, falta R${falta:.2f}")
dinheiro = float(input("quanto dinheiro Carla tem?: R$"))
custo = float(input("qual o valor total das compras?: R$"))
resul = compras (dinheiro, custo)
print(resul)