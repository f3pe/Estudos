soma = 0
op = 's'
cont = 0
maior = menor = 0
while op not in 'Nn':
    n = int(input("digite um numero: "))
    soma += n
    if cont == 0:
        maior = n
        menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    cont += 1
    op = input("Deseja continuar [S/N]: ")
print("Foram digitados {} numeros e a media deles é {:.2f}".format(cont, soma/cont)) 
print("O maio numero foi {} e o menor numero foi {}".format(maior, menor))