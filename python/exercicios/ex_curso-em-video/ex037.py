n = int(input("Digite o numero: "))
op = int(input("""
Digite a opção que vc gostaria: 
[1] - binario
[2] - octal
[3] - hexadecimal
Digite aqui: """))
if op == 1:
    print("O numero {} em binario fica: {}".format(n, bin(n)[2:]))
elif op == 2:
    print("O numero {} em octal fica: {}".format(n, oct(n)[2:]))
elif op == 3:
    print("O numero {} em hexadecimal fica: {}".format(n, hex(n)[2:]))
else: 
    print("opção invalida")