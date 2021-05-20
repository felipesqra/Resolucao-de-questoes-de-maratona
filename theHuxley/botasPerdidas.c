//Resolução da questão Botas perdidas
#include <stdio.h>
#define tam 10000

int main () {
    int botas, numero[tam];
    char pe[tam];
    int achei, qtdPares;
    int atual, i;


    while (botas != -1){
        scanf("%d", &botas);
            for(atual = 0; atual < botas; atual++){
                scanf("%d", &numero[atual]);
                scanf(" %c", &pe[atual]);
            }
        
        for(atual = 0; atual < botas; atual++){
            achei = 0;
                
            for(i = 0; i < botas; i++){
                if((numero[atual] == numero[i]) && (pe[atual] != pe[i]) && achei == 0){
                    if ((pe[atual] == 'D' || pe[atual] == 'E') && (pe[i] == 'D' || pe[i] == 'E')){
                        qtdPares++;
                        pe[atual] = 'A';
                        pe[i] = 'B';
                        numero[atual] = -1;
                        numero[i] = -1;
                        achei = 1;
                        }
                    }
                }
        }
        if(botas != -1){
            printf("%d\n", qtdPares);  
            qtdPares = 0;
        }
             
    }
    return 0;
}