num1 = float(input("Qual o primeiro número: "))
num2 = float(input("Qual o segundo número: "))
operacao = input("Qual é a operação (+ ou - ou * ou /): ")

if operacao=="+":
    resp = num1 + num2
elif operacao=="-":
    resp = num1 - num2
elif operacao=="*":
    resp = num1 * num2
elif operacao=="/":
    resp = num1 / num2

print(resp)
    
