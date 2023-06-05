import nltk
with open("token.txt") as f:
    for x in f.readlines():
        tokens = nltk.word_tokenize(x)
        #print(tokens)
        print(x)