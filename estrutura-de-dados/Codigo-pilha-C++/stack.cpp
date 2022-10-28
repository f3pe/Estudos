#include <iostream>
#include "stack.h"

using namespace std;


stack::stack() {
	len = 0;
	thing = new Item[max_itens];
	}

stack::~stack() {
	delete [] thing;
	}

void stack::add(Item n) {
	if (isFull()) {
		cout << "Pilha já está cheia";
	}
	else {
		thing[len] = n;
		len++;
	}
}

Item stack::pop() {
	if (isEmpty()) {
		cout << "\nnão existe item para ser removido\n";
		return 0;
	}
	else {
		cout << "\nO ultimo item foi removido\n";
		len--;
		return thing[len];
	}
}

int stack::lenght() {
	return len;
}

bool stack::isFull() {
	return (len == max_itens);
}

bool stack::isEmpty() {
	return (len == 0);
}

void stack::print() {
	cout << "\npilha: [ ";
	for (int i = 0; i < len; i++) {
		cout << thing[i] << " ";
	}
	cout << "] \n";
}
