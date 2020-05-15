nda = 0
aprovados = 0
soma=0
while nda<80:
    nda=nda+1
    nota=float(input('Digite a nota do aluno'))
    soma=soma+nota
   
    
    if nota>=6:       
        aprovados=aprovados+1
else:
     mediadaturma=soma/nda
print('Número de aprovados:',aprovados,',Média da turma',mediadaturma)
    
    
