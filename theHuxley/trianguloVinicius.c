//Resolução da questão Triângulo do Vinicius
#include <stdio.h>

int main () {
    char letra;
    int linhas, colunas, atual;
    int i, p, j;

    scanf(" %c", &letra);
    linhas = letra - 'A' + 1;
    colunas = (2 * linhas) - 1;

    for (i = 1; i <= linhas; i++){
        for (p = 1; p <= (colunas - (2 * i - 1)) / 2; p++){
            printf(".");
        }

        for(j = 0; j < (2 * i) - 1; j++){
            if(j < i){
                atual = 'A' + j;
                printf("%c", 'A' + j);
                atual--;
            } else {
                printf("%c", atual--);
            }
        }

        for (p = 1; p <= (colunas - (2 * i - 1)) / 2; p++){
            printf(".");
        }

        printf("\n");
    }

    return 0; 
}