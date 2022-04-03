#include <iostream>
#include <vector>

using namespace std;
int main()
{
  int g, p, aux;
  int s, colocacao_max;
  vector<int> pontuacao, sistema;
  vector<vector<int>> colocacoes;

  scanf("%d %d", &g, &p);

  while (g != 0 && p != 0)
  {
    pontuacao.assign(0, p);

    for (int i = 0; i < g; i++)
    {
      vector<int> v1;
      for (int j = 0; j < p; j++)
      {
        scanf("%d", &aux);
        v1.push_back(aux);
      }
      colocacoes.push_back(v1);
    }

    scanf("%d", &s);

    for (int i = 0; i < s; i++)
    {
      // Lendo o sistema
      sistema.clear();
      scanf("%d", &colocacao_max);
      for (int j = 0; j < colocacao_max; j++)
      {
        scanf("%d", &aux);
        sistema.push_back(aux);
      }

      // Calculando pontuação
      int max_pontos = 0;
      vector<int> ganhadores;

      for (int piloto = 0; piloto < p; piloto++)
      {
        int posicao, pontos;
        pontos = 0;
        for (int corrida = 0; corrida < g; corrida++)
        {
          posicao = colocacoes[corrida][piloto];

          if (posicao <= colocacao_max)
          {
            pontos += sistema[posicao - 1];
          }
        }

        if (pontos > max_pontos)
        {
          max_pontos = pontos;
          ganhadores.clear();
          ganhadores.push_back(piloto);
        }
        else if (pontos == max_pontos)
        {
          ganhadores.push_back(piloto);
        }
      }

      // Printando ganhadores
      for (auto i = ganhadores.begin(); i != ganhadores.end(); ++i)
      {
        if (i + 1 == ganhadores.end())
        {
          printf("%d", *(i) + 1);
        }
        else
        {
          printf("%d ", *(i) + 1);
        }
      }
      printf("\n");
    }

    pontuacao.clear();
    sistema.clear();
    colocacoes.clear();
    scanf("%d %d", &g, &p);
  }
  return 0;
}