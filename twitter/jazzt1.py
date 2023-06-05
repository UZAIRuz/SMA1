import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
     consumer_key = '4w6mCEqn1e9wYrhNZ16b87kLd  '
     consumer_secret = "Ph92BElqZX716ShBgojpjz7Y0okbMPezGxp379dBOzBlyr5Gfi "
     access_token = "1654735479886184448-cF1gM1bCO6TZr3Pn8mv82F6wbolU55"
     access_secret = "J8biHFLZyz8CKkTfg3jOAJmbrcpiNjKgfEUkU4aSEciQS "

    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    print("Auth: ", auth)
    print("Client: ", client)
    return client
# return goes to the functuo it self in which it has been written
get_twitter_client()