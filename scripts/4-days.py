import tweepy
import os
import api

auth = tweepy.OAuthHandler(api.consumerKey, api.consumerSecret)
auth.set_access_token(api.accessKey, api.accessSecret)
api = tweepy.API(auth)
print('Connected to APIs')

print('DATE - 11th September')
image = '/root/countdown/images/4-days.png'
print('Uploading image...')
media = api.media_upload(image)

tweet = "Four days until the #AppleEvent!"

for attempt in range(5):
    try:
        api.update_status(status=tweet, media_ids=[media.media_id])
        print('TWEETED:', tweet)
        break
    except:
        print('Error tweeting')
        continue