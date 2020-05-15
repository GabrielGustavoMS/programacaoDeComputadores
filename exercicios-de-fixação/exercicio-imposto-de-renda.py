sal = float(input('Digite seu salário para saber o imposto '))

salanual = sal*12

if salanual>10000:
    imposto = salanual*(18.5/100)
else:
    imposto = salanual*(12/100)

print('O valor do imposo é : ',imposto)
