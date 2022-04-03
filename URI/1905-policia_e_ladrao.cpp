#include <iostream>

using namespace std;

bool achou;

int andar(int matriz[5][5], int lin, int col)
{
  if (lin < 0 || lin > 4)
    return 0;
  if (col < 0 || col > 4)
    return 0;
  if (matriz[lin][col] != 0)
    return 0;
  if (achou == true)
    return 0;
  if (lin == 4 && col == 4)
  {
    achou = true;
    return 0;
  }

  matriz[lin][col] = -1;
  // cima
  andar(matriz, lin - 1, col);
  // direita
  andar(matriz, lin, col + 1);
  // baixo
  andar(matriz, lin + 1, col);
  // esquerda
  andar(matriz, lin, col - 1);

  return 0;
}

int achou_caminho(int matriz[5][5])
{
  int lin = 0, col = 0;

  andar(matriz, lin, col);

  return 0;
}

int main()
{

  int nCasos, aux;
  int matriz[5][5];

  scanf("%d", &nCasos);

  for (int i = 0; i < nCasos; i++)
  {
    // Lendo Matriz
    for (int lin = 0; lin < 5; lin++)
    {
      for (int col = 0; col < 5; col++)
      {
        scanf("%d", &aux);
        matriz[lin][col] = aux;
      }
    }

    achou = false;
    achou_caminho(matriz);

    if (achou == true)
    {
      printf("COPS\n");
    }
    else
    {
      printf("ROBBERS\n");
    }
  }

  return 0;
}