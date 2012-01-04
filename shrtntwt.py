import tweepy
import re

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
print 'status: '
raw = raw_input()
raw = raw.lower()

pattern = {
    'a':    'a',
    'see':  'c',
    'i':    'i',
    'are':  'r',
    'you':  'u',
    'to':   '2',
    'for':  '4',
    'no':   'no',
    'love': '<3',
}
hinge = {
    'is':   "'s",
    'am':   "'m",
}

word_token = re.split('\W+|\.', raw)
out = ''
for w in word_token:
    if w in pattern:
        out += pattern[w]
    elif w in hinge:
        if len(out) > 0:
            out = out[:-1]
        out += hinge[w]
    else:
        out += re.sub('a|e|i|o|u', '', w)
    out += ' '

out = out[:-1]
print out
print ''
if len(out) > 140:
    print 'invalid, tweet longer than 140char.'
else:
    print 'tweet sent!'
    # api.update_status(out)

# how to?
# fetch_request_token(???)
# fetch_access_token(???)
