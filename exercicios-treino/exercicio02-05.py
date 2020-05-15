g = input('Digite seu sexo M/F:    ')
h = float(input('Digite sua altura   '))


if g == 'M':
    peso = 22*h**2
else:
    peso = 20.8*h**2
print('O seu peso ideal é  ',peso'Kg')
