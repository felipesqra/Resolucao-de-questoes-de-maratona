#include <algorithm>
#include <iostream>

using namespace std;

int main(){
    int qtd;
    int questoes[200000];
    
    cin >> qtd;
    
    int i;
    for(i = 0; i < qtd; i++){
        cin >> questoes[i];
    }

    sort(questoes, questoes + qtd);

    int soma = 0;
    int dias = 1;

    for(i = 0; i < qtd; i++){
        if(questoes[i] >= dias){
            soma ++;
            dias ++;
        }
    }

    cout << soma;

    return 0;
}