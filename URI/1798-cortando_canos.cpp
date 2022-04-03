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
  int nCanos, canoOriginal;
  int comprimento, valor;
  int aux1, aux2, maiorRodada;
  vector<vector<int>> canos;
  vector<int> canoAux;

  scanf("%d %d", &nCanos, &canoOriginal);

  for (int i = 0; i < nCanos; i++)
  {
    vector<int> v1;
    scanf("%d", &comprimento);
    v1.push_back(comprimento);

    scanf("%d", &valor);
    v1.push_back(valor);

    canos.push_back(v1);
  }

  for (int i = 1; i <= nCanos; i++)
  {
    canoAux = canos[i - 1];
    for (int w = 1; w <= canoOriginal; w++)
    {
      // se o cano atual é maior que o canoOriginal comparado
      // e nao da pra cortar ele
      if (canoAux[0] > w)
      {
        aux1 = pega_estado(i - 1, w);
        maiorRodada = aux1;
      }
      else
      {
        aux1 = pega_estado(i - 1, w);
        aux2 = canoAux[1] + pega_estado(i, w - canoAux[0]);
        maiorRodada = max(aux1, aux2);
      }

      salva_estado(i, w, maiorRodada);
    }
  }

  int final = pega_estado(nCanos, canoOriginal);
  printf("%d\n", final);
  return 0;
}