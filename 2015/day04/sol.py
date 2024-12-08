#! /usr/bin/env python
import sys
import hashlib


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    with open(filename, "r") as f:
        while line := f.readline().strip():
            n = 0
            while True:
                aug = line + str(n)
                result = hashlib.md5(aug.encode())
                if result.hexdigest()[:5] == "00000":
                    print(n)
                    break
                n += 1
                


def part2(filename: str):
    with open(filename, "r") as f:
        while line := f.readline().strip():
            n = 0
            while True:
                aug = line + str(n)
                result = hashlib.md5(aug.encode())
                if result.hexdigest()[:6] == "0"*6:
                    print(n)
                    break
                n += 1


if __name__ == "__main__":
    main()
