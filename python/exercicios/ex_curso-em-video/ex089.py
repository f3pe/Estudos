res = 's'
lista = list()
while res not in 'nN':
    aluno = list()
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 01: ")))
    aluno.append(float(input("Nota 02: ")))
    lista.append(aluno[:])
    res = input("Deseja continuar[s/n]: ")
print("-="*40)
print("Nº  Nome     Média")
print("------------------------")
for i in range(0, len(lista)):
        print(f"{i:<4}{lista[i][0]:<12} {(lista[i][1]+lista[i][2])/2:>8.1f}")
while True: 
    num = int(input("Digite o numero do aluno que deseja ver as notas[999 para sair]"))
    if num == 999:
        print("Finalizando...")
        break
    print(f"{aluno[num][0]} Nota 1: {lista[num][1]} Nota 2: {lista[num][2]}")