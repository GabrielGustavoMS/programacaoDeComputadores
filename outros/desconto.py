valor = float(input("Entre com o valor total: "))

if valor >= 200:
    valor = valor - (valor * 20 / 100)

print("O valor final será de", valor)
