import numpy as np
import domain.sudoku as Sudoku
from resolvers.resolver import Resolver

class ColumnResolver(Resolver):
    def resolve(self, s: Sudoku):
        for i in range(s.len):
            col = s.puzzle[:, i]

            zeros = [x for x in range(s.len) if col[x] == 0]
            digits = [x for x in col if x != 0]

            for zero in zeros:
                for res in range(s.len):
                    if s.resolution[zero][i][res] in digits:
                        s.resolution[zero][i][res] = 0
