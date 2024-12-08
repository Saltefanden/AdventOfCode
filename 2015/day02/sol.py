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
            sides = [int(el) for el in line.split("x")]
            faces = [sides[0] * sides[1], sides[0] * sides[2], sides[1] * sides[2]]
            smallest_face = min(faces)
            score += 2 * sum(faces) + smallest_face
        print(score)



def part2(filename: str):
    with open(filename, "r") as f:
        score = 0
        while line := f.readline().strip():
            sides = [int(el) for el in line.split("x")]
            max_side_idx = sides.index(max(sides))
            two_smallest_sides = [side for idx, side in enumerate(sides) if idx!=max_side_idx]
            volume = 1
            for side in sides:
                volume *= side
            score += 2 * sum(two_smallest_sides) + volume
        print(score)


if __name__ == "__main__":
    main()
