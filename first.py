import os
import json
import facebook

def getTokenFromFile(fileName):
  with open(fileName ,encoding='utf-8') as fp:
    return fp.readline()


if __name__ == '__main__':
  #token=os.environ.get('FACEBOOK_TEMP_TOKEN')
  token=getTokenFromFile("my_token.txt")
  graph=facebook.GraphAPI(token)

  profile=graph.get_object('me',fields='name,location{location},likes,friends')
  print(json.dumps(profile, indent=4))

while true:
  try:
    with open("uzair.jsonl","a") as p:
      for post in posts["data"]:
        f.write(json.dumps(post)+"/n")
    posts=requests.get
  except keyError:
    break