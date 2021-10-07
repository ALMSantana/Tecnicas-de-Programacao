

void trocarValoresv1(int v1, int v2){


}

void trocarValoresv1(int &v1, int &v2){


}


int main(){
    int valor1 = 3;
    int valor2 = 5;

    trocarValoresv1(valor1, valor2);
    trocarValoresV2(valor1, valor2);
    return 0;
}