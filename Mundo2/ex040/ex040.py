nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1} e {nota2}, a média do aluno é {media}')

if (media < 5):
    print('O aluno está em RECUPERAÇÃO!')
elif ((media >= 5) and (media <= 6)):
    print('O aluno PASSOU, mas foi por POUCO...')
elif (media >= 7):
    print('O aluno foi APROVADO com SUCESSO!')
