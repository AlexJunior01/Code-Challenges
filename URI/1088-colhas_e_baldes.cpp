#include <iostream>
#include <vector>

using namespace std;
long long int trocas;

void mergeSort(vector<int> &v, int l, int r);
void merge(vector<int> &v, int l, int m, int r);
void printVetor(int n, vector<int> v);

int main()
{
  int n = -1, aux;
  vector<int> p;

  while (true)
  {
    scanf("%d", &n);
    if (n == 0)
      break;

    for (int i = 0; i < n; i++)
    {
      scanf("%d", &aux);
      p.push_back(aux);
    }

    trocas = 0;
    mergeSort(p, 0, n - 1);
    if (trocas % 2 == 1)
    {
      printf("Marcelo\n");
    }
    else
    {
      printf("Carlos\n");
    }

    p.clear();
  }

  return 0;
}

void merge(vector<int> &v, int l, int m, int r)
{
  int sizeLeft, sizeRight, remainsLeft;
  int idxLeft, idxRight, idxFinal;
  vector<int> leftVector, rightVector;

  sizeLeft = m - l + 1;
  sizeRight = r - m;

  for (int i = 0; i < sizeLeft; i++)
  {
    leftVector.push_back(v[l + i]);
  }

  for (int i = 0; i < sizeRight; i++)
  {
    rightVector.push_back(v[m + 1 + i]);
  }

  idxLeft = 0;
  idxRight = 0;
  idxFinal = l;
  remainsLeft = sizeLeft;

  // sorting
  while (idxLeft < sizeLeft && idxRight < sizeRight)
  {
    if (leftVector[idxLeft] <= rightVector[idxRight])
    {
      v[idxFinal] = leftVector[idxLeft];
      idxLeft++;
      remainsLeft--;
    }
    else
    {
      v[idxFinal] = rightVector[idxRight];
      trocas += remainsLeft;
      idxRight++;
    }
    idxFinal++;
  }

  while (idxLeft < sizeLeft)
  {
    v[idxFinal] = leftVector[idxLeft];
    idxLeft++;
    idxFinal++;
  }

  while (idxRight < sizeRight)
  {
    v[idxFinal] = rightVector[idxRight];
    idxRight++;
    idxFinal++;
  }
}

void mergeSort(vector<int> &v, int l, int r)
{
  if (l >= r)
  {
    return;
  }

  int m = l + (r - l) / 2;
  mergeSort(v, l, m);
  mergeSort(v, m + 1, r);
  merge(v, l, m, r);
}

void printVetor(int n, vector<int> v)
{
  for (int i = 0; i < n; i++)
  {
    printf("%d ", v[i]);
  }
  printf("\n");
}