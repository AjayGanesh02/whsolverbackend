from Trie import Trie
import pickle

tr = Trie()

with open("Solver/Data/words_alpha.txt") as readfile:
    for word in readfile:
        tr.insert(word.strip())

with open("Solver/Data/trie.pickle", "wb") as writefile:
    pickle.dump(tr, writefile)