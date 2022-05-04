# Ported by me from Nathan Ang's C++ solver and CoderSnacks's Boggle Solver
# https://github.com/nathan-149/WordHunt-Solver/blob/master/wordhunt_solver.cpp
# https://medium.com/@nathan_149/never-lose-in-wordhunt-again-with-computer-science-bb09ad5015ee

from trie import Trie
import pickle
import collections

class Solver:
    tr = Trie()
    def __init__(self):
        with open("./Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)

    def __recurse(self, row, col, word, path, board, visited):
        found = {}
        if not self.tr.search(word, True):
            return found
        else:
            if self.tr.search(word):
                found[word] = path
                if len(word) == 16:
                    return found

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
            if newRow >= 0 and newRow < 4 and newCol >= 0 and newCol < 4 and not visited[newRow][newCol]:
                visited[newRow][newCol] = True
                path.append((newRow, newCol))
                word += board[newRow][newCol]
                self.__merge(found, self.__recurse(newRow, newCol, word, path, board, visited))
                visited[row][col] = False
        return found

        
    def __get_len(key):
        return len(key[0])
    
    def __merge(dict1, dict2):
        return(dict1.update(dict2))
    
    def __sort_by_keylen(self, dict):
        dict_list = list(dict.items())
        dict_list.sort(key = self.__get_len)
        res = {ele[0] : ele[1] for ele in dict_list}
        return res

    def solve(self, boardString):
        try:
            if len(boardString) != 16:
                return ["Invalid board string"]
        except TypeError:
            return ["Invalid input type"]

        ans = {}
        board = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                board[i].append(boardString[i*4+j])

        for i in range(4):
            for j in range(4):
                ans = self.__recurse(i, j, "", [(i,j)], board, [[False] * 4] * 4)

        return ans


