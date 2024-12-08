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
            houses_visited = set()
            curr_location = (0,0)
            houses_visited.add(curr_location)
            for ch in line:
                if ch == "^":
                    curr_location = (curr_location[0] - 1, curr_location[1])
                elif ch == ">":
                    curr_location = (curr_location[0], curr_location[1]+1)
                elif ch == "v":
                    curr_location = (curr_location[0] + 1, curr_location[1])
                elif ch == "<":
                    curr_location = (curr_location[0], curr_location[1]-1)
                houses_visited.add(curr_location)
            print(len(houses_visited))

            


def part2(filename: str):
    with open(filename, "r") as f:
        while line := f.readline().strip():
            houses_visited = set()
            santa_curr_location = (0,0)
            robo_curr_location = (0,0)
            issanta = True
            curr_location = santa_curr_location if issanta else robo_curr_location
            houses_visited.add(curr_location)
            for ch in line:
                issanta = not issanta
                curr_location = santa_curr_location if issanta else robo_curr_location
                if ch == "^":
                    curr_location = (curr_location[0] - 1, curr_location[1])
                elif ch == ">":
                    curr_location = (curr_location[0], curr_location[1]+1)
                elif ch == "v":
                    curr_location = (curr_location[0] + 1, curr_location[1])
                elif ch == "<":
                    curr_location = (curr_location[0], curr_location[1]-1)
                if issanta:
                    santa_curr_location = curr_location
                else:
                    robo_curr_location = curr_location
                houses_visited.add(curr_location)
            print(len(houses_visited))


if __name__ == "__main__":
    main()
