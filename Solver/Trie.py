import pickle
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False

# create a Trie class
class Trie:
    def __init__(self):
        self.root = TrieNode("") # root doesn't have a character

    def insert(self, word):
        node = self.root
        for char in word:
            
            if char in node.children:
                node = node.children[char]
            
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def dfs(self, node, pre):
 
       if node.is_end:
           self.output.append((pre + node.char))
        
       for child in node.children.values():
           self.dfs(child, pre + node.char)

    def search(self, x):
        
        node = self.root
         
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
               
                return []
         
        self.output = []
        self.dfs(node, x[:-1])
 
        return self.output

def serializeTrie():
    tr = Trie()

    with open("./Data/words_alpha.txt") as readfile:
        for word in readfile:
            tr.insert(word.strip())

    with open("./Data/trie.pickle", "wb") as writefile:
        pickle.dump(tr, writefile)