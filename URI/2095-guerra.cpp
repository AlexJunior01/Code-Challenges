#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main()
{
  int S, aux, sQua, sNo, numeroVitoria = 0;
  vector<int> soldadosQua, soldadosNo;

  scanf("%d", &S);

  for (int i = 0; i < S; i++)
  {
    scanf("%d", &aux);
    soldadosQua.push_back(aux);
  }
  for (int i = 0; i < S; i++)
  {
    scanf("%d", &aux);
    soldadosNo.push_back(aux);
  }

  sort(soldadosNo.begin(), soldadosNo.end(), greater<int>());
  sort(soldadosQua.begin(), soldadosQua.end(), greater<int>());

  sQua = 0;
  sNo = 0;

  while (true)
  {
    if (soldadosNo[sNo] > soldadosQua[sQua])
    {
      numeroVitoria++;
      sQua++;
      sNo++;
    }
    else
    {
      sQua++;
    }

    if (sQua == S)
      break;
  }

  printf("%d\n", numeroVitoria);

  return 0;
}