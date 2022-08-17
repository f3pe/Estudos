trabalhador = dict()
trabalhador['nome'] = str(input("Digite o nome: "))
trabalhador['idade'] = 2022 - int(input("Digite o ano de nascimento: "))
trabalhador['carteira'] = str(input("Digite o numero da carteira de trabalho[0 para não tem]: "))
if trabalhador['carteira'] != '0':
    trabalhador['contratação'] = int(input("digite o ano de contratação: "))
    trabalhador['salario'] = float(input("Digite o salario: "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['contratação'] + 35 + 2022) 
print("-="*30)
print(f"O nome tem o valor: {trabalhador['nome']}")
print(f"A idade tem o valor de: {2022 - trabalhador['idade']}")
print(f"O número da carteira de trabalho é: {trabalhador['carteira']}")
if trabalhador['carteira'] != '0':
    print(f"O ano de contratação foi: {trabalhador['contratação']}")
    print(f"O salario é de: {trabalhador['salario']}")
    print(f"A idade de aposentadoria prevista é de: {trabalhador['aposentadoria']}")


