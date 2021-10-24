import sys
from domain.sudoku import Sudoku

def main():
    args = sys.argv[1:]
    with open(args[0]) as file:
        p = file.readlines()
        p = [line.rstrip() for line in p]
    s = Sudoku(p)
    solved = s.solve()
    if solved:
        print("sudoku solution found for puzzle {}".format(s))
    else:
        print("sudoku solution not found for puzzle {} \n resolution - {}".format(s, s.resolution))

if __name__ == "__main__":
    main()
