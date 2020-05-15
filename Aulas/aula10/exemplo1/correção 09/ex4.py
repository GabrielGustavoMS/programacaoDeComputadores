idade= 18
while idade>0:
    idade = int(input("Entre com a idade:"))
    sexo = input('qual o sexo?')
    salario = float(input('Qual o salário'))

    if idade>0:
        soma_idade = soma_idade + idade
        conta_idade = conta_idade+1

        if sexo=='M':
            soma_idade = soma_idade + idade
            conta_homem = conta_homem+1
        if sexo=='F' and salario<600:
            conta_mulher = conta_mulher+1
else:
    print('A média de idade do grupo é: ',soma_idade/conta_idade,'A média de salário dos homens',soma_homem/conta_homem,'O númeo de mulheres com salário<600',conta_mulher)
    
        
