#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main()
{
  vector<int> cartas_dela, cartas_dele;
  vector<bool> ja_usadas;
  int aux, pontos;

  // Lendo entrada
  ja_usadas.assign(53, false);
  for (int i = 0; i < 3; i++)
  {
    scanf("%d", &aux);
    ja_usadas[aux] = true;
    cartas_dela.push_back(aux);
  }
  for (int i = 0; i < 2; i++)
  {
    scanf("%d", &aux);
    ja_usadas[aux] = true;
    cartas_dele.push_back(aux);
  }
  sort(cartas_dela.begin(), cartas_dela.end());

  while (cartas_dela[0] != 0 && cartas_dela[1] != 0 && cartas_dela[2] != 0 &&
         cartas_dele[0] != 0 && cartas_dele[1] != 0)
  {
    pontos = 0;
    if (cartas_dele[0] > cartas_dela[2])
    {
      pontos += 3;
    }
    else if (cartas_dele[0] > cartas_dela[1])
    {
      pontos += 2;
    }

    if (cartas_dele[1] > cartas_dela[2])
    {
      pontos += 3;
    }
    else if (cartas_dele[1] > cartas_dela[1])
    {
      pontos += 2;
    }

    if (pontos < 3)
    {
      printf("-1\n");
    }
    else if (pontos == 3)
    {
      aux = cartas_dela[2];
      while (ja_usadas[aux] == true)
      {
        aux += 1;
        if (aux == 52 && ja_usadas[aux] == true)
        {
          aux = -1;
          break;
        }
      }
      printf("%d\n", aux);
    }
    else if (pontos == 4 || pontos == 5)
    {
      aux = cartas_dela[1];
      while (ja_usadas[aux] == true)
      {
        aux += 1;
        if (aux == 52 && ja_usadas[aux] == true)
        {
          aux = -1;
          break;
        }
      }
      printf("%d\n", aux);
    }
    else
    {
      aux = 1;
      while (ja_usadas[aux] == true)
      {
        aux += 1;
        if (aux == 52 && ja_usadas[aux] == true)
        {
          aux = -1;
          break;
        }
      }
      printf("%d\n", aux);
    }

    ja_usadas.clear();
    cartas_dela.clear();
    cartas_dele.clear();
    // Lendo entrada
    ja_usadas.assign(52, false);
    for (int i = 0; i < 3; i++)
    {
      scanf("%d", &aux);
      ja_usadas[aux] = true;
      cartas_dela.push_back(aux);
    }
    for (int i = 0; i < 2; i++)
    {
      scanf("%d", &aux);
      ja_usadas[aux] = true;
      cartas_dele.push_back(aux);
    }
    sort(cartas_dela.begin(), cartas_dela.end());
  }

  return 0;
}