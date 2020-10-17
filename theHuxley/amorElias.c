//Resolução da questão O amor de Elias
#include<stdio.h>
#include<string.h>

#define TAM 1001
int main(){
  char matriz[TAM][TAM];
  int n, m, t, x, y, moca;
  char direcao[10];
  int i, j;

  scanf("%d %d", &n, &m);
  for(i = 0; i < n; i++){
    for(j = 0; j < m; j++){
      scanf(" %c", &matriz[i][j]);
    }
  }

  scanf("%d", &t);
  while(t > 0){
    scanf("%d %d", &x, &y);
    scanf(" %s", direcao);
    scanf("%d", &moca);

    if(strcmp(direcao, "cima") == 0 || strcmp(direcao, "baixo") == 0){
      for(i = x; i < n && i >= 0;){
        if(matriz[i][y] == '%'){
          moca -= 2;
        } else {
          moca--;
        }
        if(strcmp(direcao, "cima") == 0){
          i--;
        } else {
          i++;
        }
      }
    } else {
      for(j = y; j < m && j >= 0;){
        if(matriz[x][j] == '%'){
          moca -= 2;
        } else {
          moca--;
        }
        if(strcmp(direcao, "direita") == 0){
          j++;
        } else {
          j--;
        }
      }
    }
    if(moca <= 0){
      printf("Vou voltar pra Limoeiro...\n");
    } else {
      printf("O amor est� no ar!\n");
    }
    t--;
  }
  return 0;
}