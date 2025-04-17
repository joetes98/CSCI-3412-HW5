import collections
import re
import sys

# using a dictionary table
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1
    tbl = {}
    for i in range(m): tbl[i,0]=i #initialization
    for j in range(n): tbl[0,j]=j #initialization

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1 # same or replacement
            tbl[i,j] = min(tbl[i,j-1]+1,tbl[i-1,j]+1,tbl[i-1,j-1]+cost)
    
    return tbl[i,j]

def spellChecker(words, wordsDict, total):
    for i in words:
        if i in wordsDict: # check if word is misspelt
            continue
        distances = {}
        for j in wordsDict: # compute edit distance for each word in dictionary
            distances[j] = (edit_distance(i,j), wordsDict[j])
        
        # output the suggestions
        suggestions = dict(sorted(distances.items(), key=lambda item: item[1][0])[:total])
        print(f"Suggestions for '{i}': {suggestions}")


def main():

    dictionary = re.findall(r'\w+', open('dictionary.txt').read().lower())
    misspelled = re.findall(r'\w+', open('misspelled.txt').read().lower())
    dictionaryCount = dict(collections.Counter(dictionary))

    spellChecker(misspelled, dictionaryCount, int(sys.argv[1]))


if __name__ =='__main__':
    main()