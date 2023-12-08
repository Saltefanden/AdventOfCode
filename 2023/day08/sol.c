#include <ctype.h>
#include <stddef.h>
#include <string.h>
#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

typedef struct MAP {
  char* name;
  struct MAP* l;
  struct MAP* r; 
} map;

// Tree Breadth first search
void parse_file(FILE *file, char **instructions, size_t *n_instr, map **maps, size_t *n_maps);
void print_map(map *maps, size_t n_maps);

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
  size_t n_instr = 512;
  size_t n_maps = 1024;
  char* instructions = malloc(sizeof(char) * n_instr); 
  instructions[0] = '\0';
  map* maps = malloc(sizeof(map) * n_maps); 
  parse_file(file, &instructions, &n_instr, &maps, &n_maps);
  printf("%s\n", instructions);
  free(instructions);
  print_map(maps, n_maps);
  for (int i=0; i <n_maps; ++i) {
    free(maps[i].name); 
  }
  free(maps);
  fclose(file);
}

void part2(char* filename){
  FILE *file = fopen(filename, "r");

  fclose(file);
}

void parse_file(FILE *file, char **instructions, size_t *n_instr, map **maps, size_t *n_maps){
  char c;
  size_t i = 0;
  while ( (c = getc(file)) != '\n' ){
    (*instructions)[i++] = c; 
    if (i >= *n_instr){
      *n_instr *= 2;
      *instructions = realloc(*instructions, sizeof(char) * *n_instr);
      if (!*instructions){
        printf("Realloc failed, exiting\n");
        exit(1);
      }
    }
  }
  (*instructions)[i] = '\0'; 

  while ( (c = getc(file)) == '\n' );
  ungetc(c, file);

  char **ls = malloc(sizeof(char*) * *n_maps);
  char **rs = malloc(sizeof(char*) * *n_maps);
  size_t maxlinesize = 100;
  char *map_name = malloc(sizeof(char)* maxlinesize); 
  char *lstr = malloc(sizeof(char)* maxlinesize); 
  char *rstr = malloc(sizeof(char)* maxlinesize); 
  i=0;
  size_t map_no = 0;
  int read;
  char** parsing = &map_name;
  int to_parse = 0;
  int change_parsing = 1;
  while (( c = getc(file)) != EOF) {
    if ( isalpha(c) ) {
      (*parsing)[i++] = c;
      change_parsing = 1;
    } else if (change_parsing) {
      (*parsing)[i] = '\0';
      i = 0;
      to_parse++;
      to_parse%=3;
      switch (to_parse) {
        case 0: // Happens on every new line
          if (map_no>=*n_maps){
            *n_maps *= 2;
            *maps = realloc(*maps, sizeof(map) * *n_maps);
            ls = realloc(ls, sizeof(char*) * *n_maps);
            rs = realloc(rs, sizeof(char*) * *n_maps);
            if (!*maps || !rs || !ls){
              printf("Realloc failed, exiting\n");
              exit(1);
            }
          }
          (*maps)[map_no].name = map_name;
          ls[map_no] = lstr;
          rs[map_no] = rstr;
          map_name = malloc(sizeof(char)* maxlinesize); 
          lstr = malloc(sizeof(char)* maxlinesize); 
          rstr = malloc(sizeof(char)* maxlinesize); 
          map_no++;
          parsing = &map_name;
          break;
        case 1:
          parsing = &lstr;
          break;
        case 2:
          parsing = &rstr;
          break;
        default:
          printf("PAnic in parsing, exit!\n");
          exit(1);
      } 
    change_parsing = 0;
    }
  }
  free(map_name);
  free(lstr);
  free(rstr);

  for (int i=0; i<map_no; ++i){
    for (int j=0; j<map_no; ++j){
      // Get the reference to the map with a name matching the left/right name expected
      if (strncmp(ls[i], (*maps)[j].name, maxlinesize) == 0){
        (*maps)[i].l = &(*maps)[j];
      }
      if (strncmp(rs[i], (*maps)[j].name, maxlinesize) == 0){
        (*maps)[i].r = &(*maps)[j];
      }
    }
    free(ls[i]);
    free(rs[i]);
  }
  free(ls);
  free(rs);
  *n_maps = map_no;
}

void print_map(map *maps, size_t n_maps){
  for (int i=0; i <n_maps; ++i){
    printf("%s = (%s, %s)\n", maps[i].name, maps[i].l->name, maps[i].r->name);
  }
}
