dia = int(input('Digite o dia  '))
mes = int(input('Digite o Mês  '))
ano = int(input('Digite o Ano  '))

if mes>12 or mes<1:
    mes =('inválido')

    
elif (mes==1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes ==12) and (dia<1 or dia>31):
    dia = 'inválido'

elif (mes == 4 or mes ==6 or mes ==9 or mes==11) and (dia<1 or dia>30):
    dia = 'inválido'
elif mes ==2 and (dia<1 or dia>28):
    dia = 'inválido'

if dia == 'inválido' or mes == 'inválido':
    data ='Data Inválida'
else:
    data = 'Data Válida'

print(data)
