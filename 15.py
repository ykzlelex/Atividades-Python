def saudar (nome, periodo = "dia"):
    if periodo == "dia":
        print(f"bom dia, {nome}!")
    elif periodo == "tarde":
        print(f"boa tarde, {nome}!")
    elif periodo == "noite":
        print(f"boa noite, {nome}!")
saudar('elano')
saudar('vera')
saudar('elano', 'noite')
saudar('vera', 'tarde')