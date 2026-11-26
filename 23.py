def exibir_perfil(nome,**dados_extras):

    return nome, dados_extras

nome = input('digite seu nome: ')
dados_extras = {
    'idade': input('digite sua idade: '),
    'cidade': input('digite sua cidade: ')
}

exibir_perfil(nome, **dados_extras)