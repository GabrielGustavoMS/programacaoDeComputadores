compra = float(input("Digite o valor da compra  para saber o valor final:   "))

if compra>= 200:
    valorfinal = compra - (compra*20/100)
    print("o valor final da compra é:  ","\n", valorfinal)

else:
    print("o valor final da compra é:  ", compra)

