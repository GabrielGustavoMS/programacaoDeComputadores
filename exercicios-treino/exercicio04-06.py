a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

if a>b and a>c:
    m = a
elif b>c:
    m = b
    
elif c>b:
    m = c

else:
    m =a

print(m)
    
