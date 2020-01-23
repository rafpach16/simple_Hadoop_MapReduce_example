#!/usr/bin/env python
import string,  sys

from sklearn.feature_extraction import stop_words

stops = set(stop_words.ENGLISH_STOP_WORDS)

for line in sys.stdin:
    ## removes the whitespace
    line = line.strip()

    ## removes punctuation
    line = line.translate( string.maketrans(string.punctuation, ' ' * len(string.punctuation)) )

    ## makes sure that the text is a valid Unicode string
    ## ignores the characters that are not valid
 

    ## converts the text to lowercase 
    line = line.lower()

    ## this splits words at all whitespace
    words = line.split()

    ## prints out all the words with a count of 1
    for w in words:
       if w not in stops:
         print '%s\t%s' % (w, "1")


