#include <stddef.h>
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int cmpint(const void*, const void*);
void part1(char*);
void part2(char*);

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);
    exit(0);
  }
  part1(argv[1]);
  part2(argv[1]);
}

void part1(char *filename){
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  size_t nread = 0;
  int item_val;
  int curr_elf = 0;
  int max_elf=0;
  while ((nread = getline(&line, &len, file)) != EOF) {
    if ((item_val = atoi(line)) != 0) {
      curr_elf += item_val;
    } else {
      max_elf = curr_elf>max_elf ? curr_elf : max_elf;
      curr_elf = 0;
    }
  }
  printf("Part 1: %d\n", max_elf);
  fclose(file);
}

void part2(char *filename){
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  size_t nread = 0;
  int item_val;
  int curr_elf = 0;
  int arr[10000];
  size_t arrptr = 0;
  while ((nread = getline(&line, &len, file)) != EOF) {
    if ((item_val = atoi(line)) != 0) {
      curr_elf += item_val;
    } else {
      arr[arrptr++] = curr_elf;
      curr_elf = 0;
    }
  }
  qsort(arr, arrptr, sizeof(arr[0]), cmpint);
  printf("Part 2: %d\n",
         arr[arrptr - 3] + arr[arrptr - 2] + arr[arrptr - 1]);
  fclose(file);
}

int cmpint(const void *A, const void *B) {
  int *a = (int *)A;
  int *b = (int *)B;
  return *a > *b;
}
