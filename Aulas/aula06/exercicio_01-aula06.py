valor = float(input("Digite o valor total da compra:   "))
n = int(input("Digite o número de parcelas que você deseja, considerando as seguintes opções: \n 2, 4, 6, 8 ===>   "))
if n==2:
   parcela = (valor*(3/100) + valor)/2
elif n==4:
    parcela = (valor*(7/100) + valor)/4
elif n==6:
    parcela = (valor*(9/100) + valor)/6
elif n==8:
    parcela = (valor*(12/100) + valor)/8 
    



print("O valor final é da parcela ", parcela)
