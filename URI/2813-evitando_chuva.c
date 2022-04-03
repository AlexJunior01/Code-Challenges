#include <stdio.h>
#include <string.h>

int main()
{
  int qtdCasa = 0, qtdEmprego = 0;
  int qtdFinalCasa = 0, qtdFinalEmprego = 0;
  char casaToEmprego[10], empregoToCasa[10];
  int dias, i;

  scanf("%d", &dias);

  for (i = 0; i < dias; i++)
  {
    scanf("%s", casaToEmprego);

    if (strlen(casaToEmprego) == 5)
    {
      if (qtdCasa == 0)
      {
        qtdFinalCasa++;
        qtdEmprego++;
      }
      else
      {
        qtdCasa--;
        qtdEmprego++;
      }
    }

    scanf("%s", empregoToCasa);

    if (strlen(empregoToCasa) == 5)
    {
      if (qtdEmprego == 0)
      {
        qtdFinalEmprego++;
        qtdCasa++;
      }
      else
      {
        qtdEmprego--;
        qtdCasa++;
      }
    }
  }

  printf("%d %d\n", qtdFinalCasa, qtdFinalEmprego);
  return 0;
}