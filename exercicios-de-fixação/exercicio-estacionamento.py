hent= int(input('Digite as horas de entrada'))
ment = int(input('Digite os minutos de entrada'))

hs= int(input('Digite as horas de saída'))
ms = int(input('Digite os minutos de saída '))

t0 = hent*60 + ment
t1 = hs*60 + ms

tempo = t1 -t0
print(tempo,'Minutos se Passaram desde sua entrada.')
