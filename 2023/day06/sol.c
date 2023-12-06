#include <ctype.h>
#include <math.h>
#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void part1(char *filename);
void part2(char *filename);

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);
    exit(0);
  }
  part1(argv[1]);
  part2(argv[1]);
}

void part1(char *filename) {
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  int score = 1;
  ssize_t nread;
  double times[100];
  double dists[100];
  size_t nraces = 0;
  getline(&line, &len, file);
  while (*line++ != ':')
    ;
  char *token = strtok(line, " ");
  while (token != NULL) {
    times[nraces++] = atof(token);
    token = strtok(NULL, " ");
  }
  getline(&line, &len, file);
  while (*line++ != ':')
    ;
  token = strtok(line, " ");
  for (int i = 0; i < nraces; ++i) {
    dists[i] = atof(token);
    token = strtok(NULL, " ");
  }

  for (int i = 0; i < nraces; ++i) {
    double upperlimit = (times[i] + sqrt(pow(times[i], 2.) - 4 * dists[i]) ) / 2;
    double lowerlimit = (times[i] - sqrt(pow(times[i], 2.) - 4 * dists[i]) ) / 2+1; // +1 due to rounding up
    if ( (int) upperlimit == upperlimit/1 ){ // You need to beat it exactly
      upperlimit -= 1.;
    }
    score *= (int)(upperlimit) - (int)(lowerlimit) + 1;
  }
  printf("Part 1: %d\n", score); 

  fclose(file);
}

void part2(char *filename) {
  FILE *file = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  int score = 1;
  ssize_t nread;
  double times=0;
  double dists=0;
  size_t nraces = 0;
  getline(&line, &len, file);
  while (*line++ != ':')
    ;
  while(*line++){
    if (isdigit(*line)){
      times = 10*times + *line-'0';
    }
  }
  getline(&line, &len, file);
  while (*line++ != ':')
    ;
  while(*line++){
    if (isdigit(*line)){
      dists = 10*dists + *line-'0';
    }
  }

  double upperlimit = (times + sqrt(pow(times, 2.) - 4 * dists) ) / 2;
  double lowerlimit = (times - sqrt(pow(times, 2.) - 4 * dists) ) / 2+1; // +1 due to rounding up
  if ( (int) upperlimit == upperlimit/1 ){ // You need to beat it exactly
    upperlimit -= 1.;
  }
  score *= (int)(upperlimit) - (int)(lowerlimit) + 1;
  printf("Part 2: %d\n", score); 

  fclose(file);
}
