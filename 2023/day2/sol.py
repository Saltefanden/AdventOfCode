import sys
import re


def part1(filename):
    limits = [12, 13, 14]
    score = 0
    with open(filename, "r") as f: 
        while (line := f.readline().strip()):
            gameno = re.findall("Game (\d+)", line)[0]
            reds = [int(match) for match in re.findall("(\d+) red", line) if
                    int(match)>limits[0]]
            greens = [int(match) for match in re.findall("(\d+) green", line) if
                      int(match)>limits[1]]
            blues = [int(match) for match in re.findall("(\d+) blue", line) if
                     int(match)>limits[2]]

            if not (any(reds) or any(greens) or any(blues)):
                score += int(gameno)

    print(score)

def part2(filename):
    score = 0
    with open(filename, "r") as f:
        while (line := f.readline().strip()):
            line = line.split(":")[1]
            games = line.split(";")
            maxes = [0, 0, 0]
            for game in games:
                reds = sum([int(match) for match in re.findall("(\d+) red",
                                                               game)])
                greens = sum([int(match) for match in re.findall("(\d+) green",
                                                                 game)])
                blues = sum([int(match) for match in re.findall("(\d+) blue",
                                                                game)])
                maxes = [max(maxes[0],reds), max(maxes[1],greens),
                         max(maxes[2],blues) ]
            powers = maxes[0] * maxes[1] * maxes[2]
            score += powers
    print(score)



def main(filename: str) -> None:
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        exit(1)
    main(sys.argv[1])
