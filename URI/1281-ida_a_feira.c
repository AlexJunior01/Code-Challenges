#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _produto
{
  char nome[50];
  float preco;
} produto;

int main()
{
  int qtdFeiras;
  produto *feira;
  int qtdProduto;

  int qtdDona;
  int qtdProdutosComprados;
  char recebeNome[50];

  float precoTotal = 0;
  int i, j, k;
  int flag;

  scanf("%d", &qtdFeiras);

  for (i = 0; i < qtdFeiras; i++)
  {
    scanf("%d", &qtdProduto);
    feira = malloc(sizeof(produto) * qtdProduto);

    for (j = 0; j < qtdProduto; j++)
    {
      scanf("%s", feira[j].nome);
      scanf("%f", &(feira[j].preco));
    }

    scanf("%d", &qtdDona);
    for (j = 0; j < qtdDona; j++)
    {
      scanf("%s", recebeNome);
      scanf("%d", &qtdProdutosComprados);
      flag = 0;
      for (k = 0; k < qtdProduto && flag == 0; k++)
      {
        if (strcmp(feira[k].nome, recebeNome) == 0)
        {
          precoTotal += feira[k].preco * qtdProdutosComprados;
          flag = 1;
        }
      }
    }
    printf("R$ %.2f\n", precoTotal);
    precoTotal = 0;
    free(feira);
  }

  return 0;
}