# Ported by me from Nathan Ang's C++ solver and CoderSnacks's Boggle Solver
# https://github.com/nathan-149/WordHunt-Solver/blob/master/wordhunt_solver.cpp
# https://medium.com/@nathan_149/never-lose-in-wordhunt-again-with-computer-science-bb09ad5015ee
# https://www.youtube.com/watch?v=FFQ-nbul6VY

from trie import Trie
import pickle
import collections

def get_len(key):
    return len(key[0]) * -1

class Solver:
    tr = Trie()
    def __init__(self):
        with open("./Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)

    def __recurse(self, row, col, word, path, board):
        found = []
        if not self.tr.search(word, True):
            return found
        else:
            if len(word) > 2 and self.tr.search(word):
                found.append(([word], path))

        directions = {
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "LD": (1, -1),
            "RD": (1, 1),
            "LU": (-1, -1),
            "RU": (-1, 1)
        }

        for direction in directions:
            newRow = row + directions[direction][0]
            newCol = col + directions[direction][1]
            if newRow >= 0 and newRow < 4 and newCol >= 0 and newCol < 4 and (newRow, newCol) not in path:
                newpath = path + [(newRow, newCol)]
                newword = word + board[newRow][newCol]
                found += self.__recurse(newRow, newCol, newword, newpath, board)
        return found
    
    def solve(self, boardString):

        #check for invalid boards
        try:
            if len(boardString) != 16:
                return ["Invalid board string"]
            if not boardString.isalnum():
                return ["Invalid board string"]
        except TypeError:
            return ["Invalid input type"]

        #construct board from string
        ans = []
        board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                board[i].append(boardString[i*4+j])

        #perform actual solving using recursive dfs
        for i in range(4):
            for j in range(4):
                visited = [[False for _ in range(4)] for _ in range(4)]
                visited[i][j] = True
                ans += self.__recurse(i, j, board[i][j], [(i,j)], board)

        #filter duplicates and convert list of tuples into a dictionary
        ansdict = {}
        for word,path in ans:
            if word[0] not in ansdict:
                ansdict[word[0]] = path
        
        #sort the dictionary by key length
        dictlist = list(ansdict.items())
        dictlist.sort(key=get_len)

        ansdict = [{"word": ele[0], "path": ele[1]} for ele in dictlist] 

        return ansdict


