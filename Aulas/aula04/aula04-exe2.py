salario = float(input("Entre com o salário==>  "))

porcentagem = float(input("Entre com a porcentagem de aumento==>"))
aumento= salario*porcentagem/100
salario = salario + aumento
print("o novo salário = ",salario,"o valor do aumento",aumento)
