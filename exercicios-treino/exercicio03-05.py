compra = float(input('Digite o valor da compra:   '))

if compra>200:
    compra  = compra - compra*20/100
print('O valor final da compra é :  ', compra)
