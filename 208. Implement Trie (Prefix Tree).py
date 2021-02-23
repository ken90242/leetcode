# 208. Implement Trie (Prefix Tree).py
# https://leetcode.com/problems/implement-trie-prefix-tree/

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.wordEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, w in enumerate(word):
            if w not in node.children:
                node.children[w] = TrieNode()

            node = node.children[w]

        node.wordEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        
        return node.wordEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        
        return True
