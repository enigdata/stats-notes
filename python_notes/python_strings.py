import requests

url = "http://www.gutenberg.org/cache/epub/12/pg12.txt"
res = requests.get(url)
text = res.text

with open('looking_glass.txt', 'w') as f:
    f.write(str(text))

start = text.find('JABBERWOCKY')

text[start:start+2000]

end = text.find('It seems very pretty', start)
poem = text[start:end]

poem.count('the')

print(poem.replace('the', 'XXX'))

poem = poem.lower()

import string 

string.punctuation

poem = poem.translate(dict.fromkeys(map(ord, string.punctuation)))

words = poem.split()
words[:10]

def is_palindrome(word):
    return word == word[::-1]

{word for word in words if is_palindrome(word)}

##### Top 10 most frequent words
import collections

counter = collections.Counter(words) #this is a dictionary

top_10 = counter.most_common(10)

# [('the', 19),
#  ('and', 14),
#  ('he', 7),
#  ('in', 6),
#  ('my', 3),
#  ('through', 3),
#  ('jabberwock', 3),
#  ('gyre', 2),
#  ('mimsy', 2),
#  ('mome', 2)]

#### words that appear exactly twice
[(k,v) for (k,v) in counter.items() if v==2]

list(zip(words[:], words[1:], words[2:]))[:10]

import itertools

def window(x, n):
    '''
    Sliding window of size n from iterable x.
    '''
    s = (itertools.islice(x, i, None) for i in range(n))
    return zip(*s)

print(list(window(words, 5))[:5])



