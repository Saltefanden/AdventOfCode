#include <string.h>
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
/* Idea: 
 * Recursive solution. While there are still unknowns to be placed (How to
 * determine this?), iterate over possible placements of the first piece. 
 * Recurse this while there are still pieces. Return 1 if placement is possible
 * 0 otherwise. A placement must include either the start range and an ending
 * '.', the end range and a '.' or the entire range and no dot. 
 * */ 
  FILE *file = fopen(filename, "r");
  char* line = NULL;
  size_t len = 0;
  char* records;
  char* groups;
  char* renamethislol;
  while ( (getline(&line, &len, file) != -1) ){
    records = strtok(line, " ");
    groups = strtok(NULL, " ");
    renamethislol = strtok(records, ".");
    printf("Contiguous groups?: \n");
    while (renamethislol != NULL) {
      //do work 
      printf("%s\n", renamethislol);
      renamethislol = strtok(NULL, "."); 
    }
    printf("Groups: %s\n", groups);
  }

  fclose(file);
}

void part2(char* filename){
  FILE *file = fopen(filename, "r");

  fclose(file);
}

