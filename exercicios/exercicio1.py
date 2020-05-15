nomes = []
sal=[]
trabalhadores = 2
maior = 0
nomesm = []
for i in range(trabalhadores):
    nomes.append(input('Digite o nome do trabalhador '))
    sal.append(eval(input('Digite o salário do' + nomes[i])))
    if sal[i]>=maior:
        nomesm = nomes[i]
        maior = sal[i]
print(nomesm)      

