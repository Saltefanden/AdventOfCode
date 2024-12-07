#! /usr/bin/env python
import itertools
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    score = 0
    with open(filename, "r") as f:
        while line := f.readline().strip():
            answer, inputs = line.split(":")
            inplist = [int(inp) for inp in inputs.split()] 
            answer = int(answer) 
            noperators = len(inplist)-1
            for i in range(2**(noperators)):
                bstring = ''
                number = i
                while number > 0:
                    bstring = str(number % 2) + bstring
                    number //=2
                bstring = bstring if bstring else '0' # Ensure string
                bstring = '0' * (noperators - len(bstring)) + bstring    # Pad string
                result = inplist[0]
                for idx, op in enumerate(bstring):
                    inplist_idx = idx+1
                    if op == "0":
                        result += inplist[inplist_idx]
                    elif op == "1":
                        result *= inplist[inplist_idx]
                    else:
                        print("FUCK A DUCK")
                        exit()
                if result == answer:
                    score += answer
                    break
    print(score) # 1038838357795

                     

                

def part2(filename: str):
    score = 0
    with open(filename, "r") as f:
        while line := f.readline().strip():
            answer, inputs = line.split(":")
            inplist = [int(inp) for inp in inputs.split()] 
            answer = int(answer) 
            noperators = len(inplist)-1
            for i in range(3**(noperators)):
                bstring = ''
                number = i
                while number > 0:
                    bstring = str(number % 3) + bstring
                    number //=3
                bstring = bstring if bstring else '0' # Ensure string
                bstring = '0' * (noperators - len(bstring)) + bstring    # Pad string
                result = inplist[0]
                for idx, op in enumerate(bstring):
                    inplist_idx = idx+1
                    if op == "0":
                        result += inplist[inplist_idx]
                    elif op == "1":
                        result *= inplist[inplist_idx]
                    elif op == "2":
                        result *= 10**len(str(inplist[inplist_idx]))
                        result += inplist[inplist_idx]
                    else:
                        print("FUCK A DUCK")
                        exit()
                if result == answer:
                    score += answer
                    break
    print(score) 


if __name__ == "__main__":
    main()
