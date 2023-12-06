#! /usr/bin/env python
import sys 


def part1(filename):
    score = 0
    total_lines = []
    non_symbols = {*"1234567890."}
    with open(filename, "r") as f:
        while (line := f.readline().strip()):
            total_lines.append(line)
    # [print(line) for line in total_lines]
    for idx, line in enumerate(total_lines):
        for jdx, char in enumerate(line):
            if char not in non_symbols:
                symbolidx = (idx, jdx)
                for i in range(idx-1, idx+2):
                    for j in range(jdx-1, jdx+2):
                        if total_lines[i][j].isdigit():
                            startpos, endpos = get_number_limits(total_lines[i], j)
                            part_number = int(total_lines[i][startpos:endpos])
                            newline = ''.join('.' if startpos<=index<endpos else
                                              c for
                                              index, c in
                                              enumerate(total_lines[i]))
                            total_lines[i] = newline
                            score += part_number
    print("Part 1 score: ", score)

def part2(filename):
    score = 0
    total_lines = []
    non_symbols = {*"1234567890."}
    with open(filename, "r") as f:
        while (line := f.readline().strip()):
            total_lines.append(line)
    # [print(line) for line in total_lines]
    for idx, line in enumerate(total_lines):
        for jdx, char in enumerate(line):
            if char == "*":
                n_found = 0
                gear_ratio =1 
                symbolidx = (idx, jdx)
                for i in range(idx-1, idx+2):
                    startend = set()
                    for j in range(jdx-1, jdx+2):
                        if total_lines[i][j].isdigit():
                            startpos, endpos = get_number_limits(total_lines[i], j)
                            if (startpos, endpos) not in startend:
                                startend.add((startpos, endpos))
                                n_found+= 1
                                part_number = int(total_lines[i][startpos:endpos])
                                gear_ratio *= part_number

                if n_found == 2:
                    score += gear_ratio
                if n_found > 2:
                    print("FUCK")
                    print("FUCK AT: ", idx+1, "col ", jdx+1)
                    exit(1)
                if n_found == 1:
                    print("Not a gear at lineno ", idx+1, "col ", jdx+1)

    print("Part 2 score: ", score)


def get_number_limits(linestr, j):
    backposition=j
    forwardposition = j
    maximum = len(linestr)
    while (linestr[backposition-1].isdigit()):
        backposition-=1
    while (forwardposition < maximum and linestr[forwardposition].isdigit()): # Remember the end is the limiter
        forwardposition+=1
    return backposition, forwardposition # (linestr[backposition:forwardposition])


def main():
    if len(sys.argv) == 2:
        part1(sys.argv[1])
        part2(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} filename")

if __name__ == '__main__':
    main()
