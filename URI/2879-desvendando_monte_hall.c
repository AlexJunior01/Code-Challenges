#include <stdio.h>

int main()
{
  int qtdEntradas;
  int porta;
  int contador = 0;
  int i;

  scanf("%d", &qtdEntradas);

  for (i = 0; i < qtdEntradas; i++)
  {
    scanf("%d", &porta);
    if (porta != 1)
      contador++;
  }

  printf("%d\n", contador);
  return 0;
}