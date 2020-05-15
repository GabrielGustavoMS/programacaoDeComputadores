numero = int(input('Digite um número inteiro: '))

if numero<0:
    print('Não exite fatorial de número negativo')
else:
    fatorial = 1
    contador = numero

    while contador > 0:
             fatorial = fatorial * contador
             contador = contador - 1
    else:
        print('O fatorial de',numero,'é',fatorial)
             
             
