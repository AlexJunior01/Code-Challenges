#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int a, c, aux, pico_atual, fundo_atual;
  bool pico;
  int qtd_final, qtd_iteracao;
  vector<int> molde;

  scanf("%d %d", &a, &c);

  while (a != 0 && c != 0)
  {
    qtd_final = 0;
    for (int i = 0; i < c; i++)
    {
      scanf("%d", &aux);
      molde.push_back(aux);
    }

    pico = true;
    pico_atual = a;
    for (int col_atual = 0; col_atual < c; col_atual++)
    {
      if (pico == true && molde[col_atual] < pico_atual)
      {
        pico = false;
        fundo_atual = molde[col_atual];
      }
      else if (pico == true && molde[col_atual] > pico_atual)
      {
        pico_atual = molde[col_atual];
      }
      else if (pico == false && molde[col_atual] < fundo_atual)
      {
        fundo_atual = molde[col_atual];
      }
      else if (pico == false && molde[col_atual] > fundo_atual)
      {
        pico = true;
        qtd_final += pico_atual - fundo_atual;
        pico_atual = molde[col_atual];
      }

      if (pico == false && col_atual == c - 1)
      {
        qtd_final += pico_atual - fundo_atual;
      }
    }

    printf("%d\n", qtd_final);
    molde.clear();
    scanf("%d %d", &a, &c);
  }
  return 0;
}