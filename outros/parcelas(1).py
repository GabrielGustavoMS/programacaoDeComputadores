total = float(input("Valor total da compra: "))
parcelas = int(input("Qual o número de parcelas (2, 4, 6 ou 8): "))

if parcelas==2:
    juros = 3
elif parcelas==4:
    juros = 7
elif parcelas==6:
    juros = 9
else:
    juros = 12

total = total + (total*juros/100)
parcela = total / parcelas

print("O valor de cada parcela será", parcela)
