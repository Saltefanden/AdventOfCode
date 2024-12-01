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
        list1 = []
        list2 = []
        while( line:=f.readline().strip()):
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
        list1.sort()
        list2.sort()
   
    score = 0
    for a, b in zip(list1, list2):
        score += abs(a-b)

    print(score)

def part2(filename: str):
    with open(filename, "r") as f:
        list1 = []
        list2 = []
        while( line:=f.readline().strip()):
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
        list1.sort()
        list2.sort()
   
    score = 0
    for a in list1:
       count = sum([el == a for el in list2])
       score += a * count
    print(score)

if __name__ == '__main__':
    main()
