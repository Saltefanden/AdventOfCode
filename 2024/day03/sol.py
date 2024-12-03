#! /usr/bin/env python
import sys
import re

def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    with open(filename, "r") as f:
        score = 0
        while line := f.readline().strip():
            res =re.findall(r"mul\(\d+,\d+\)", line)
            for mul in res:
                stripped = mul.strip("mul").strip(")(").split(",")
                product = int(stripped[0]) * int(stripped[1])
                score += product
        print(score) 

             


def part2(filename: str):
    with open(filename, "r") as f:
        score = 0
        line = f.read()
        does = line.split("do()")
        for do in does:
            realdo = do.split("don't()")[0]
            res =re.findall(r"mul\(\d+,\d+\)", realdo)
            for mul in res:
                stripped = mul.strip("mul").strip(")(").split(",")
                product = int(stripped[0]) * int(stripped[1])
                score += product
        print(score) 


if __name__ == "__main__":
    main()
