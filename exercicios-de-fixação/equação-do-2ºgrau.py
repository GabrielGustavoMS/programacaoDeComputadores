a = int(input('Digite o coeficiente a :  '))
b = int(input('Digite o coeficiente b :  '))
c = int(input('Digite o coeficiente c :  '))

delta = b**2 - 4*a*c

x1= (-b + delta**1/2)/(2*a)
x2= (-b - delta**1/2)/(2*a)
if delta<0:
    print('Nao existe solução real')

else:
    print('Raiz 1 =',x1,"/n Raiz2 = ",x2)
