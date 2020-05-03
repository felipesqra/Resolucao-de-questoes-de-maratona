#include <iostream>

using namespace std;
int cartas;
int linha[1000];
int certo;
int cont;
int cont2;


int main(){

    certo = 0;
    cont = 0;
    cont2 = 0;
    cin >> cartas;
    
    for(int i = 0; i < cartas; i++){
        cin >> linha[i];
    }

    for(int i = 0; i < cartas; i++){
        if(linha[i] == 1){
            certo += 1;
        }
    }

    cont2 = 0;

    for(int i = 0; i < cartas; i++){
        if(linha[i] == 1){
            cont += 1;
            cont2 += 1;
            if(i < cartas -1){
                if(linha[i+1] == 0 and cont2 < certo){
                    cont += 1;
                }
            }
        }
    }

cout << cont;
}



