#include <iostream>
#include <vector>

using namespace std;

int estado[50][1000];

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
  int comprimentoCartao, nFrases, indexTeste;
  int aux, compAtual, qtdDesculpasAtual, opc1, opc2, maiorRodada;
  vector<vector<int>> frases;
  vector<int> fraseAtual;

  // Resolução de um caso
  scanf("%d %d", &comprimentoCartao, &nFrases);
  indexTeste = 1;
  while (comprimentoCartao != 0 && nFrases != 0)
  {
    for (int i = 0; i < nFrases; i++)
    {
      vector<int> v1;
      scanf("%d", &compAtual);
      v1.push_back(compAtual);

      scanf("%d", &qtdDesculpasAtual);
      v1.push_back(qtdDesculpasAtual);

      frases.push_back(v1);
    }

    for (int i = 1; i <= nFrases; i++)
    {
      fraseAtual = frases[i - 1];
      for (int w = 1; w <= comprimentoCartao; w++)
      {
        // se o cano atual é maior que o canoOriginal comparado
        // e nao da pra cortar ele
        if (fraseAtual[0] > w)
        {
          opc1 = pega_estado(i - 1, w);
          maiorRodada = opc1;
        }
        else
        {
          opc1 = pega_estado(i - 1, w);
          opc2 = fraseAtual[1] + pega_estado(i - 1, w - fraseAtual[0]);
          maiorRodada = max(opc1, opc2);
        }
        salva_estado(i, w, maiorRodada);
      }
    }

    // Printando resposta
    int final = pega_estado(nFrases, comprimentoCartao);
    printf("Teste %d\n%d\n\n", indexTeste, final);

    indexTeste++;
    frases.clear();
    fraseAtual.clear();
    scanf("%d %d", &comprimentoCartao, &nFrases);
  }
  return 0;
}