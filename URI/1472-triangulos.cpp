#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

void printVetor(int n, vector<int> v);

int main()
{
  int n, aux, triangulos, total, step;
  vector<int> p;

  while (cin >> n)
  {
    // iniciando caso
    p.clear();
    total = 0;
    triangulos = 0;
    p.push_back(0);

    for (int i = 0; i < n; i++)
    {
      scanf("%d", &aux);
      total += aux;
      if (i != n - 1)
        p.push_back(total);
    }

    step = total / 3;
    for (int i = 0; i < n; i++)
    {
      aux = p[i];
      aux = (aux + step) % total;
      if (binary_search(p.begin(), p.end(), aux))
      {
        aux = (aux + step) % total;
        if (binary_search(p.begin(), p.end(), aux))
          triangulos++;
      }
    }

    printf("%d\n", triangulos / 3);
  }

  return 0;
}