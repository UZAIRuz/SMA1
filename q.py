import re
import nltk

def preprocess(text):
    #Basic cleaning
    text=text.strip()
    text=re.sub(r"[^\w\s]","",text)
    text=text.lower()

    #token single comment
    tokens=nltk.word_tokenize(text)
    return(tokens)
a="A story *** is a great way to get* your kids engaged. Probably one of the clearest memories of your childhood is that of the stories you read as a child.Most of the stories of your childhood were probably stories with morals. These are not the kind of stories we see very often these days."
print(preprocess(a))

def get_hashtag(text):
    hashtags=re.findall(r"#(\w+)")