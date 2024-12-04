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
    xmasarr = []
    nxmas = 0
    with open(filename, "r") as f:
        while line := f.readline().strip():
            xmasarr.append(list(line))

    # Check horizontal
    for i in range(len(xmasarr)):
        buff = []
        for j in range(len(xmasarr[0])):
            buff.append(xmasarr[i][j])
            if len(buff) > 4:
                buff = buff[1:]
            if "".join(buff) in ["XMAS", "SAMX"]: 
                nxmas += 1


    for j in range(len(xmasarr[0])):
        buff = []
        for i in range(len(xmasarr)):
            buff.append(xmasarr[i][j])
            if len(buff) > 4:
                buff = buff[1:]
            if "".join(buff) in ["XMAS", "SAMX"]: 
                nxmas += 1
    
    # check positive diagonal
    for i in range(len(xmasarr) - 3):
        for j in range(len(xmasarr[0]) - 3):
            buff = []
            for b in range(4):
                buff.append(xmasarr[i+b][j+b])
            if "".join(buff) in ["XMAS", "SAMX"]: 
                nxmas += 1

    # check negative diagonal
    for i in range(len(xmasarr) - 3):
        for j in range(len(xmasarr[0])-3):
            buff = []
            for b in range(4):
                buff.append(xmasarr[i+b][j+3-b])
            if "".join(buff) in ["XMAS", "SAMX"]: 
                nxmas += 1

    print(nxmas)

def part2(filename: str):
    xmasarr = []
    nxmas = 0
    with open(filename, "r") as f:
        while line := f.readline().strip():
            xmasarr.append(list(line))
    
    # Get convolution window
    for i in range(len(xmasarr) - 2):
        for j in range(len(xmasarr[0]) - 2):
            buff = []
            for b in range(3):
                buff.append(xmasarr[i+b][j:j+3])
            # Check positive diagonal
            posbuff = []
            for k in range(3):
                posbuff.append(buff[k][k])
            # Check negative diagonal
            negbuff = []
            for k in range(3):
                negbuff.append(buff[k][2-k])

            if "".join(posbuff) in ["MAS", "SAM"] and "".join(negbuff) in ["MAS", "SAM"]:
                nxmas += 1

    print(nxmas)


if __name__ == "__main__":
    main()
