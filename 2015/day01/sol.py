#! /usr/bin/env python
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    with open(filename, "r") as f:
        while line := f.readline().strip():
            floor = 0
            for ch in line:
                if ch == "(":
                    floor += 1
                elif ch == ")":
                    floor -= 1
                else:
                    print("what")
            print(floor)


def part2(filename: str):
    with open(filename, "r") as f:
        while line := f.readline().strip():
            floor = 0
            for idx, ch in enumerate(line):
                if ch == "(":
                    floor += 1
                elif ch == ")":
                    floor -= 1
                else:
                    print("what")
                if floor == -1:
                    print("PART 2: ", idx + 1)
                    break

if __name__ == "__main__":
    main()
