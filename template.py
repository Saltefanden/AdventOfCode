import sys


def main():
    if (len(sys.argv) != 2): 
        print(f"Usage {sys.argv[0]} <filename>")
        return;
    part1(sys.argv[1])
    part2(sys.argv[1])

def part1(filename: str):
    pass


def part2(filename: str):
    pass

if __name__ == '__main__':
    main()
