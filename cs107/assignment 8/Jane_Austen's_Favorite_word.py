import urllib
from collections import defaultdict
urls_ALL_JANE='http://www.gutenberg.org/cache/epub/31100/pg31100.txt'


def pullLines(url):
    f= urllib.urlopen(url)
    lines = f.readlines()
    lines = map(lambda line: line.rstrip("\n"), lines)
    f.close()
    return lines

def digestLine(line, wordDict):
    wordList = line.split()
    for word in wordList:
        if  word.islower():
            wordDict[word] += 1

def digestLines(lines, wordDict):
    for line in lines:
        digestLine(line, wordDict)

def digestText(url, wordDict):
    lines = pullLines(url)
    digestLines(lines, wordDict)

def getFavouriateWord(urls):
    wordDict = defaultdict(int)
    for url in urls:
        digestText(url, wordDict)
    favouriateWordNum = 0
    for key in wordDict.keys():
        if wordDict[key]>favouriateWordNum:
            favouriateWordNum = wordDict[key]**len(key)
            favouriateWord = key
    print "Jane Austen's favouriate word is \"%s\". " %favouriateWord

getFavouriateWord([urls_ALL_JANE])


