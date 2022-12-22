#Exercício Python 094
def main():
    cadastros = list()
    somaIdades = qtdf = 0
    op = 's'
    while(op not in "nN"):
        temp = dict()
        temp['nome'] = input("Nome: ")
        while(True):
            temp['sexo'] = input("Sexo[F/M]: ")
            if temp['sexo'] in "FfMm":
                break
            else:
                print("Opção invalida, Digite novamente")
        if temp['sexo'] in "fF":
            qtdf += 1
        temp['idade'] = int(input("Idade: "))
        somaIdades += temp["idade"]
        cadastros.append(temp)
        del temp
        while(True):
            op = input("quer continuar[S/N]")
            if op in "SsNn":
                break
            else:
                print("Opção invalida, Digite novamente")
    print("=="*20)
    print(f"A quantidade de pessoas cadastradas é de {len(cadastros)}")
    print(f"A quantidade de mulheres cadastradas foi de {qtdf} ", end="")
    if qtdf != 0:
        print("e elas são ", end="")
        for i in cadastros:
            if i['sexo'] in "fF":
                print(i['nome'], end=" ")
    print(f"\nA media de idade foi {somaIdades/len(cadastros):0.2f}")
    print("As pessoas que ficaram acima da media foram: ")
    for i in cadastros:
        if somaIdades/len(cadastros) < i['idade']:
            print(f"Nome: {i['nome']}; Sexo: {i['sexo']}; Idade: {i['idade']}")

if __name__ == "__main__":
    main()