a =int(input('Digite o coeficiente  A da equação ==>  '))
b =int(input('Digite o coeficiente  B da equação ==>  '))
c =int(input('Digite o coeficiente  C da equação ==>  '))

delta = b**2 -4*a*c


x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**(1/2))/(2*a)

if delta<0:
    print("Não existe solução real")
else:
    print("Raiz1: ",x1,"\n","Raiz2: ",x2)

    

