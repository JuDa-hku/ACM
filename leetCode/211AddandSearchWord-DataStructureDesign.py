class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.symbol = ''
        self.child = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def addWord(self, word):
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

    def search(self, word):
        tmpRoot = self.root
        return searchHelp(tmpRoot, word, 0)


def searchHelp(tmpRoot, word, length):
    if length == len(word):
        return len(tmpRoot.symbol) == len(word)
        
    for i in range(length,len(word),1):
        if word[i] in tmpRoot.child:
            tmpRoot = tmpRoot.child[word[i]]
            if i == len(word)-1:
                return len(tmpRoot.symbol) == len(word)
        elif word[i] == '.':
#            print len(tmpRoot.child.values())
            for node in tmpRoot.child.values():
                if searchHelp(node, word, i+1):
                    return True
            break
        else:
            return False

    return False
                
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("...d")