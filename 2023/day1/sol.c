#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int read_line(char *line, FILE *file);
void part1(char *filename);
void part2(char *filename);
int get_first_digit(char *line, int n_read);
int get_last_digit(char *line, int n_read);
int get_str_digit(char *line, int until);
int starts_with(char *text, char *substr);
int str_len(char *str);

int main(int argc, char *argv[]) {
  part1(argv[1]);
  part2(argv[1]);
}

void part1(char* filename) {
  FILE *file = fopen(filename, "r");
  char line[1024];
  char c;
  int digit;
  int n_read;
  int first_digit;
  int last_digit;
  int score = 0;
  while ((n_read = read_line(line, file)) != -1) {
    first_digit = -1;
    for (int i = 0; i < n_read; ++i) {
      if ((c = line[i]) <= '9' && c >= '0') {
        digit = c - '0';
        first_digit = first_digit == -1 ? digit : first_digit;
        last_digit = digit;
      }
    }
    score += first_digit * 10 + last_digit;
  }
  printf("Part 1 score: %d\n", score);
}

void part2(char* filename) {
  FILE *file = fopen(filename, "r");
  char line[1024];
  int n_read;
  int first_digit;
  int last_digit;
  int score = 0;
  while ((n_read = read_line(line, file)) != -1) {
    first_digit = get_first_digit(line, n_read);
    last_digit = get_last_digit(line, n_read);
    score += first_digit * 10 + last_digit;
  }
  printf("Part 2 score: %d\n", score);
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

int get_first_digit(char *line, int n_read) {
  char c;
  int digit;
  for (int i = 0; i < n_read; ++i) {
    c = line[i];
    if (c <= '9' && c >= '0') {
      return c - '0';
    } else if ((digit = get_str_digit(line, i)) != -1) {
      return digit;
    }
  }
  return -1;
}

int get_last_digit(char *line, int n_read) {
  char c;
  int digit;
  for (int i = n_read; i >= 0; --i) {
    c = line[i];
    if (c <= '9' && c >= '0') {
      return c - '0';
    } else if ((digit = get_str_digit(line + i, n_read - i)) != -1) {
      return digit;
    }
  }
  return -1;
}

int get_str_digit(char *line, int until) {
  char *numbers[] = {"one", "two",   "three", "four", "five",
                     "six", "seven", "eight", "nine"};

  int word_length;

  for (int i = 0; i < 9; ++i) {
    word_length = str_len(numbers[i]);
    for (int j = 0; j <= until - (word_length - 1); ++j) {
      if (starts_with(line + j, numbers[i])) {
        return i + 1;
      }
    }
  }
  return -1;
}

int str_len(char *str) {
  int i = 0;
  while (str[i] != '\0') {
    ++i;
  }
  return i;
}

int starts_with(char *text, char *substr) {
  while (*substr++ == *text++) {
    if (*substr == '\0')
      return 1;
  }
  return 0;
}
