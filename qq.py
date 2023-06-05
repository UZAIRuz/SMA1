import requests
import json
params={'access_token':'EAAR9O6bDkEcBAF8i6bK4Vy6hdCuETgZAlz4HUqRK85ZBE6pwUoEUAhPPrFGw8O321gHREm3SIiq1IDB7geYMSP0ZBjdZBZAc0lK9YVC96F360CsJO4YczWy5ZBm2UFFJWgyuaeOzMZAQP6x1dsGqYwBumYWLc2KUmLnxcmtThgZBV30szZAP5D8DNHuWZBz1zpTcuq27zzWMvhAIsLGsYwnsKZBvdKBnnZAq5p91UWJfUiLVfvMUjEZA5KJzr'}
page_url='https://graph.facebook.com/v2.8/google/feed?/fields=id , message , reactions , shares .summary(true)'
posts=requests.get(page_url,params=params)
posts=posts.json()
for element in posts ['posts']:
    print(element['message'])
