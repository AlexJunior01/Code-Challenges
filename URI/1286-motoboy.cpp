#include <iostream>
#include <vector>

using namespace std;

// estado[i][w]
int estado[5000][2000];

void salva_estado(int i, int w, int aux)
{
  estado[i - 1][w - 1] = aux;
}

int pega_estado(int i, int w)
{
  if (i == 0 || w == 0)
  {
    return 0;
  }

  return estado[i - 1][w - 1];
}

int max(int x1, int x2)
{
  if (x1 > x2)
  {
    return x1;
  }

  return x2;
}

int main()
{
  int nPedidos, qtdMaxPizza;
  int tempoEntrega, qtdPizzas;

  int aux1, aux2, maiorRodada;
  vector<vector<int>> entregas;
  vector<int> entregaAux;

  scanf("%d", &nPedidos);
  scanf("%d", &qtdMaxPizza);

  while (nPedidos != 0)
  {
    for (int i = 0; i < nPedidos; i++)
    {
      vector<int> v1;
      scanf("%d", &tempoEntrega);

      scanf("%d", &qtdPizzas);
      v1.push_back(qtdPizzas);
      v1.push_back(tempoEntrega);

      entregas.push_back(v1);
    }

    for (int i = 1; i <= nPedidos; i++)
    {
      entregaAux = entregas[i - 1];
      for (int w = 1; w <= qtdMaxPizza; w++)
      {
        // se o cano atual é maior que o canoOriginal comparado
        // e nao da pra cortar ele
        if (entregaAux[0] > w)
        {
          aux1 = pega_estado(i - 1, w);
          maiorRodada = aux1;
        }
        else
        {
          aux1 = pega_estado(i - 1, w);
          aux2 = entregaAux[1] + pega_estado(i - 1, w - entregaAux[0]);
          maiorRodada = max(aux1, aux2);
        }

        salva_estado(i, w, maiorRodada);
      }
    }

    int final = pega_estado(nPedidos, qtdMaxPizza);
    printf("%d min.\n", final);

    entregas.clear();
    entregaAux.clear();
    scanf("%d", &nPedidos);
    scanf("%d", &qtdMaxPizza);
  }

  return 0;
}