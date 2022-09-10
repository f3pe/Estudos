#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

int main()
{
    int x, y, resultado;
    char op;

    setlocale(LC_ALL, "Portuguese");

    while(1){
        //zerando variaveis
        x = y = resultado, resultadof = 0;

        //menu
        printf("1) Soma\n");
        printf("2) Subtrair\n");
        printf("3) Multiplicar\n");
        printf("4) Dividir(retorna parte inteira)\n");
        printf("0) Sair\n");
        printf("Escolha a operação: ");
        op = getche();
        printf("\n\n");
        if (op == '0'){
            break;
        }

        //coletando os operandos
        printf("Digite os números para executar a operação: ");
        scanf("%i %i", &x, &y);

        //efetuando o calcúlo
        switch(op){
        case '1':
            resultado = x + y;
            break;
        case '2':
            resultado = x - y;
            break;
        case '3':
            resultado = x * y;
            break;
        case '4':
            resultado = x / y;
        }

        //saida
        printf("O resultado é: %i\n", resultado);
    }
}
