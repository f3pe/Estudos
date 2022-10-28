/*
	A pilha deve:
		1 - adicionar novos elementos
		2 - Remover elementos
		3 - Verificar seu tamanho
		4 - verificar se está cheia 
		5 - Verificar se está vazia
		6 - Imprimir
*/
typedef int Item;
const int max_itens = 100;

class stack {
private:
	int len;
	Item* thing;

public:
	stack();
	
	~stack();

	void add(Item n);

	Item pop();

	int lenght();

	bool isFull();

	bool isEmpty();

	void print();
};;
