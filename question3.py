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

def spellChecker(words, dict):
    suggestions = 0
    for i in words:
        print()


def main():

    print(edit_distance("Hello world!", "HalloWorld")) # returns 4

    dictionary = re.findall(r'\w+', open('dictionary.txt').read().lower())
    misspelled = re.findall(r'\w+', open('misspelled.txt').read().lower())
    dictionaryCount = collections.Counter(dictionary)
    # print(dictionaryCount)
    print(misspelled)

if __name__ =='__main__':
    main()