#include <stdio.h>

int main()
{
  int numeros[26];
  char letras = 'a';
  int i, j = 0;

  for (i = 97; i <= 122; i++, j++, letras++)
  {
    numeros[j] = i;
    printf("%d e %c\n", numeros[j], letras);
  }

  return 0;
}