import numpy as np
import domain.sudoku as Sudoku
from resolvers.resolver import Resolver

class RowResolver(Resolver):
    def resolve(self, s: Sudoku):
        for i in range(len(s.puzzle)):
            row = s.puzzle[i, :]
            
            zeros = [x for x in range(s.len) if row[x] == 0]
            digits = [x for x in row if x != 0]


            for zero in zeros:
                for res in range(s.len):
                    if s.resolution[i][zero][res] in digits:
                        s.resolution[i][zero][res] = 0
