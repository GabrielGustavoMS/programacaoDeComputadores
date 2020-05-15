numero = int(input("Entre com um número de 0 a 100: "))

if numero>100:
    print("O número deveria ser entre 0 e 100. Não sabe ler?")
else:
    if numero%3==0:
        print("O número é múltiplo de 3")
    else:
        print("O  número não é múltiplo de 3")
