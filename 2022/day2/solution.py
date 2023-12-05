#! /usr/bin/env python
import sys 


def part1():
    score=0

    scorekeys = {
        "X": 1,     # Rock
        "Y": 2,     # Paper
        "Z": 3,     # Scissors
    }

    winkeys = {
        "X": "CAB",
        "Y": "ABC",
        "Z": "BCA",
    }


    with open("input", "r") as file: 
        while (line := file.readline().strip()):
            opponent, player = line.split()
            choice_score = scorekeys[player]
            win_score = (
                    6 if opponent == winkeys[player][0]
                    else 3 if opponent == winkeys[player][1]
                    else 0 if opponent == winkeys[player][2]
                    else -10000000000
                    )
            score += choice_score + win_score

    print("Part 1: ", score)

def part2():
    score=0

    scorekeys = {
        "A": 1,     # Rock
        "B": 2,     # Paper
        "C": 3,     # Scissors
    }

    relation = {
        "X": "0CAB",
        "Y": "0ABC",
        "Z": "0BCA",
    }

    winkeys = {
        "X": 0,
        "Y": 1,
        "Z": 2,
    }


    with open("input", "r") as file: 
        while (line := file.readline().strip()):
            opponent, player = line.split()
            choice_score = (
                 scorekeys[relation[player][scorekeys[opponent]]]
            )
            win_score = winkeys[player] * 3
            score += choice_score + win_score

    print("Part 2: ", score)

def main():
    if (len(sys.argv)!=2):
        print(f"Usage {sys.argv[0]} <filename>")
        exit(0)
    part1() 
    part2()

if __name__ == '__main__':
    main()
