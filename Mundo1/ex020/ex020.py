from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
aluno5 = str(input('Quinto aluno: '))
lista_de_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
shuffle(lista_de_alunos)
print('A ordem de apresentação será')
print(lista_de_alunos)
