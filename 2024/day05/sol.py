#! /usr/bin/env python
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <filename>")
        return
    part1(sys.argv[1])
    part2(sys.argv[1])


def part1(filename: str):
    score = 0
    with open(filename, "r") as f:
        # Get ordering
        disallowed_ahead = {}
        while line := f.readline().strip():
            first, last = line.split("|") 
            disallowed_ahead.setdefault(int(last), set()).add(int(first))

        # Get updates
        while line := f.readline().strip():
            updates = [int(el) for el in line.split(',')]
            middle_element = updates[int(len(updates)/2)] # Assume odd number of elements
            for idx, el in enumerate(updates[:-1]):
                disallowed_for_current_element = disallowed_ahead.get(el, set())
                ahead = updates[idx+1:]
                any_disallowed_ahead = disallowed_for_current_element.intersection(set(ahead))
                if any_disallowed_ahead:
                    break
            else: # When the for loop does not break
                score += middle_element
            
    print("PART 1: ", score)


def part2(filename: str):
    score = 0
    with open(filename, "r") as f:
        sortrules = []
        while line := f.readline().strip():
            first, last = line.split("|") 
            sortrules.append([int(first), int(last)])
        while line := f.readline().strip():
            updates = [int(el) for el in line.split(',')]
            thissortrules = [sortrule for sortrule in sortrules if sortrule[0] in updates]
            thissortrules_input = ""
            for rule in thissortrules:
                thissortrules_input += f"{rule[0]} {rule[1]}\n"
            process = subprocess.run(["tsort"], input=thissortrules_input, text=True, capture_output=True)
            sortorder = [int(i) for i in process.stdout.split("\n") if i]

            updates_sorted=sorted(updates, key=lambda x: sortorder.index(x)) 
            if updates_sorted != updates:
                middle_element = updates_sorted[int(len(updates_sorted)/2)] 
                score += middle_element
    print("PART 2: ", score)
        
            

if __name__ == "__main__":
    main()
