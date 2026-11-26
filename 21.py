def avaliar_media (n1, n2, n3):

    return media 

n1 =float(input('digite a primeira nota: '))
n2 =float(input('digite a segunda nota: '))
n3 =float(input('digite a terceira nota: '))

if media >= 7:
    print(f'parabens')
if media >= 5 and media <= 6.9:
    print('recuperação')
if media < 5:
    print('reprovado')

media = (n1+n2+n3)/3

print(f'a media do aluno é {media}')