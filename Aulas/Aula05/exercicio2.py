sexo = input("Digite seu Sexo m/f: ")
H = float(input("Digite a sua altura   "))

if sexo=="f":
    p = 20.8*H**2
    print("Seu peso ideal é:  ", p)
if sexo=="m":
    p = 22.0*H**2
    print("Seu peso ideal é:  ", p)
    

