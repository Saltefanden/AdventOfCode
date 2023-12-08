#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>


void part1(char* filename);
void part2(char* filename);

int main(int argc, char *argv[])
{
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);  
    exit(0);
  }  
  part1(argv[1]);
  part2(argv[1]);
}


void part1(char* filename){
  FILE *file = fopen(filename, "r");

  fclose(file);
}

void part2(char* filename){
  FILE *file = fopen(filename, "r");

  fclose(file);
}

