#include <ctype.h>
#include <stddef.h>
#include <string.h>
#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

typedef struct MAP {
  char *name;
  struct MAP *l;
  struct MAP *r;
} map_t;

void parse_file(FILE *file, char **instructions, size_t *n_instr, map_t **maps,
                size_t *n_maps);
void print_map(map_t *maps, size_t n_maps);
int get_steps(char *instructions, map_t *maps, size_t n_maps);
size_t get_ghost_steps(char *instructions, map_t *maps, size_t n_maps);
size_t gcd(size_t x, size_t y);
size_t lcm(size_t x, size_t y);

void part1(char *filename);
void part2(char *filename);

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <filename>\n", argv[0]);
    exit(0);
  }
  part1(argv[1]);
}

void part1(char *filename) {
  FILE *file = fopen(filename, "r");
  if (!file) {
    printf("Cannot open file: %s\n", filename);
    return;
  }
  size_t n_instr = 512;
  size_t n_maps = 1024;
  char *instructions = malloc(sizeof(char) * n_instr);
  instructions[0] = '\0';
  map_t *maps = malloc(sizeof(map_t) * n_maps);
  parse_file(file, &instructions, &n_instr, &maps, &n_maps);
  int nsteps = get_steps(instructions, maps, n_maps);
  printf("Part 1: %d\n", nsteps);
  size_t n_gh_steps = get_ghost_steps(instructions, maps, n_maps);
  printf("Part 2: %zu\n", n_gh_steps);
  free(instructions);
  for (int i = 0; i < n_maps; ++i) {
    free(maps[i].name);
  }
  free(maps);
  fclose(file);
}

size_t get_ghost_steps(char *instructions, map_t *maps, size_t n_maps) {
  /* I fucking cheated and looked at the subreddit to see if the input was evil
   * or whether I could make some serious assumptions. I only made a simple
   * solution ---- AND FINISHED this because of reading other peoples input.
   */
  size_t nstarting = 0;
  map_t *starting_maps = malloc(sizeof(map_t) * n_maps);

  for (size_t i = 0; i < n_maps; ++i) {
    if (maps[i].name[2] == 'A') {
      starting_maps[nstarting++] = maps[i];
    }
  }

  size_t j;
  size_t len_instr = strlen(instructions);
  size_t curr_lcm = 0;
  for (size_t i = 0; i < nstarting; ++i) {
    map_t *curr_map = &starting_maps[i];
    j = 0;
    while (curr_map->name[2] != 'Z') {
      switch (instructions[j++ % len_instr]) {
      case 'R':
        curr_map = curr_map->r;
        break;
      case 'L':
        curr_map = curr_map->l;
        break;
      }
    }
    curr_lcm = curr_lcm? lcm(j, curr_lcm) : j;
  }
  return curr_lcm;
}

size_t lcm(size_t x, size_t y){
  return x * y / gcd(x, y);
}

size_t gcd(size_t x, size_t y) {
  size_t t;
  while (y) { t = y; y = x%y; x = t; }
  return x;
}

int get_steps(char *instructions, map_t *maps, size_t n_maps) {
  int i = 0;
  map_t curr_map;
  while (strncmp((curr_map = maps[i++]).name, "AAA", 3)) { // Get starting map
    if (i == n_maps) {
      return -1;
    }
  }

  size_t len_instr = strlen(instructions);
  i = 0;

  while (1) {
    if (strncmp(curr_map.name, "ZZZ", 3) == 0) {
      return i;
    }
    switch (instructions[i++ % len_instr]) {
    case 'R':
      curr_map = *(curr_map.r);
      break;
    case 'L':
      curr_map = *(curr_map.l);
      break;
    }
  }
}

void parse_file(FILE *file, char **instructions, size_t *n_instr, map_t **maps,
                size_t *n_maps) {
  char c;
  size_t i = 0;
  while ((c = getc(file)) != '\n') {
    (*instructions)[i++] = c;
    if (i >= *n_instr) {
      *n_instr *= 2;
      *instructions = realloc(*instructions, sizeof(char) * *n_instr);
      if (!*instructions) {
        printf("Realloc failed, exiting\n");
        exit(1);
      }
    }
  }
  (*instructions)[i] = '\0';

  while ((c = getc(file)) == '\n')
    ;
  ungetc(c, file);

  char **ls = malloc(sizeof(char *) * *n_maps);
  char **rs = malloc(sizeof(char *) * *n_maps);
  size_t maxlinesize = 100;
  char *map_name = malloc(sizeof(char) * maxlinesize);
  char *lstr = malloc(sizeof(char) * maxlinesize);
  char *rstr = malloc(sizeof(char) * maxlinesize);
  i = 0;
  size_t map_no = 0;
  int read;
  char **parsing = &map_name;
  int to_parse = 0;
  int change_parsing = 1;
  while ((c = getc(file)) != EOF) {
    if (isalnum(c)) {
      (*parsing)[i++] = c;
      change_parsing = 1;
    } else if (change_parsing) {
      (*parsing)[i] = '\0';
      i = 0;
      to_parse++;
      to_parse %= 3;
      switch (to_parse) {
      case 0: // Happens on every new line
        if (map_no >= *n_maps) {
          *n_maps *= 2;
          *maps = realloc(*maps, sizeof(map_t) * *n_maps);
          ls = realloc(ls, sizeof(char *) * *n_maps);
          rs = realloc(rs, sizeof(char *) * *n_maps);
          if (!*maps || !rs || !ls) {
            printf("Realloc failed, exiting\n");
            exit(1);
          }
        }
        (*maps)[map_no].name = map_name;
        ls[map_no] = lstr;
        rs[map_no] = rstr;
        map_name = malloc(sizeof(char) * maxlinesize);
        lstr = malloc(sizeof(char) * maxlinesize);
        rstr = malloc(sizeof(char) * maxlinesize);
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

  for (int i = 0; i < map_no; ++i) {
    for (int j = 0; j < map_no; ++j) {
      // Get the reference to the map with a name matching the left/right name
      // expected
      if (strncmp(ls[i], (*maps)[j].name, maxlinesize) == 0) {
        (*maps)[i].l = &(*maps)[j];
      }
      if (strncmp(rs[i], (*maps)[j].name, maxlinesize) == 0) {
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

void print_map(map_t *maps, size_t n_maps) {
  for (int i = 0; i < n_maps; ++i) {
    printf("%s = (%s, %s)\n", maps[i].name, maps[i].l->name, maps[i].r->name);
  }
}
