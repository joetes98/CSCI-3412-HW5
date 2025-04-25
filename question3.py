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


def spellChecker(words, wordsDict, total, max_distance, min_length):
    for i in words:
        if i not in wordsDict: # check whether word is misspelt     
            distances = {}

            for j in wordsDict:
                if len(j) >= min_length: # check minimum word length
                    # compute edit distance for each word in dictionary
                    if edit_distance(i,j) <= max_distance: # only add to suggestions if less than equal to the max edit distance
                        distances[j] = (edit_distance(i,j), wordsDict[j])
        
            # output the suggestions
            suggestions = dict(sorted(distances.items(), key=lambda x: (x[1][0], -x[1][1]))[:total])
            print(f"Suggestions for '{i}': {suggestions}")


def main():

    misspelled = re.findall(r'\w+', open('misspelled.txt').read().lower())
    dictionaryCount = dict(collections.Counter(re.findall(r'\w+', open('dictionary.txt').read().lower())))
    spellChecker(misspelled, dictionaryCount, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

if __name__ =='__main__':
    main()