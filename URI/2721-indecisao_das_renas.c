#include <stdio.h>
enum renas
{
  Rudolph,
  Dasher,
  Dancer,
  Prancer,
  Vixen,
  Comet,
  Cupid,
  Donner,
  Blitzen
};

int main()
{
  int qtdBolas;
  int i;
  int totalBolas = 0;

  for (i = 0; i < 9; i++)
  {
    scanf("%d", &qtdBolas);
    totalBolas += qtdBolas;
  }

  totalBolas = totalBolas % 9;
  switch (totalBolas)
  {
  case Dasher:
    printf("Dasher\n");
    break;

  case Dancer:
    printf("Dancer\n");
    break;

  case Prancer:
    printf("Prancer\n");
    break;

  case Vixen:
    printf("Vixen\n");
    break;

  case Comet:
    printf("Comet\n");
    break;

  case Cupid:
    printf("Cupid\n");
    break;

  case Donner:
    printf("Donner\n");
    break;

  case Blitzen:
    printf("Blitzen\n");
    break;

  case Rudolph:
    printf("Rudolph\n");
    break;

  default:
    break;
  }
  return 0;
}