#! /usr/bin/env python
import sys
from typing import List


def main():
    if (len(sys.argv) != 2): 
        print(f"Usage {sys.argv[0]} <filename>")
        return;
    part1(sys.argv[1])
    part2(sys.argv[1])

def part1(filename: str):
    score = 0
    with open(filename, "r") as f:
        while(line := f.readline().strip()): 
            curr_arr = [int(i) for i in line.split()]
            allarrs = [curr_arr]
            while (any(curr_arr)):
                allarrs.append(curr_arr := diff(curr_arr))

            expand(allarrs)
            score += allarrs[0][-1]

    print(f"Part 1: {score}")

            

def part2(filename: str):
    score = 0
    with open(filename, "r") as f:
        while(line := f.readline().strip()): 
            curr_arr = [int(i) for i in line.split()]
            curr_arr.reverse()
            allarrs = [curr_arr]
            while (any(curr_arr)):
                allarrs.append(curr_arr := diff(curr_arr))

            expand(allarrs)
            score += allarrs[0][-1]

    print(f"Part 2: {score}")


def expand(allarrs: List[List[int]]):
    last_arr = allarrs[-1]
    last_arr.append(0)
    for i in range(len(allarrs)-1):
        allarrs[-2-i].append(allarrs[-1-i][-1]+ allarrs[-2-i][-1])

def diff(x: list):
    return [x[i+1] - x[i] for i in range(len(x)-1)]

if __name__ == '__main__':
    main()
