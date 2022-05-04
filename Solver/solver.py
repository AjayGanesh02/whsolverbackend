# Ported by me from Nathan Ang's C++ solver
# https://github.com/nathan-149/WordHunt-Solver/blob/master/wordhunt_solver.cpp
# https://medium.com/@nathan_149/never-lose-in-wordhunt-again-with-computer-science-bb09ad5015ee

from trie import Trie
import pickle

class Solver:
    tr = Trie()
    def __init__(self):
        with open("./Data/trie.pickle", "rb") as readfile:
            self.tr = pickle.load(readfile)

    def __recurse(self, row, col, word, path, board, visited, ans):
        # print(path)
        if row < 0 or row >= 4 or col < 0 or col >= 4:
            return ans
        if visited[row][col]:
            return ans
        
        letter = board[row][col]
        word = word + letter
        searchOut = self.tr.search(word)
        if len(searchOut) == 0:
            return ans
        if len(word) > 3 and word in searchOut:
            print("word found, ", word) 
            # ans[word] = path
            
        visited[row][col] = True

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
            if newRow >= 0 and newRow < 4 and newCol >= 0 and newCol < 4:
                path.append((newRow, newCol))
                ans = self.__recurse(newRow, newCol, word, path, board, visited, ans)

        visited[row][col] = False
        
    def __get_len(key):
        return len(key[0])
    
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
                ans = self.__recurse(i, j, "", [(i,j)], board, [[False] * 4] * 4, {})

        return ans


