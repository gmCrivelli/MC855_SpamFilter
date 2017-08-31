import sys

n_ham = 0
n_spam = 0

spam = {}
ham = {}
stopwords = {"a",  "about",  "above",  "after",  "again",  "against",  "all",  "am",  "an",  "and",  "any",  "are",  "aren't",  "as",  "at",  "be",  "because",  "been",  "before",  "being",  "below",  "between",  "both",  "but",  "by",  "can't",  "cannot",  "could",  "couldn't",  "did",  "didn't",  "do",  "does",  "doesn't",  "doing",  "don't",  "down",  "during",  "each",  "few",  "for",  "from",  "further",  "had",  "hadn't",  "has",  "hasn't",  "have",  "haven't",  "having",  "he",  "he'd",  "he'll",  "he's",  "her",  "here",  "here's",  "hers",  "herself",  "him",  "himself",  "his",  "how",  "how's",  "i",  "i'd",  "i'll",  "i'm",  "i've",  "if",  "in",  "into",  "is",  "isn't",  "it",  "it's",  "its",  "itself",  "let's",  "me",  "more",  "most",  "mustn't",  "my",  "myself",  "no",  "nor",  "not",  "of",  "off",  "on",  "once",  "only",  "or",  "other",  "ought",  "our",  "ours 	ourselves",  "out",  "over",  "own",  "same",  "shan't",  "she",  "she'd",  "she'll",  "she's",  "should",  "shouldn't",  "so",  "some",  "such",  "than",  "that",  "that's",  "the",  "their",  "theirs",  "them",  "themselves",  "then",  "there",  "there's",  "these",  "they",  "they'd",  "they'll",  "they're",  "they've",  "this",  "those",  "through",  "to",  "too",  "u",  "under",  "until",  "up",  "very",  "was",  "wasn't",  "we",  "we'd",  "we'll",  "we're",  "we've",  "were",  "weren't",  "what",  "what's",  "when",  "when's",  "where",  "where's",  "which",  "while",  "who",  "who's",  "whom",  "why",  "why's",  "with",  "won't",  "would",  "wouldn't",  "you",  "you'd",  "you'll",  "you're",  "you've",  "your",  "yours",  "yourself",  "yourselves", ".", ",", "-", "_", "/", ":", "'", "=", "(", "|", "?", ")", "*", "@", ";"}
unique_words = set()
n_unique = 0

# read training data
def readTrain():
	global spam
	global ham
	global n_spam
	global n_ham
	
	f = open("emailset.txt")
	
	# jump first line
	f.readline()
	
	# read spam
	while True:
		line = f.readline()
		line = line.replace('\n','')
		
		if line == "###HAM###\t":
			break
		else:
			(word, count) = line.split("\t")
			spam[word] = int(count)
	
	n_spam = len(spam)
	
	# read ham
	while True:
		line = f.readline()
		line = line.replace('\n','')
		
		if line == "###UNIQUE###\t":
			break
		else:
			(word, count) = line.split("\t")
			ham[word] = int(count)
	
	n_ham = len(ham)
			
	# read unique
	for line in f:
		line = line.replace('\n','')
		unique_words.add(line)

	n_unique = len(unique_words)
	
# return P(word|class)
def condProb(word, c):
	aux = 0
	global len_unique_words
	
	if c == "spam":
		if word in spam:
			aux = float(spam[word])
			
		return (aux + 1.0) / float(n_spam + n_unique)
		
	else:
		if word in ham:
			aux = float(ham[word])
			
		return (aux + 1.0) / float(n_ham + n_unique)
		

# return P(class)
def classProb(c):
	if c == "spam":
		return float(n_spam) / float(n_spam + n_ham)
	else:
		return float(n_ham) / float(n_spam + n_ham)

# return P(word)
def wordProb(word):
	a = 0
	b = 0
	aux = 0
	
	if word in spam:
		a = spam[word]
	else:
		a = 1
		aux += 1
	
	if word in ham:
		b = ham[word]
	else:
		b = 1
		aux += 1
	
	return float(a + b) / float(n_spam + n_ham + aux)


readTrain()
mode = raw_input("Enter the mode (0 for custom input; 1 for input from validation_email.txt):")
mode = int(mode)

if mode == 0:
    # get text from user
    text = raw_input("Enter the text: ")
    text = text.split()
    
    p_spam = 1
    p_ham = 1

    # first we add all words not in the vocabulary to it
    for word in text:
        if word not in stopwords:
            unique_words.add(word.lower())

    len_unique_words = len(unique_words)

    # now we compute the probability stuff
    for word in text:
        if word not in stopwords:
            p_spam *= condProb(word.lower(), "spam")
            p_ham *= condProb(word.lower(), "ham")
            print("P( " + word.lower() + " | SPAM) = " + str(condProb(word.lower(), "spam")))
            print("P( " + word.lower() + " | HAM) = " + str(condProb(word.lower(), "ham")))

    p_spam *= classProb("spam")
    p_ham *= classProb("ham")

    if p_spam > p_ham:
        print("ITS A SPAM!")
    else:
        print("ITS A HAM!")

else:
    input_emails = open("emailcollection.txt")

    correct_spam = 0
    correct_ham = 0
    wrong_spam = 0
    wrong_ham = 0

    spam_count = 0
    ham_count = 0
    
    for line in input_emails:
        # get text from user
        # text = raw_input("Enter the text: ")
        # text = text.split()
        (c, text) = line.split("\t")
        text = text.split()
        
        if c == "ham":
            ham_count += 1
        else:
            spam_count += 1

        p_spam = 1
        p_ham = 1

        # first we add all words not in the vocabulary to it
        for word in text:
            if word not in stopwords:
                unique_words.add(word.lower())

        len_unique_words = len(unique_words)

        # now we compute the probability stuff
        for word in text:
            if word not in stopwords:
                p_spam *= condProb(word.lower(), "spam")
                p_ham *= condProb(word.lower(), "ham")
                # print("P( " + word.lower() + " | SPAM) = " + str(condProb(word.lower(), "spam")))
                # print("P( " + word.lower() + " | HAM) = " + str(condProb(word.lower(), "ham")))

        p_spam *= classProb("spam")
        p_ham *= classProb("ham")

        classification = "ham"
        if p_spam > p_ham:
            classification = "spam"

        print("Original: " + c + " - Classified as: " + classification)

        if classification == "ham":
            if c == classification:
                correct_ham += 1
            else:
                wrong_ham += 1

        if classification == "spam":
            if c == classification:
                correct_spam += 1
            else:
                wrong_spam += 1

    print("Correctly classified as HAM: {} / {}".format(correct_ham, ham_count))
    print("Incorrectly classified as SPAM: {} / {}".format(wrong_spam, ham_count))
    print("Correctly classified as SPAM: {} / {}".format(correct_spam, spam_count))
    print("Incorrectly classified as HAM: {} / {}".format(wrong_ham, spam_count))


    #print("Its a SPAM!")
    #    else:
    #print("Its a HAM!")
