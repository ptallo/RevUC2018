import tweepy

def initApi():
    # Authorization keys
    consumer_key = "0j5zlz4h5IQ71ncz8ZsrpTEMc"
    consumer_secret = "zJpRVvpMGI13c1MnDrzAKC6fwIIpoUJa25YAFAV4B9aovKDdwe"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located
    # under "Your access token")
    access_token = "969676143853998080-MZ7ivjmYzbWLq0SPlhWFCqe3nP6Fsgg"
    access_token_secret = "8T56Wh5JURMbKRDHUOG6COLhoI4KezQg8rwO9CPYH1Jws"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # If the authentication was successful, you should
    # see the name of the account print out
    print(api.me().name)

    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    # api.update_status(status='WE are in the twittersphere!')

    # get the url
    try:
        redirect_url = auth.get_authorization_url()
        print('Success! Got request token.')
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

    return api




