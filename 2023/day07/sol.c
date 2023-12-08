#include <ctype.h>
#include <stddef.h>
#define __GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

#define HANDSIZE 5

typedef enum { NOTHING = 0, PAIR, TWOPAIR, THREE, HOUSE, FOUR, FIVE } cat_t;

typedef struct {
  cat_t category;
  int cards[HANDSIZE];
  int bid;
} hand_t;

void part1(char *filename);
void part2(char *filename);

int card2numeric(const char c);
size_t parse_cards(hand_t **hands, FILE *file, int prealloc);
void add_categories(hand_t *hands, size_t nhands);
void get_category(hand_t *hand);
int comp_hand(const void *a, const void *b);
void set_jokers(hand_t *hands, size_t nhands);

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
  int score = 0;
  int prealloc = 2;
  hand_t *hands = malloc(sizeof(hand_t) * prealloc);
  size_t nhands = parse_cards(&hands, file, prealloc);
  add_categories(hands, nhands);
  qsort(hands, nhands, sizeof(hand_t), comp_hand);
  for (int i = 0; i < nhands; ++i) {
    score += (i + 1) * hands[i].bid;
  }
  printf("Part 1 score: %d\n", score);
  free(hands);
  fclose(file);
}

void part2(char *filename) {
  FILE *file = fopen(filename, "r");
  int score = 0;
  int prealloc = 2;
  hand_t *hands = malloc(sizeof(hand_t) * prealloc);
  size_t nhands = parse_cards(&hands, file, prealloc);
  add_categories(hands, nhands);
  set_jokers(hands, nhands);
  qsort(hands, nhands, sizeof(hand_t), comp_hand);
  for (int i = 0; i < nhands; ++i) {
    score += (i + 1) * hands[i].bid;
  }
  printf("Part 2 score: %d\n", score);
  free(hands);
  fclose(file);
}

void set_jokers(hand_t *hands, size_t nhands) {
  for (int i = 0; i < nhands; ++i) {
    int n_jokers = 0;
    cat_t newcat;
    cat_t oldcat = hands[i].category;
    for (int card = 0; card < HANDSIZE; ++card) {
      if (hands[i].cards[card] == 10) {
        n_jokers++;
        hands[i].cards[card] = 0; // set value low
      } else {
      }
    }
    switch (n_jokers) {
    // cat_t: { NOTHING = 0, PAIR, TWOPAIR, THREE, HOUSE, FOUR, FIVE }
    case 5:
      newcat = oldcat;
      break;
    case 4:
      newcat = FIVE;
      break;
    case 3:
      newcat = oldcat + 2;
      break; // THREE->FOUR(+2)  HOUSE->FIVE(+2)
    case 2:
      newcat = oldcat == 2 ? oldcat + 3 : oldcat + 2;
      break; // HOUSE->FIVE(+2) TWOPAIR->FOUR(+3) PAIR->THREE(+2)
    case 1:
      newcat = oldcat % 5 == 0 ? oldcat + 1 : oldcat + 2;
      break; // NOTHING->PAIR(+1) PAIR->THREE(+2) TWOPAIR->HOUSE(+2)
             // THREE->FOUR(+2) FOUR->FIVE(+1)
    case 0:
      newcat = oldcat;
      break;
    }
    hands[i].category = newcat;
  }
}

int comp_hand(const void *a, const void *b) {
  hand_t *handa = (hand_t *)a;
  hand_t *handb = (hand_t *)b;
  int catdif = handa->category - handb->category;
  int carddiff;
  if (catdif) {
    return catdif;
  } else {
    for (int i = 0; i < HANDSIZE; ++i) {
      if ((carddiff = handa->cards[i] - handb->cards[i])) {
        return carddiff;
      }
    }
  }
  exit(1);
}

void add_categories(hand_t *hands, size_t nhands) {
  for (int i = 0; i < nhands; ++i) {
    get_category(&hands[i]);
  }
}

void get_category(hand_t *hand) {
  int found[14] = {0};
  int largest = 0;
  int second = 0;
  int times_found;
  for (int i = 0; i < HANDSIZE; ++i) {
    found[hand->cards[i]]++;
  }
  for (int i = 0; i < 14; ++i) {
    if ((times_found = found[i])) {
      if (times_found >= largest) {
        second = largest;
        largest = times_found;
      } else if (times_found > second) {
        second = times_found;
      }
    }
  }
  if (largest == 5) {
    hand->category = FIVE;
  }
  if (largest == 4) {
    hand->category = FOUR;
  }
  if (largest == 3) {
    hand->category = second == 2 ? HOUSE : THREE;
  }
  if (largest == 2) {
    hand->category = second == 2 ? TWOPAIR : PAIR;
  }
  if (largest == 1) {
    hand->category = NOTHING;
  }
}

size_t parse_cards(hand_t **hands, FILE *file, int prealloc) {
  _Bool iscards = 1;
  size_t currcard = 0;
  size_t nhands = 0;
  char c;
  hand_t *new=NULL;
  while ((c = getc(file)) != EOF) {
    if (c == ' ') {
      iscards = 0;
    }
    if (iscards) {
      (*hands)[nhands].cards[currcard++] = card2numeric(c);
    } else { // is bids
      (*hands)[nhands].bid = 0;
      while ((c = getc(file)) != '\n') {
        (*hands)[nhands].bid = 10 * (*hands)[nhands].bid + c - '0';
      }
      iscards = 1;
      ++nhands;
      if (nhands >= prealloc) {
        prealloc *= 2;
        new = realloc(*hands, sizeof(hand_t) * prealloc);
        if (new) {
          *hands = new;
        } else {
          printf("Realloc failed! PANIC!\n");
          exit(1);
        }
      }
      currcard = 0;
    }
  }
  return nhands;
}

int card2numeric(const char c) {
  switch (c) {
  case 'T':
    return 9;
  case 'J':
    return 10;
  case 'Q':
    return 11;
  case 'K':
    return 12;
  case 'A':
    return 13;
  default:
    return c - '0' - 1;
  }
}
