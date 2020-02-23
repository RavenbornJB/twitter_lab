# Testing material

from __future__ import print_function
import twitter

tokens = {
'CONSUMER_KEY': 'OQq7hDIBr6i9sCLS1GxgpjWfW',
'CONSUMER_SECRET': 'GI7Aezf2c5rBXs3Bcf3OAHj5JIYsGK5j6ybtNv2cpSDb1rxqgs',
'ACCESS_TOKEN': '4853080863-S42xdY4GLTqSCIFypVI5KEjdPRkgFHaKwWoPnJ3',
'ACCESS_TOKEN_SECRET': 'ZIWuNQGIB0NjepOqllfuYU0oUo2CQtg8F2RrrNEW5WeDV',
'USER_ID': '4853080863'}

def get_locations(uid='', name=''):
    api = twitter.Api(consumer_key=tokens['CONSUMER_KEY'],
                      consumer_secret=tokens['CONSUMER_SECRET'],
                      access_token_key=tokens['ACCESS_TOKEN'],
                      access_token_secret=tokens['ACCESS_TOKEN_SECRET'])

    users = api.GetFriends(user_id=uid, screen_name=name)
    return [(u.location, u.screen_name) for u in users]


if __name__ == "__main__":
    locs = get_locations(uid=1230067977699184641, name = 'androy777')