# Ported by me from Nathan Ang's C++ solver
# https://github.com/nathan-149/WordHunt-Solver/blob/master/wordhunt_solver.cpp
# https://medium.com/@nathan_149/never-lose-in-wordhunt-again-with-computer-science-bb09ad5015ee

from Trie import Trie
import pickle

class Solver:
    
    def __init__(self):
        with open("Solver/Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)

    def __recurse(self, row, col, word, path, board, visited, ans):
        if row < 0 or row >= 4 or col < 0 or col >= 4:
            return ans
        if visited[row][col]:
            return ans
        
        letter = board[row][col]
        word = word + letter
        searchOut = self.tr.search(word)
        if len(searchOut) == 0:
            return ans
        visited[row][col] = True
        
        
        
    def solve(self, boardString):
        try:
            if len(boardString) != 16:
                return ["Invalid board string"]
        except TypeError:
            return ["Invalid input type"]

        ans = []
        board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                board[i].append(boardString[i*4+j])

        for i in range(4):
            for j in range(4):
                ans = self.__recurse(i, j, "", [(i,j)], board, [[False] * 4] * 4, ans)

