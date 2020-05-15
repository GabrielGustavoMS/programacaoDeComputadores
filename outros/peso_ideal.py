altura = float(input("Entre com a sua altura: "))
sexo = input("Entre com o seu sexo (M/F): ")

if sexo=="M":
    peso = 22.0*altura**2
else:
    peso = 20.8*altura**2

print("O seu peso ideal é", peso)
    
