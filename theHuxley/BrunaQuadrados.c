//Resolução da questão Bruna e os Quadrados
#include <stdio.h>

#define TAM 101

int main(){
  int matriz[TAM][TAM];
  int n, qtd, maiorArea = 0;
  int i, j, k, m;

  scanf("%d", &n);

  for(i = 0; i < n; i++){
    for(j = 0; j < n; j++){
      scanf("%d", &matriz[i][j]);
    }
  }

  for(i = 0; i < n; i++){
    for(j = 0; j < n; j++){
      if(matriz[i][j] == 1){
        qtd = 0;
        for(k = j; k < n; k++){
          if(matriz[i][k] == 0){
            k = n;
          } else {
            qtd++;
          }
        }
        for(k = i; k < i + qtd; k++){
          for(m = j; m < j + qtd; m++){
            if(matriz[k][m] != 1){
              k = i - 1;
              m = j + qtd;
              qtd--;
            } 
          }
        }
        if((qtd * qtd) > maiorArea){
          maiorArea = qtd * qtd;
        }
      }
    }
  }
  printf("%d\n", maiorArea);
  return 0;
}