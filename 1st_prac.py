import os
import json
import facebook
import requests

def tokenn(file):
    with open(file,encoding="utf-8") as f:
        return f.readline()

if __name__=="__main__":
    token=tokenn("my_token.txt")
    graph=facebook.GraphAPI(token)
    profile=graph.get_object("me")
    friends1=graph.get_connections('me',"posts")
    print(json.dumps(friends1,indent=4))

while(True):
    try:
        with open("uu.jsonl",'a') as l:
            for post in friends1['data']:
                l.write(json.dumps(post)+"\n")
            posts=requests.get(friends1["paging"]['next']).json()
    except KeyError:
        break


