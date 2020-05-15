n1 = float(input('Digite o 1º número:   '))
n2 = float(input('Digite o 2º número  '))
operação = input('Digite a operaçõa que deseja aplicar sobre eles considerando as seguintes: +, -, *, /  ')
if operação == '+':
    vf = n1+n2
elif operação == '-':
    vf = n1-n2

elif operação == '*':
    vf = n1*n2

elif operação == '/':
    vf = n1/n2

    
print('O resultado da ',operação,'é:',vf)
