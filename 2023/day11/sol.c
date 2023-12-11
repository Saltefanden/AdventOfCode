#include <stddef.h>
#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

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
  char c = '\0';
  size_t row = 0;
  size_t col = 0;
  size_t n_galaxies = 0;
  size_t galaxies[2][1000];
  size_t galaxy_in_col[1000] = {0};
  _Bool galaxy_in_row;
  size_t maxcols = 0;

  size_t row_expander = 0;
  while (c != EOF) {
    galaxy_in_row = 0;
    while ((c = getc(file)) != '\n' && c != EOF) {
      if (c == '#') {
        /* printf("Found a GALAXY at (%zu, %zu)\n", row, col); */
        galaxy_in_row = 1;
        galaxy_in_col[col] = 1;
        galaxies[0][n_galaxies] = row + row_expander;
        galaxies[1][n_galaxies] = col;
        ++n_galaxies;
      }
      ++col;
    }
    maxcols = maxcols == 0 ? col : maxcols;
    col = 0;
    ++row;
    if (!galaxy_in_row) { 
      ++row_expander;
    }
  }

  size_t column_expander = 0;
  size_t column_expansion[1000] = {0};
  for (size_t i = 0; i < maxcols; ++i) {
    if (!galaxy_in_col[i]){
      ++column_expander;
    }  
    column_expansion[i] = i + column_expander;
  }


  for (size_t i = 0; i < n_galaxies; ++i) {
    galaxies[1][i] = column_expansion[ galaxies[1][i] ];
    /* printf("Galaxy expanded to %zu, %zu\n", galaxies[0][i], galaxies[1][i]); */
  }

  size_t score = 0;
  size_t curr_row;
  size_t curr_col;
  size_t comp_row;
  size_t comp_col;
  size_t xdist;
  size_t ydist;
  for (size_t i = 0; i < n_galaxies-1; ++i){
    curr_row = galaxies[0][i];
    curr_col = galaxies[1][i];
    for (size_t j = i+1; j< n_galaxies; ++j){
      comp_row = galaxies[0][j];
      comp_col = galaxies[1][j];
      xdist = curr_col > comp_col ? curr_col - comp_col : comp_col - curr_col;
      ydist = curr_row > comp_row ? curr_row - comp_row : comp_row - curr_row;
      /* printf("Distance between Galaxy %zu and %zu: x=%zu, y=%zu\n", i, j, xdist, ydist); */
      score += xdist + ydist; 
    }
  }
  printf("Part 1: %zu\n", score);

  fclose(file);
}

void part2(char *filename) {
  FILE *file = fopen(filename, "r");
  char c = '\0';
  size_t row = 0;
  size_t col = 0;
  size_t n_galaxies = 0;
  size_t galaxies[2][1000];
  size_t galaxy_in_col[1000] = {0};
  _Bool galaxy_in_row;
  size_t maxcols = 0;
  size_t expansion_size = 1000000-1;
  size_t row_expander = 0;
  while (c != EOF) {
    galaxy_in_row = 0;
    while ((c = getc(file)) != '\n' && c != EOF) {
      if (c == '#') {
        /* printf("Found a GALAXY at (%zu, %zu)\n", row, col); */
        galaxy_in_row = 1;
        galaxy_in_col[col] = 1;
        galaxies[0][n_galaxies] = row + row_expander;
        galaxies[1][n_galaxies] = col;
        ++n_galaxies;
      }
      ++col;
    }
    maxcols = maxcols == 0 ? col : maxcols;
    col = 0;
    ++row;
    if (!galaxy_in_row) { 
      row_expander += expansion_size;
    }
  }

  size_t column_expander = 0;
  size_t column_expansion[1000] = {0};
  for (size_t i = 0; i < maxcols; ++i) {
    if (!galaxy_in_col[i]){
      column_expander += expansion_size;
    }  
    column_expansion[i] = i + column_expander;
  }


  for (size_t i = 0; i < n_galaxies; ++i) {
    galaxies[1][i] = column_expansion[ galaxies[1][i] ];
    /* printf("Galaxy expanded to %zu, %zu\n", galaxies[0][i], galaxies[1][i]); */
  }

  size_t score = 0;
  size_t curr_row;
  size_t curr_col;
  size_t comp_row;
  size_t comp_col;
  size_t xdist;
  size_t ydist;
  for (size_t i = 0; i < n_galaxies-1; ++i){
    curr_row = galaxies[0][i];
    curr_col = galaxies[1][i];
    for (size_t j = i+1; j< n_galaxies; ++j){
      comp_row = galaxies[0][j];
      comp_col = galaxies[1][j];
      xdist = curr_col > comp_col ? curr_col - comp_col : comp_col - curr_col;
      ydist = curr_row > comp_row ? curr_row - comp_row : comp_row - curr_row;
      /* printf("Distance between Galaxy %zu and %zu: x=%zu, y=%zu\n", i, j, xdist, ydist); */
      score += xdist + ydist; 
    }
  }
  printf("Part 1: %zu\n", score);

  fclose(file);
}
