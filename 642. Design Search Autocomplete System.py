# 642. Design Search Autocomplete System
# https://leetcode.com/problems/design-search-autocomplete-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOS = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.EOS = True
    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []

            node = node.children[char]
        
        return self.getAllSentences(node, prefix)
    
    def getAllSentences(self, node, prefix):
        result = [prefix] if node.EOS else []
        for char, child in node.children.items():
            result += self.getAllSentences(child, prefix + char)

        return result
            

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.times = collections.defaultdict(int)
        self.buffer = ''

        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence)
            self.times[sentence] = times[i]
        

    def input(self, c: str) -> List[str]:
        # memorize c, when c == '#', update times & tire
        if c == '#':
            self.trie.insert(self.buffer)
            self.times[self.buffer] += 1
            self.buffer = ''
            return

        self.buffer += c

        results = self.trie.search(self.buffer)
        topResults = sorted(results, key=self.hotSortAlgo)
        atMostThreeTopResults = topResults[:3]

        return atMostThreeTopResults
    
    def hotSortAlgo(self, word):
        # (1) larget times, (2) lower ascii
        return chr(255 - self.times[word]) + word
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
