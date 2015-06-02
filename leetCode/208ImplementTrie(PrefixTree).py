class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.symbol = ''
        self.child = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if len(word) == 0:
            return
            
        tmpRoot, tag = self.root, True
        for i in range(len(word)):
            if word[i] in tmpRoot.child and tag:
                if i == len(word)-1:
                    tmpRoot.child[word[i]].symbol = word
                tmpRoot = tmpRoot.child[word[i]]
            else:
                tag = False
                newTrieNode = TrieNode()
                if i == len(word)-1:
                    newTrieNode.symbol = word
                tmpRoot.child[word[i]] = newTrieNode
                tmpRoot  = newTrieNode



    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        tmpRoot = self.root
        for i in range(len(word)):
            if word[i] in tmpRoot.child:
                tmpRoot = tmpRoot.child[word[i]]
            else:
                return False
        if tmpRoot.symbol == word:
            return True
        else:
            return False
        
        
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        tmpRoot = self.root
        if len(prefix) == 0:
            return True
        for i in range(len(prefix)):
            if prefix[i] in tmpRoot.child:
                tmpRoot = tmpRoot.child[prefix[i]]
            else:
                return False
        return True
        
        
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("a")
trie.insert("abc")
trie.insert("ab")
print trie.search("a")
print trie.search("ab")
print trie.startsWith("a")