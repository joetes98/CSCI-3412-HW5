import collections
import re

words = re.findall(r'\w+', open('dictionary.txt').read().lower())
print(collections.Counter(words).most_common(10))