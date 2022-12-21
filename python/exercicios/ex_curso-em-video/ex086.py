#Codigo feito pelo celular com pydroid

def main():
	matriz = [ [], [], [] ]
	for i in range(0, 3):
		for j in range(0, 3):
			matriz[i].append(int(input("Digite um numero: ")))
	print()
	for i in range(0, 3):
		for j in range(0, 3):
			print(f" {matriz[i][j]}", end=" ")
		print()


if __name__ =="__main__":
	main()