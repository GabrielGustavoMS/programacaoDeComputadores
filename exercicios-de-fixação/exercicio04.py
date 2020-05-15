hent=int(input("Digite a hora de entrada:  " ))
ment=int(input("Digite os minutos de entrada:   "))

hsaida=int(input("Digite a hora de saída:   "))
msaida=int(input("Digite os minutos de saida:  "))

hent = (hent*60)
hsaida = (hsaida*60)

t0 = hent+ ment
t1 = hsaida + msaida

tf = t1-t0

print("Passaram-se",tf,"minutos desde o momento de entrada")



