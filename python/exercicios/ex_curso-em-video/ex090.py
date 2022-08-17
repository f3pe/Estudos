aluno = dict()
aluno['nome'] = str(input("digite o nome do aluno: "))
aluno['nota'] = float(input(f'digite a nota do {aluno["nome"]}:'))
if aluno['nota'] >= 7:
    aluno['situação'] = "Aprovado"
elif 5 <= aluno['nota'] < 7:
    aluno['situação'] = "Recuperação"
else:
    alino['situação'] = "Reprovado"
print("=="*20)
print(f"O aluno {aluno['nome']} teve a media de {aluno['nota']}\ne está com a situação: {aluno['situação']}")
        
