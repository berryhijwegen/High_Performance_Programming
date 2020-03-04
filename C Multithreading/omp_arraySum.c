/* omp_arraySum.c uses an array to sum the values (using OpenMP) in inputfiles,
 *  whose names are specified in the `fileNames` variable.
 * 	Based on arraySum.c made by Huib Aldewereld.
 * 	Berry Hijwegen, HU, HPP, 2020
 */

#include <stdio.h>      /* I/O stuff */
#include <stdlib.h>     /* calloc, etc. */
#include <omp.h>        /* OpenMP */
  
void readArray(char * fileName, double ** a, int * n);
double sumArray(double * a, int numValues);

int main(int argc, char * argv[])
{
  int howMany;
  double sum;
  double * a;
  char *fileNames[] = {"10k","100k","1m","10m"};
  
  for (size_t i = 0; i < sizeof(fileNames); i++)
  {

      readArray(fileNames[i], &a, &howMany);
      double start = omp_get_wtime();

      sum = sumArray(a, howMany);
      free(a);

      double end = omp_get_wtime();
      printf("%s Elasped time = %f sec\n", fileNames[i], end - start);

  }
 

  return 0;
}

/* readArray fills an array with values from a file.
 * Receive: fileName, a char*,
 *          a, the address of a pointer to an array,
 *          n, the address of an int.
 * PRE: fileName contains N, followed by N double values.
 * POST: a points to a dynamically allocated array
 *        containing the N values from fileName
 *        and n == N.
 */

void readArray(char * fileName, double ** a, int * n) {
  int count, howMany;
  double * tempA;
  FILE * fin;

  fin = fopen(fileName, "r");
  if (fin == NULL) {
    fprintf(stderr, "\n*** Unable to open input file '%s'\n\n",
                     fileName);
    exit(1);
  }

  fscanf(fin, "%d", &howMany);
  tempA = calloc(howMany, sizeof(double));
  if (tempA == NULL) {
    fprintf(stderr, "\n*** Unable to allocate %d-length array",
                     howMany);
    exit(1);
  }
  
  for (count = 0; count < howMany; count++)
   fscanf(fin, "%lf", &tempA[count]);

  fclose(fin);

  *n = howMany;
  *a = tempA;
}

/* sumArray sums the values in an array of doubles.
 * Receive: a, a pointer to the head of an array;
 *          numValues, the number of values in the array.
 * Return: the sum of the values in the array.
 */

double sumArray(double * a, int numValues) {
  int i;
  double result = 0.0;

  #pragma omp parallel for reduction(+:result)
  for (i = 0; i < numValues; i++) {
    result += a[i];
  }

  return result;
}
