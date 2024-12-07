#! /usr/bin/env python
from time import sleep
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    global part1grid
    grid = []
    guard_symbols = list("^>v<")
    guard_symbol = ""
    with open(filename, "r") as f:
        guard_row = -1
        guard_col = -1
        row = -1
        while line := f.readline().strip():
            row += 1
            grid.append(list(line))
            if [
                guard_col := idx
                for idx, el in enumerate(list(line))
                if el in set("^>v<")
            ]:
                guard_symbol = grid[guard_row := row][guard_col]
    gridsize = len(grid), len(grid[0])
    # print(*grid, sep="\n")
    # print("")
    while True:
        if guard_symbol == "^":
            if guard_row - 1 < 0:
                grid[guard_row][guard_col] = "X"
                break
            if grid[guard_row - 1][guard_col] == "#":
                guard_symbol = ">"
            else:
                grid[guard_row][guard_col] = "X"
                grid[guard_row := guard_row - 1][guard_col] = guard_symbol
        elif guard_symbol == ">":
            if guard_col + 1 >= gridsize[1]:
                grid[guard_row][guard_col] = "X"
                break
            if grid[guard_row][guard_col + 1] == "#":
                guard_symbol = "v"
            else:
                grid[guard_row][guard_col] = "X"
                grid[guard_row][guard_col := guard_col + 1] = guard_symbol
        elif guard_symbol == "v":
            if guard_row + 1 >= gridsize[0]:
                grid[guard_row][guard_col] = "X"
                break
            if grid[guard_row + 1][guard_col] == "#":
                guard_symbol = "<"
            else:
                grid[guard_row][guard_col] = "X"
                grid[guard_row := guard_row + 1][guard_col] = guard_symbol
        elif guard_symbol == "<":
            if guard_col - 1 < 0:
                grid[guard_row][guard_col] = "X"
                break
            if grid[guard_row][guard_col - 1] == "#":
                guard_symbol = "^"
            else:
                grid[guard_row][guard_col] = "X"
                grid[guard_row][guard_col := guard_col - 1] = guard_symbol
        else:
            print("WHADDUP")

    score = 0
    for row in grid:
        for el in row:
            if el == "X":
                score += 1
    part1grid = grid
    # print(*grid, sep="\n")
    print(score)


def part2(filename: str):
    score = 0
    grid = []
    guard_symbol = ""
    with open(filename, "r") as f:
        guard_row = -1
        guard_col = -1
        row = -1
        while line := f.readline().strip():
            row += 1
            grid.append(list(line))
            if [ guard_col := idx for idx, el in enumerate(list(line)) if el in set("^>v<") ]:
                guard_symbol = grid[guard_row := row][guard_col]
    original_guard_symbol = guard_symbol
    original_guard_row = guard_row
    original_guard_col = guard_col
    originalgrid = [[el for el in row] for row in grid]
    gridsize = len(grid), len(grid[0])
    print(*grid, sep="\n")
    print(*originalgrid, sep="\n")
    for ridx, row in enumerate(originalgrid):
        for cidx, element in enumerate(row):
            if element in set("#^>v<"): # Not ones to be changed!
                continue
            elif part1grid[ridx][cidx] != "X": # Not somewhere the guard would visit anyways
                continue
            else:
                print(f"Attempting {ridx}, {cidx}\n")
                guard_symbol = original_guard_symbol
                guard_row = original_guard_row
                guard_col = original_guard_col
                grid = [[el for el in row] for row in originalgrid]
                grid[ridx][cidx] = "#"
                while True:
                    if (ridx, cidx) == (84, 81):
                        print(guard_row, guard_col)
                        # print(*grid, sep="\n")
                        # sleep(0.1)
                    # print(*grid, sep="\n")
                    # sleep(0.1)
                    if guard_symbol == "^":
                        if guard_row - 1 < 0:
                            # grid[guard_row][guard_col] = "X"
                            break
                        if grid[guard_row - 1][guard_col] == "#":
                            grid[guard_row][guard_col] += '^'
                            guard_symbol = ">"
                        else:
                            if "^" in grid[guard_row -1][guard_col]:
                                # Loop detected
                                print("LOOOP")
                                score += 1
                                break
                            elif grid[guard_row][guard_col] in set("-+"):
                                grid[guard_row][guard_col] = '+'
                            else:
                                grid[guard_row][guard_col] += "^"
                            # grid[guard_row := guard_row - 1][guard_col] = guard_symbol
                            guard_row -= 1
                    elif guard_symbol == ">":
                        if guard_col + 1 >= gridsize[1]:
                            # grid[guard_row][guard_col] = "X"
                            break
                        if grid[guard_row][guard_col + 1] == "#":
                            grid[guard_row][guard_col] += '>'
                            guard_symbol = "v"
                        else:
                            if ">" in grid[guard_row][guard_col+1]:
                                # Loop detected
                                score += 1
                                print("LOOOP")
                                break
                            elif grid[guard_row][guard_col] in set("|+"):
                                grid[guard_row][guard_col] = '+'
                            else:
                                grid[guard_row][guard_col] += ">"
                            guard_col += 1 
                            # grid[guard_row][guard_col := guard_col + 1] = guard_symbol
                    elif guard_symbol == "v":
                        if guard_row + 1 >= gridsize[0]:
                            grid[guard_row][guard_col] = "X"
                            break
                        if grid[guard_row + 1][guard_col] == "#":
                            grid[guard_row][guard_col] += 'v'
                            guard_symbol = "<"
                        else:
                            if "v" in grid[guard_row+1][guard_col]:
                                # Loop detected
                                score += 1
                                print("LOOOP")
                                break
                            elif grid[guard_row][guard_col] in set("-+"):
                                grid[guard_row][guard_col] = '+'
                            else:
                                grid[guard_row][guard_col] += "v"
                            guard_row += 1
                            # grid[guard_row := guard_row + 1][guard_col] = guard_symbol
                    elif guard_symbol == "<":
                        if guard_col - 1 < 0:
                            grid[guard_row][guard_col] = "X"
                            break
                        if grid[guard_row][guard_col - 1] == "#":
                            grid[guard_row][guard_col] += '<'
                            guard_symbol = "^"
                        else:
                            if "<" in grid[guard_row][guard_col-1]:
                                # Loop detected
                                score += 1
                                print("LOOOP")
                                break
                            elif grid[guard_row][guard_col] in set("|+"):
                                grid[guard_row][guard_col] = '+'
                            else:
                                grid[guard_row][guard_col] += "<"
                            guard_col -= 1
                            # grid[guard_row][guard_col := guard_col - 1] = guard_symbol
                    else:
                        print("WHADDUP")


    print(score)


if __name__ == "__main__":
    main()
