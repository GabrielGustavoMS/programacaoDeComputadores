numb1 = float(input("Digite o 1º número: "))
numb2 = float(input("Digite o 2º número: "))

operador = input("Digite o símbolo da operação, considerando as opções:+ , - , *, / ")

if operador == "+":
    result = numb1 + numb2
elif operador == "-":
    result = numb1 - numb2
elif operador == "*":
    result = numb1 * numb2
elif operador == "/":
    result = numb1 / numb2

print("O resultado da operação é ===> : ",result)

