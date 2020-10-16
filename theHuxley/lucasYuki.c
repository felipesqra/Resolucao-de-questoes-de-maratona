#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define X 100

int resolveCima(int x, int y, char str[][X], int n, int m, char amigos[][X], int tamA){
    int i, j, k, z, h;
    int qtdAmigo;
    int saida = 0;

    for(i = 0; i < tamA; i++){
        qtdAmigo = strlen(amigos[i]); 

        if(x - qtdAmigo >= -1){ 
            for(k = 0; k < qtdAmigo && str[x - k][y] == amigos[i][k]; k++);
            
            if(k == qtdAmigo){
                saida++;
            }
        }
    }  

    return saida;
}

int resolveBaixo(int x, int y, char str[][X], int n, int m, char amigos[][X], int tamA){
    int i, j, k, z, h;
    int qtdAmigo;
    int saida = 0;

    for(i = 0; i < tamA; i++){ 
        qtdAmigo = strlen(amigos[i]); 

        if(x + qtdAmigo <= n){ 
            for(k = 0; k < qtdAmigo && str[x + k][y] == amigos[i][k]; k++);
            
            if(k == qtdAmigo){
                saida++;
            }
        }
    }  

    return saida;
}

int resolveDireita(int x, int y, char str[][X], int n, int m, char dogs[][X], int tamA){
    int i, j, k;
    int qtdAmigo;
    int saida = 0;

    for(i = 0; i < tamA; i++){ 
        qtdAmigo = strlen(dogs[i]);
        if(y + qtdAmigo <= m){ 
            for(k = 0; k < qtdAmigo && str[x][y + k] == dogs[i][k]; k++);
            
            if(k == qtdAmigo){
                saida++;
            }
        }
    }  

    return saida;
}

int resolveEsquerda(int x, int y, char str[][X], int n, int m, char amigos[][X], int tamA){
    int i, j, k, z, h;
    int qtdAmigo;
    int saida = 0;

    for(i = 0; i < tamA; i++){
        qtdAmigo = strlen(amigos[i]);

        if(y - qtdAmigo >= -1){ 
            for(k = 0; k < qtdAmigo && str[x][y - k] == amigos[i][k]; k++); 
            
            if(k == qtdAmigo){
                saida++;
            }
        }
    }  

    return saida;
}

int main () {
    char caca[X][X], dogs[X][X];
    int linhas, colunas;
    int qCP, qO, qA;
    int i, j, nomes, fim = 0;

    scanf("%d %d %d %d %d", &qCP, &qO, &qA, &linhas, &colunas);
    strcpy(dogs[0], "yuki");

    for(i = 1; i <= qA; i++){
        scanf(" %s", dogs[i]);
        for(j = 0; dogs[i][j] != '\0'; j++){
            dogs[i][j] = tolower(dogs[i][j]);
        }
    }
    qA++;
    
    while(qCP--){
        for(i = 0; i < linhas; i++){
            scanf(" %s", caca[i]);
            for(j = 0; j < colunas; j++){
                caca[i][j] = tolower(caca[i][j]);
            }
        }

        nomes = 0;
        for(i = 0; i < linhas; i++){
            for(j = 0; j < colunas; j++){
                nomes += resolveCima(i, j, caca, linhas, colunas, dogs, qA);
                nomes += resolveBaixo(i, j, caca, linhas, colunas, dogs, qA);
                nomes += resolveDireita(i, j, caca, linhas, colunas, dogs, qA);
                nomes += resolveEsquerda(i, j, caca, linhas, colunas, dogs, qA);  
            }
        }

        if(nomes <= qO){
          fim++;
        }
    }

    printf("%d\n", fim);

    return 0;
}