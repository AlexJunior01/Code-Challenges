#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

// Variables
typedef pair<int, int> iPair;
#define MAXVERTICES 200001
int menoresDistancias[MAXVERTICES];
bool setMST[MAXVERTICES];

// Functions Definitions
void addEdge(vector<iPair> adj[], int u, int v, int w);
void clearGraph(vector<iPair> adj[], int n);

int prim(vector<iPair> adj[], int nVertices);

int main()
{
  vector<iPair> adjList[MAXVERTICES];
  int nVertices, nArestas, v1, v2, w;
  int total, mstCost;

  while (true)
  {
    scanf("%d %d", &nVertices, &nArestas);

    if (nVertices == 0 && nArestas == 0)
      break;

    total = 0;
    for (int i = 0; i < nArestas; i++)
    {
      scanf("%d %d %d", &v1, &v2, &w);
      addEdge(adjList, v1, v2, w);
      total += w;
    }

    mstCost = prim(adjList, nVertices);
    printf("%d\n", total - mstCost);

    clearGraph(adjList, nVertices);
  }

  return 0;
}

void addEdge(vector<iPair> adj[], int u, int v, int w)
{
  adj[u].push_back(make_pair(v, w));
  adj[v].push_back(make_pair(u, w));
}

int prim(vector<iPair> adj[], int nVertices)
{
  // <distancia, idx>
  priority_queue<iPair, vector<iPair>, greater<iPair>> pq;
  int u, soma = 0, v, w;

  // talvez declarar os dois vetores aqui na função
  for (int i = 0; i < nVertices; i++)
  {
    setMST[i] = false;
    menoresDistancias[i] = INT_MAX;
  }

  menoresDistancias[0] = 0;
  pq.push(make_pair(0, 0));

  while (!pq.empty())
  {
    u = pq.top().second;
    pq.pop();

    if (!setMST[u])
    {
      setMST[u] = true;

      // atualizando distancias
      for (iPair x : adj[u])
      {
        v = x.first;  // Vertice
        w = x.second; // Distancia
        if (w < menoresDistancias[v] && !setMST[v])
        {
          menoresDistancias[v] = w;
          pq.push(make_pair(w, v));
        }
      }
    }
  }

  for (int i = 0; i < nVertices; i++)
  {
    soma += menoresDistancias[i];
  }

  return soma;
}

void clearGraph(vector<iPair> adj[], int n)
{
  for (int i = 0; i < n; i++)
  {
    adj[i].clear();
  }
}