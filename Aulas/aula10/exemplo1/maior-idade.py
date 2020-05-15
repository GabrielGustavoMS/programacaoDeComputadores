maior_altura=0
contador = 1
while contador <=10:
    print('---Aluno',contador,' ---')
    altura = int(input('Qual é a altura do aluno?'))
    if altura > maior_altura:
        maior_altura = altura

        contador = contador + 1

else:
    print('A maior altura é',maior_altura)
