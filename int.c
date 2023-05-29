#include <stdio.h>
#include <stdlib.h>

int main() {
  int op, i;
  FILE *fp;
  fp = fopen("in.dat", "w");

  for (int j = 0; j < 8; j++) {
    op = j * 8;
    fprintf(fp, "%d ", op);
    for (i = 0; i < 8; i++) {
      fprintf(fp, "%d ", op + i);
    }
    fprintf(fp, "\n");
  }
  
  fclose(fp
