#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int get_index(char c);
void part1(char *filename);
void part2(char *filename);

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);
    exit(1);
  }
  part1(argv[1]);
  part2(argv[1]);
}

void part1(char *filename) {
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  ssize_t nread;
  int score = 0;
  char c;
  int idx;
  int found[52] = {0};
  while ((nread = getline(&line, &len, file)) != -1) {
    for (int i = 0; i < nread / 2; ++i) {
      for (int j = nread / 2; j < nread; ++j) {
        if ((c = line[i]) == line[j]) {
          idx = get_index(c);
          found[idx] = 1;
        }
      }
    }
    for (int i = 0; i < 52; ++i) {
      score += (i + 1) * found[i];
      found[i] = 0;
    }
  }
  printf("Part 1: %d\n", score);
  free(line);
  fclose(file);
}

void part2(char *filename) {
  FILE *file = fopen(filename, "r");
  char *line[3] = {NULL};
  size_t len[3] = {0};
  ssize_t nread;
  int score = 0;
  char c;
  int idx;
  int found[52] = {0};
  int count = 0;
  while (getline(&(line[0]), &len[0], file) != -1) {
    len[0] = 0;
    if (getline(&(line[1]), &len[1], file)) {
      len[1] = 0;
      if (getline(&(line[2]), &len[2], file)) {
        len[2] = 0;
        while ((c = *(line[0])++) && c != '\n') {
          idx = get_index(c);
          found[idx] = 1;
        }
        while ((c = *(line[1])++) && c != '\n') {
          idx = get_index(c);
          if (found[idx] == 1) {
            found[idx] = 2;
          }
        }
        while ((c = *(line[2])++) && c != '\n') {
          idx = get_index(c);
          if (found[idx] == 2) {
            found[idx] = 3;
          }
        }
      }
    }
    for (int i = 0; i < 52; ++i) {
      score += (i + 1) * (int)(found[i] / 3);
      found[i] = 0;
    }
  }
  printf("Part 2: %d\n", score);
  fclose(file);
}


int get_index(char c){
  if ('A' <= c && c <= 'Z') {
    return c - 'A' + 26;
  } else if ('a' <= c && c <= 'z') {
    return c - 'a';
  }
  return -1;
}
