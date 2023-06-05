import nltk
i=0
l=[]
# ,read() makes a whole string damn it
#f = open("token.txt"):
with open("token.txt") as f:
    for x in f.readlines():
      tokens = nltk.word_tokenize(x)
      print(tokens)
"""l.append([])
for d in /f.split():
    l[i].append(d)
i=i+1 """
#split function adds "' adnd then it gets splitted













#with open("token.txt") as f:
   # for line in f.readlines():
        #print(f)
