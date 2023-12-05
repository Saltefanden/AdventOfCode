#include <ctype.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void part1(char* filename);
void part2(char* filename);
int read_line(char* line, FILE* file);
int get_game_number(char* line);
void get_game(char* line, int* winnumbers, int* mynumbers);
void get_num_arr(char* line, int* arr);


int main(int argc, char *argv[]) {
  if (argc != 2){
    printf("Usage: %s <filename>\n", argv[0]);
    exit(1);
  }
  part1(argv[1]);
  part2(argv[1]);
}

void part1(char* filename) {
  FILE *file = fopen(filename, "r");
  char line[1024];
  int n_read;
  int score = 0;
  int* winnumbers = malloc(sizeof(int)*1024);
  int* mynumbers = malloc(sizeof(int)*1024);
  int found;
  int gamescore;
  while ((n_read = read_line(line, file)) != -1) {
    gamescore = 0;
    get_game(line, winnumbers, mynumbers);
    for (int i=0; mynumbers[i] != -1; ++i){
      found = 0;
      for (int j=0; winnumbers[j] != -1; ++j){
        if (mynumbers[i] == winnumbers[j]){found = 1;} 
      }
      if (found){
        gamescore = gamescore ? gamescore*2 : 1;
      }
    }
    score += gamescore;
  }
  printf("Score for part1: %d\n", score);
  free(winnumbers);
  free(mynumbers);
  fclose(file);
}

void part2(char* filename) {
  FILE *file = fopen(filename, "r");
  char line[1024];
  int n_read;
  long score = 0;
  int* winnumbers = malloc(sizeof(int)*1024);
  int* mynumbers = malloc(sizeof(int)*1024);
  long* n_cards = malloc(sizeof(long)*1024);
  for (int i=0; i<1024; ++i){ n_cards[i] = 0; }
  int gamenumber;
  int found;
  int gamescore;
  int n_games=0;
  while ((n_read = read_line(line, file)) != -1) {
    ++n_games;
    gamescore = 0;
    gamenumber = get_game_number(line); 
    if (gamenumber>1024){ printf("Ideally realloc...\n"); exit(1); }
    n_cards[gamenumber-1] += 1; // The original copy
    get_game(line, winnumbers, mynumbers);
    for (int i=0; mynumbers[i] != -1; ++i){
      found = 0;
      for (int j=0; winnumbers[j] != -1; ++j){
        if (mynumbers[i] == winnumbers[j]){found = 1;} 
      }
      if (found){
        gamescore++;
      }
    }
    for (int i=0; i<gamescore; ++i){
      n_cards[gamenumber+i] += n_cards[gamenumber-1];
    }
  }
  for (int i=0; i<n_games ; ++i) {
    score += (long) n_cards[i]; 
  }
  printf("Score for part2: %ld\n", score);
  free(winnumbers);
  free(mynumbers);
  free(n_cards);
  fclose(file);

}

int get_game_number(char* line){
  while (! isdigit(*line++));
  return atoi(line-1);
}

void get_game(char* line, int* winnumbers, int* mynumbers){
  while (*line++ != ':');
  char* winstring = strtok(line, "|");
  char *mystring = strtok(NULL, "|");
  get_num_arr(winstring, winnumbers);
  get_num_arr(mystring, mynumbers);
}

void get_num_arr(char* line, int* arr){
  int i = 0;
  char *token = strtok(line, " ");
  while (token != NULL){
    *(arr + i++) = atoi(token);
    token = strtok(NULL, " ");
  }
  *(arr + i) = -1;
}

int read_line(char *line, FILE *file) {
  char c;
  size_t tapehead = 0;
  while ((c = getc(file)) != '\n' && c != EOF) {
    line[tapehead++] = c;
  }
  line[tapehead] = '\0';
  if (c == EOF) {
    return -1;
  }
  return tapehead;
}



int str_len(char *str) {
  int i = 0;
  while (str[i] != '\0') {
    ++i;
  }
  return i;
}
