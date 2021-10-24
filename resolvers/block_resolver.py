import math 
import numpy as np
import domain.sudoku as Sudoku
from resolvers.resolver import Resolver

class BlockResolver(Resolver):
    def resolve(self, s: Sudoku):
        sqrt = int(math.sqrt(s.len))
        for r in range(sqrt):
            for c in range(sqrt):
                arr = []
                for br in range(sqrt):
                    for bc in range(sqrt):
                        arr.append(s.puzzle[r*sqrt+br][c*sqrt+bc])

                zeros = [x for x in range(s.len) if arr[x] == 0]
                digits = [x for x in arr if x != 0]

                for zero in zeros:
                    for res in range(s.len):
                        if s.resolution[int(r*sqrt+zero/sqrt)][c*sqrt+zero%sqrt][res] in digits:
                            s.resolution[int(r*sqrt+zero/sqrt)][c*sqrt+zero%sqrt][res] = 0
