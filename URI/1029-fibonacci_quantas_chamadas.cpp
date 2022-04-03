#include <iostream>

using namespace std;

int num_calls;

int fat(int x)
{
  num_calls += 1;
  if (x == 1)
  {
    return 1;
  }

  if (x == 0)
  {
    return 0;
  }

  int r1 = fat(x - 1);
  int r2 = fat(x - 2);

  return r1 + r2;
}

int main()
{

  int n_casos, x;
  scanf("%d", &n_casos);

  for (int i = 0; i < n_casos; i++)
  {
    scanf("%d", &x);
    num_calls = 0;
    int resultado = fat(x);

    printf("fib(%d) = %d calls = %d\n", x, num_calls - 1, resultado);
  }

  return 0;
}