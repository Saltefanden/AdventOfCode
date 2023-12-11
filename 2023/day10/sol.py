#! /usr/bin/env python
import sys



go_left  = (0, -1)
go_up    = (-1, 0)
go_down  = (1, 0)
go_right = (0, 1)
str_dir = "left up down right".split(' ')
dir_coord = [go_left, go_up, go_down, go_right]
            # L U D R

tiles = { 
    "|": [None, go_up, go_down, None],
    "-": [go_left, None, None, go_right],
    "L": [go_up, None, go_right, None],
    "7": [None, go_left, None, go_down],
    "J": [None, None, go_left, go_up],
    "F": [go_down, go_right, None, None ],
    ".": [None, None, None, None],
    "S": [],
}

def main():
    if (len(sys.argv) != 2): 
        print(f"Usage {sys.argv[0]} <filename>")
        return;
    part1(sys.argv[1])
    part2(sys.argv[1])

def part1(filename: str):
    with open(filename, "r") as f:
        grid = []
        rowno = 0
        S_coords = [-1, -1]
        while( line:=f.readline().strip()):
            grid.append([*line])
            if ((colno := line.find("S")) != -1): 
                S_coords = [rowno, colno]
            rowno += 1

        curr_dir = get_first_direction(grid, S_coords)
        curr_coords = S_coords
        n_steps = 1
        while ( (curr_coords := step(curr_coords,curr_dir))!=S_coords):
            n_steps += 1
            curr_dir = get_new_direction(grid, curr_coords, curr_dir)

        print("Part 1: ", n_steps//2)

def part2(filename: str):
    with open(filename, "r") as f:
        grid = []
        rowno = 0
        S_coords = [-1, -1]
        while( line:=f.readline().strip()):
            grid.append([*line])
            if ((colno := line.find("S")) != -1): 
                S_coords = [rowno, colno]
            rowno += 1

        xgrid = [[col for col in row] for row in grid]
        xxgrid = [[col for col in row] for row in grid]
        curr_dir = get_first_direction(grid, S_coords)
        curr_coords = S_coords
        n_steps = 1
        while ( (curr_coords := step(curr_coords,curr_dir))!=S_coords):
            n_steps += 1
            curr_dir = get_new_direction(grid, curr_coords, curr_dir)
            char = at(grid, curr_coords)
            xgrid[curr_coords[0]][curr_coords[1]]= char if char in "|-" else "/" if char in "JF" else "\\" if char in "7L" else "¶"
            xxgrid[curr_coords[0]][curr_coords[1]]= "x"

        xgrid[S_coords[0]][S_coords[1]]= replaceS(grid, S_coords)
        xxgrid[S_coords[0]][S_coords[1]]= "x"

        counter = 0
        for i in range(len(xgrid)): 
            for j in range(len(xgrid[0])): 
                if xxgrid[i][j] != 'x':
                    if is_inner(xgrid, xxgrid, i, j):
                        counter +=1

        print("Part 2: ", counter)


def is_inner(xgrid, xxgrid, i, j):
    nxs = False
    dists = [j, i, len(xgrid)-i, len(xgrid[0])-j]
    # Go in the direction shortest to the end
    direction = dists.index(min(dists))
    curr_coords = [i, j]
    squeezing = False
    while( is_valid(curr_coords := step(curr_coords, direction), xgrid) ) :
        if at(xxgrid, curr_coords) != 'x':
            continue
        if at(xgrid, curr_coords) == "|":
            if direction in [0, 3]:
                nxs= not nxs
        if at(xgrid, curr_coords) == "-":
            if direction in [1, 2]:
                nxs= not nxs

        if at(xgrid, curr_coords) == "/":
            if squeezing == "/":
                nxs= not nxs
                squeezing = False
            elif squeezing == "\\":
                squeezing = False
            else: 
                squeezing = "/"
        if at(xgrid, curr_coords) == "\\":
            if squeezing == "\\":
                nxs= not nxs
                squeezing = False
            elif squeezing == "/":
                squeezing = False
            else: 
                squeezing = "\\"

    return nxs

def replaceS(grid, S_coords):
    newdirs = set()
    for cur_dir in range(4):
        newcoord = step(S_coords, cur_dir) 
        char = at(grid, newcoord)
        if is_valid(newcoord, grid):
            if tiles[char][cur_dir]:
                newdirs.add(cur_dir)
    if (newdirs in [{3,1}, {2, 0}]):
        return "\\"
    if (newdirs in [{0,1}, {2, 3}]):
        return "/"
    if (newdirs in [{0, 3}]):
        return "-"
    if (newdirs in [{1,2}]):
        return "|"
    return "S"
     


def get_first_direction(grid, S_coords):
    for cur_dir in range(4):
        newcoord = step(S_coords, cur_dir) 
        if is_valid(newcoord, grid):
            if new_dir := get_new_direction(grid, newcoord, cur_dir):
                return new_dir


def get_new_direction(grid, coord, cur_dir):
    char = at(grid, coord)
    if dcoord:=tiles[char][cur_dir]:
        return dir_coord2dir(dcoord)

def step(coords, direction):
    return [S + G for S, G in zip(coords, dir_coord[direction])]

def at(grid, coord):
    return grid[coord[0]][coord[1]]
                
def dir_coord2dir(direction):
    for i in range(4):
        if (direction == dir_coord[i]):
            return i
    return -1
        
def is_valid(coord, grid):
    return coord[0] in range(0, len(grid)) and coord[1] in range(0, len(grid[0]))



if __name__ == '__main__':
    main()
