#include <iostream>
#include "stack.h"
#include <locale.h>
using namespace std;

int main() {
	setlocale(LC_ALL, "portuguese");
	stack stack1;
	Item n;
	int op;
	do {	
		cout << "\nEscolha uma opção: \n";
		cout << "1 - Adicionar item a pilha\n";
		cout << "2 - Remover item da pilha\n";
		cout << "3 - Verificar tamanho atual\n";
		cout << "4 - Verificar se está vazio\n";
		cout << "5 - Verificar se está cheio\n";
		cout << "6 - Exibir pilha\n";
		cout << "0 - Sair\n";
		cout << "resposta: ";
		cin >> op;
		switch (op) {
			case 0:
				cout << "bye bye\n\n";
				break;
			case 1:
				cout << "Numero que deseja adicionar: ";
				cin >> n;
				stack1.add(n);
				break;
			case 2:
				n = stack1.pop();
				break;
			case 3:
				cout << "\nO tamanho da pilha: " << stack1.lenght() << endl;
				break;
			case 4: 
				if (stack1.isEmpty()) {
					cout << "\nA pilha está vazia! \n";
				}
				else {
					cout << "\nExiste conteúdo na pilha\n";
				}
				break;
			case 5:
				if (stack1.isFull()) {
					cout << "\nA pilha está cheia\n";
				}
				else {
					cout << "\nAinda tem espaço na pilha\n";
				}
				break;
			case 6:
				stack1.print();
				break;
			default:
				cout << "Opcao invalida\n";
		}
	} while (op != 0);
	return 0;
}
