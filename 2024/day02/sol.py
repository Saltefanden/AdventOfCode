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
        score = 0
        while line := f.readline().strip():
            arr = [int(el) for el in line.split()]
            curr = arr[0]
            globalsign = 0
            safevals = [1]
            for el in arr[1:]:
                safe, globalsign = issafe(el, curr, globalsign)
                safevals.append(safe)
                curr = el
            score += all(safevals)

    print(score)


def part2(filename: str):
    with open(filename, "r") as f:
        score = 0
        while line := f.readline().strip():
            arr = [int(el) for el in line.split()]
            safearrs = []
            for i in range(len(arr)):
                newarr = [el for idx, el in enumerate(arr) if idx != i]
                curr = newarr[0]
                globalsign = 0
                safevals = [1]
                for el in newarr[1:]:
                    safe, globalsign = issafe(el, curr, globalsign)
                    safevals.append(safe)
                    curr = el
                safearrs.append(all(safevals)) 
            score += any(safearrs)

        print(score)


def issafe(a, b, globalsign):
    safe = 1
    diff = a - b
    if abs(diff) > 3 or diff == 0:
        safe = 0
    sign = 1 if diff > 0 else -1
    globalsign = globalsign if globalsign else sign
    if sign != globalsign:
        safe = 0
    return safe, globalsign


if __name__ == "__main__":
    main()
