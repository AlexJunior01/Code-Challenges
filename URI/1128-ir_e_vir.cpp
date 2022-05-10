#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

#define MAXVERTICES 2001

void printMatriz(int n);
void dfs(int n, int maxVertices);

int matrizAdj[MAXVERTICES][MAXVERTICES];
int visited[MAXVERTICES];
int completos;
bool reachCompleted;

int main()
{
  int nVertices, nArestas, v, w, p;
  bool conectado;

  while (true)
  {
    scanf("%d %d", &nVertices, &nArestas);
    if (nVertices == 0 && nArestas == 0)
      break;

    memset(matrizAdj, 0, sizeof matrizAdj);

    for (int i = 0; i < nArestas; i++)
    {
      scanf("%d %d %d", &v, &w, &p);

      matrizAdj[v][w] = 1;
      if (p == 2)
        matrizAdj[w][v] = 1;
    }

    conectado = true;
    for (int i = 1, completos = 0; i <= nVertices; i++, completos++)
    {
      reachCompleted = false;
      memset(visited, false, sizeof visited);

      dfs(i, nVertices);
      for (int j = 1; j <= nVertices && conectado && !reachCompleted; j++)
      {
        if (visited[j] == 0)
          conectado = false;
      }

      if (!conectado)
        break;
    }

    if (conectado)
      printf("1\n");
    else
      printf("0\n");
  }

  return 0;
}

void dfs(int n, int maxVertices)
{
  visited[n] = 1;
  if (n <= completos)
  {
    reachCompleted = true;
    return;
  }

  for (int i = 1; i <= maxVertices && !reachCompleted; i++)
  {
    if (matrizAdj[n][i] == 1)
    {
      if (visited[i] == 0)
      {
        dfs(i, maxVertices);
      }
    }
  }
}