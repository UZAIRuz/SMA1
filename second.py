import os
import json
import facebook

def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()
#graph api an object

if __name__=='__main__':
  #token=os.environ.get('FACEBOOK_TEMP_TOKEN')
  token=getTokenFromFile("my_token.txt")
  graph=facebook.GraphAPI(token)
  # there is a  choice for using the user or we can aslo do it without using user
  user=graph.get_object("me")
  friends = graph.get_connections(user["id"],"friends")
  print(json.dumps(friends, indent=4))