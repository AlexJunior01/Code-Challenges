#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main()
{
  int N, aux;
  int pos_chegada, pos_largada, ultrapassagens;
  vector<int> largada, chegada;
  vector<int>::iterator it;

  while (scanf("%d", &N) != EOF)
  {
    for (int i = 0; i < N; i++)
    {
      scanf("%d", &aux);
      largada.push_back(aux);
    }

    for (int i = 0; i < N; i++)
    {
      scanf("%d", &aux);
      chegada.push_back(aux);
    }

    ultrapassagens = 0;

    for (int i = 0; i < N; i++)
    {
      aux = 0;
      while (chegada[0] != largada[aux])
        aux++;
      ultrapassagens += aux;

      chegada.erase(chegada.begin());
      largada.erase(largada.begin() + aux);
    }

    printf("%d\n", ultrapassagens);
    largada.clear();
    chegada.clear();
  }

  return 0;
}