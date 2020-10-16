//Resolução da questão O campeonato de Kinho
#include <stdio.h>
#include <string.h>

#define T 10000

int main () {
    char str[T], str2[T];
    char aux[T];
    int num, n;
    int i, x, qtd = 0;;


    scanf("%d %s", &num, str);
    scanf("%d", &n);

    x = num;
    while(x > 0){
        x /= 10;
        qtd++;
    }
    
    x = num;
    for(i = qtd - 1; i >= 0; i--){
        aux[x % 10] = str[i];
        x /= 10;
    }


    while(n-- > 0){
        scanf(" %s", str2);

        for(i = 0; i < strlen(str2); i++){
            if('0' <= str2[i] && str2[i] <= '9'){
                str2[i] = aux[str2[i] - '0'];
            }
        }

        printf("%s\n", str2);
    }
    return 0;
}