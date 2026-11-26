nome_de_cidade = ['GUARULHOS', 'VENZA''MARACANAU', 'FORTALEZA', 'ATENAS', 'BANDEIRANTE', 'JEREISSATI 3']
cidade = input(f"digite a cidade que você deseja encontrar: ").upper().strip()
if cidade not in (nome_de_cidade):
    print(f'NÃO ENCONTRADA')
else:
    print(f'a cidade de {cidade} encontrada! posição {cidade.index(cidade)}')