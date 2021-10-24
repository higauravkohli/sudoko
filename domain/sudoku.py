import numpy as np
from resolvers.column_resolver import ColumnResolver
from resolvers.row_resolver import RowResolver
from resolvers.block_resolver import BlockResolver


class Sudoku:

    resolvers = [
        ColumnResolver(),
        RowResolver(),
        BlockResolver()
    ]

    def __init__(self, puzzle) -> None:
        print("puzzle to solve is {}".format(str(puzzle)))

        self.len = len(puzzle)
        print("received puzzle of len {}".format(self.len))

        self.puzzle = np.array([[0]*self.len for i in range(self.len)])

        vals = [i+1 for i in range(self.len)]
        self.resolution = np.array([[vals]*self.len for i in range(self.len)])

        for r in range(self.len):
            for c in range(self.len):
                val = int(puzzle[r][c])
                self.puzzle[r][c] = val
                if val != 0:
                    self.resolution[r][c] = np.full(9, 0)

        print("sudoku is ready \n{}".format(str(self)))    

    def solve(self) -> bool:
        reiterate = True

        while reiterate:
            reiterate = False
            for resolver in self.resolvers:
                resolver.resolve(self)

            for r in range(self.len):
                for c in range(self.len):
                    vals = np.asarray(np.where(self.resolution[r][c] != 0))[0]

                    if len(vals) == 1:
                        self.puzzle[r][c] = self.resolution[r][c][vals[0]]
                        self.resolution[r][c] = np.full(9, 0)
                        reiterate = True


        return self.solved()

    def solved(self) -> bool:
        return np.all((self.puzzle != 0))

    def __str__(self) -> str:
        return "puzzle \n{}".format(self.puzzle)