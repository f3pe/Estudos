#Codigo feito pelo celular com pydroid

def main():
	soma = sumTerceiraC = maior = 0
	matriz = [ [], [], [] ]
	for i in range(0, 3):
		for j in range(0, 3):
			matriz[i].append(int(input("Digite um numero: ")))
	print()
	for i in range(0, 3):
		for j in range(0, 3):
			print(f" {matriz[i][j]}", end=" ")
			if matriz[i][j] % 2 == 0:
				soma += matriz[i][j]
			if j == 2:
				sumTerceiraC += matriz[i][j]
			if i == 1 and (maior < matriz[i][j] or j ==1):
				maior = matriz[i][j]
		print()
	
	print(f"\n\n  A soma dos numeros pares: {soma}")
	print(f"  A soma dos valores sa terceira coluna: {sumTerceiraC}")
	print(f"  O maior valor da segunda linha: {maior}")
	


if __name__ =="__main__":
	main()