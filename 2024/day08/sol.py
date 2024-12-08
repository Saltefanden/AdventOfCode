#! /usr/bin/env python
import sys
from collections import defaultdict


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    nodes = set()
    score = 0
    cols = 0
    rows = 0
    antennas = defaultdict(list)
    with open(filename, "r") as f:
        while line := f.readline().strip():
            cols = 0
            for ch in line:
                antennas[ch].append((rows, cols))
                cols += 1
            rows += 1

     
    print(rows, cols)
    for key, val in antennas.items():
        if key == ".":
            continue
        else:
            for idx1, pos1 in enumerate(val[:-1]):
                for pos2 in val[idx1+1:]:
                    dr, dc = [el2 - el1 for el1, el2 in zip(pos1, pos2)]

                    antinode1 = pos1[0] - dr, pos1[1] - dc
                    if (antinode1[0] < rows 
                        and 0 <= antinode1[0]
                        and antinode1[1] < cols
                        and 0 <= antinode1[1] 
                    ):
                        nodes.add(antinode1)
                    antinode2 = pos2[0] + dr, pos2[1] + dc
                    
                    if (antinode2[0] < rows 
                        and 0 <= antinode2[0]
                        and antinode2[1] < cols
                        and 0 <= antinode2[1] 
                    ):
                        nodes.add(antinode2)

    print(len(nodes))


def part2(filename: str):
    nodes = set()
    score = 0
    cols = 0
    rows = 0
    antennas = defaultdict(list)
    with open(filename, "r") as f:
        while line := f.readline().strip():
            cols = 0
            for ch in line:
                antennas[ch].append((rows, cols))
                cols += 1
            rows += 1

     
    print(rows, cols)
    for key, val in antennas.items():
        if key == ".":
            continue
        else:
            for idx1, pos1 in enumerate(val[:-1]):
                for pos2 in val[idx1+1:]:
                    dr, dc = [el2 - el1 for el1, el2 in zip(pos1, pos2)]

                    harmonics = 0 
                    while True:
                        antinode1 = pos1[0] - dr * harmonics, pos1[1] - dc * harmonics
                        harmonics += 1
                        if (antinode1[0] < rows 
                            and 0 <= antinode1[0]
                            and antinode1[1] < cols
                            and 0 <= antinode1[1] 
                        ):
                            nodes.add(antinode1)
                        else:
                            break

                    harmonics = 0
                    while True:
                        antinode2 = pos2[0] + dr * harmonics, pos2[1] + dc * harmonics
                        harmonics += 1 
                        if (antinode2[0] < rows 
                            and 0 <= antinode2[0]
                            and antinode2[1] < cols
                            and 0 <= antinode2[1] 
                        ):
                            nodes.add(antinode2)
                        else:
                            break

    print(len(nodes))


if __name__ == "__main__":
    main()
