import re
import nltk
def preprocess(text):
    #Basic cleaning
    text=text.strip()
    text=re.sub(r'[^\w\s]','',text)
    text=text.lower()

    #token single comment
    tokens=nltk.word_tokenize(text)
    return(tokens)
a=open("token.txt","r")
for i in a:
    b = a.readline()
    print(b)
    print(preprocess(b))
a.close()