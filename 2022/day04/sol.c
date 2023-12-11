#include <stddef.h>
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
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  int ranges[4];
  size_t score = 0;
  while ( getline(&line, &len, file) != -1) {
    char* firstrange = strtok(line, ",");
    char* secondrange = strtok(NULL, ",");
    ranges[0] = atoi(strtok(firstrange, "-"));
    ranges[1] = atoi(strtok(NULL, "-"));
    ranges[2] = atoi(strtok(secondrange, "-"));
    ranges[3] = atoi(strtok(NULL, "-"));
    if (ranges[0] >= ranges[2] && ranges[1] <= ranges[3]) {
      ++score; 
    } else if (ranges[0] <= ranges[2] && ranges[1] >= ranges[3]) {
      ++score;
    }
  }
  printf("Part 1: %zu\n", score);
  fclose(file);
}

void part2(char* filename){
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  int ranges[4];
  size_t score = 0;
  while ( getline(&line, &len, file) != -1) {
    char* firstrange = strtok(line, ",");
    char* secondrange = strtok(NULL, ",");
    ranges[0] = atoi(strtok(firstrange, "-"));
    ranges[1] = atoi(strtok(NULL, "-"));
    ranges[2] = atoi(strtok(secondrange, "-"));
    ranges[3] = atoi(strtok(NULL, "-"));
    if ( ((ranges[0] <= ranges[3]) && (ranges[0] >=ranges[2])) || ((ranges[2] >= ranges[0])&& (ranges[2] <= ranges[1]))){
      ++score;
    }
  }
  printf("Part 2: %zu\n", score);
  fclose(file);
}

