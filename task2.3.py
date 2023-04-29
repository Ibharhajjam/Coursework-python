# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:12:17 2023

@author: dell
"""

class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solution = None

    def solve(self, hint=None):
        self.solution = self.backtrack(hint)

    def backtrack(self, hint=None):
        row, col = self.find_empty()

        if row is None:
            return self.puzzle

        if hint is not None and len(hint) > 0:
            num = hint.pop(0)
            if self.is_valid(row, col, num):
                self.puzzle[row][col] = num
                result = self.backtrack(hint)
                if result is not None:
                    return result
                self.puzzle[row][col] = 0
            hint.insert(0, num)
        else:
            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    self.puzzle[row][col] = num
                    result = self.backtrack(hint)
                    if result is not None:
                        return result
                    self.puzzle[row][col] = 0

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    return row, col
        return None, None

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False

        square_row = (row // 3) * 3
        square_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.puzzle[square_row + i][square_col + j] == num:
                    return False

        return True
