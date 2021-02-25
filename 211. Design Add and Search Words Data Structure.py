# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.EndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
        
        node.EndOfWord = True
    
    def searchNode(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                result = any([self.searchNode(word[i + 1:], child) for child in node.children.values()])
                return result
            elif char not in node.children:
                return False
            node = node.children[char]
        
        return node.EndOfWord

    def search(self, word: str) -> bool:
        
        return self.searchNode(word, self.root)
