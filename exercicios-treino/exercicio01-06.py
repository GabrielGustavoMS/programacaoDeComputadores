compra = float(input('Digite o valor da compra:  '))
parcelas = int(input('Digite o número de parcelas que deseja considerando as seguintes opções: \n 2,4,6,8  '))

if parcelas ==2:
    compra = compra + (compra*3/100)
elif parcelas == 4:
    compra = compra + (compra*7/100)
elif parcelas == 6:
    compra = compra + (compra*9/100)
elif parcelas == 8:
    compra = compra + (compra*12/100)

print('O valor final da compra é de :   ', compra)
