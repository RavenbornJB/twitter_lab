import twitter
from not_hidden import tokens


def get_locations(name=''):
    api = twitter.Api(consumer_key=tokens['CONSUMER_KEY'],
                      consumer_secret=tokens['CONSUMER_SECRET'],
                      access_token_key=tokens['ACCESS_TOKEN'],
                      access_token_secret=tokens['ACCESS_TOKEN_SECRET'])

    users = api.GetFriends(screen_name=name)
    user = api.GetUser(screen_name=name)
    print(user)
    return [(u.location, u.screen_name) for u in users], user.location


if __name__ == "__main__":
    locs = get_locations(name = 'jb_ravenborn')
