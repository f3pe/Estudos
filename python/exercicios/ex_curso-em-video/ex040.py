nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
if (nota1 + nota2) / 2 < 5:
    print("--"*20)
    print("Aluno reprovado")
    print("--"*20)
elif (nota1 + nota2) / 2 >= 5 and (nota1 + nota2) / 2 <= 6.9:
    print("--"*20)
    print("Aluno de recuperação")
    print("--"*20)
else:
    print("--"*20)
    print("Aprovado")
    print("--"*20)