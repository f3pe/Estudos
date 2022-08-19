def main():
    man = menorF20 = maior_18 = 0
    op = 'S'
    while op not in 'nN':
        print("-" * 40)
        print("Cadastre uma pessoa")
        print("-" * 40)
        idade = int(input("Idade: "))
        while True:
            sex = input("sexo [F/M]: ").upper().strip()[0]
            if sex in 'FM':break 
            print("opção invalida \n")
        if idade > 18: maior_18 += 1
        if sex == 'M': man += 1
        if sex == 'F' and idade < 20: menorF20
        op = input("Gostaria de continuar? [S/N]: ")
    print(f"\nForam registrados {maior_18} pessoas com mais de 18 anos")
    print(f"Foram registrados {man} homens")
    print(f"E foram registrados {menorF20} mulheres com menos de 20 anos \n")

if __name__ == "__main__":
    main()