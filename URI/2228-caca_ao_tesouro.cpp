#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

#define TAM_VETOR 10001

int somas[TAM_VETOR];

void zerarVetor(int n);

void printVetor(int n, vector<int> v);

int main()
{
  int x, y, n, aux, index = 0, opt1, valorAtual;
  int diff, totItens = 0;

  vector<int> itens;

  while (true)
  {
    scanf("%d %d %d", &x, &y, &n);
    if (x == 0 && y == 0 && n == 0)
      break;

    zerarVetor(TAM_VETOR);
    itens.clear();
    totItens = 0;
    index++;

    for (int i = 0; i < n; i++)
    {
      scanf("%d", &aux);
      totItens = totItens + aux;
      itens.push_back(aux);
    }

    printf("Teste %d\n", index);
    diff = abs(x - y);
    aux = abs(diff - totItens);
    opt1 = aux / 2;

    if (aux % 2 != 0 || totItens < diff)
    {
      printf("N\n\n");
      continue;
    }

    for (int i = 0; i < n; i++)
    {
      valorAtual = itens[i];
      for (int j = totItens; j >= 0; j--)
      {
        if (somas[j] == 1)
          somas[j + valorAtual] = 1;
      }

      // chega na combinação certa
      if (somas[opt1] == 1)
        break;
    }

    if (somas[opt1] == 1)
    {
      printf("S\n\n");
    }
    else
    {
      printf("N\n\n");
    }
  }

  return 0;
}

void zerarVetor(int n)
{
  somas[0] = 1;
  for (int i = 1; i < n; i++)
  {
    somas[i] = 0;
  }
}
