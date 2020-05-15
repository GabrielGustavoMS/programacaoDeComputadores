num_alunos = 10
nomes = []
notas = []

media = 0

for i in range (num_aluno):
    nomes.append(input('Informe o nome do aluno: '))
    notas.append(eval(input('Informe a nota de ' + nomes[i] + ":")))

    media = media + notas[i]

media = media / num_alunos

for i in range(len(nomes)):
    if notas[i] > media:
        print("parabéns", nomes[i], notas[i])
