#!/usr/bin/env python

from operator import itemgetter
import sys

spam = {}
ham = {}
n_spam = 0
n_ham = 0
stopwords = {"a",  "about",  "above",  "after",  "again",  "against",  "all",  "am",  "an",  "and",  "any",  "are",  "aren't",  "as",  "at",  "be",  "because",  "been",  "before",  "being",  "below",  "between",  "both",  "but",  "by",  "can't",  "cannot",  "could",  "couldn't",  "did",  "didn't",  "do",  "does",  "doesn't",  "doing",  "don't",  "down",  "during",  "each",  "few",  "for",  "from",  "further",  "had",  "hadn't",  "has",  "hasn't",  "have",  "haven't",  "having",  "he",  "he'd",  "he'll",  "he's",  "her",  "here",  "here's",  "hers",  "herself",  "him",  "himself",  "his",  "how",  "how's",  "i",  "i'd",  "i'll",  "i'm",  "i've",  "if",  "in",  "into",  "is",  "isn't",  "it",  "it's",  "its",  "itself",  "let's",  "me",  "more",  "most",  "mustn't",  "my",  "myself",  "no",  "nor",  "not",  "of",  "off",  "on",  "once",  "only",  "or",  "other",  "ought",  "our",  "ours 	ourselves",  "out",  "over",  "own",  "same",  "shan't",  "she",  "she'd",  "she'll",  "she's",  "should",  "shouldn't",  "so",  "some",  "such",  "than",  "that",  "that's",  "the",  "their",  "theirs",  "them",  "themselves",  "then",  "there",  "there's",  "these",  "they",  "they'd",  "they'll",  "they're",  "they've",  "this",  "those",  "through",  "to",  "too",  "u",  "under",  "until",  "up",  "very",  "was",  "wasn't",  "we",  "we'd",  "we'll",  "we're",  "we've",  "were",  "weren't",  "what",  "what's",  "when",  "when's",  "where",  "where's",  "which",  "while",  "who",  "who's",  "whom",  "why",  "why's",  "with",  "won't",  "would",  "wouldn't",  "you",  "you'd",  "you'll",  "you're",  "you've",  "your",  "yours",  "yourself",  "yourselves", ".", ",", "-", "_", "/", ":", "'", "=", "(", "|", "?", ")", "*", "@", ";"}
unique_words = set()

import operator

# add word to dictionary
def addWord(c, word):
	global spam
	global ham
	global n_ham
	global n_spam
	
	unique_words.add(word)
	
	if word in stopwords:
		return
		
	if c == "spam":
		n_spam += 1
		
		if word in spam:
			spam[word] += 1
		else:
			spam[word] = 1
	else:
		n_ham += 1
		
		if word in ham:
			ham[word] += 1
		else:
			ham[word] = 1
					
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    (c, word) = line.split('\t')

	# add it to the dictionary
    addWord(c, word)

# print result
sorted_spam = sorted(spam.items(), key=operator.itemgetter(1), reverse = True)
sorted_ham = sorted(ham.items(), key=operator.itemgetter(1), reverse = True)

print("###SPAM###")
for i in range(len(sorted_spam)):
	print(str(sorted_spam[i][0]) + "\t" + str(sorted_spam[i][1]))

print("###HAM###")
for i in range(len(sorted_ham)):
	print(str(sorted_ham[i][0]) + "\t" + str(sorted_ham[i][1]))

print("###UNIQUE###")	
for word in unique_words:
	print(word)

