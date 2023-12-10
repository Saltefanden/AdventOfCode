#! /usr/bin/env python
import sys


def main():
    if (len(sys.argv) != 2): 
        print(f"Usage {sys.argv[0]} <filename>")
        return;
    part1(sys.argv[1])
    part2(sys.argv[1])

def part1(filename: str):
    with open(filename, "r") as f:
        while( line:=f.readline().strip()):
            pass


def part2(filename: str):
    with open(filename, "r") as f:
        while( line:=f.readline().strip()):
            pass

if __name__ == '__main__':
    main()
