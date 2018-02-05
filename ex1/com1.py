import re
import tweepy
import wget
import urllib 
import os

import requests


#Twitter API credentials
consumer_key = "uSaUtFQs3UNEQBIBPu1lhiSBO"
consumer_secret = "JKOgEDwrsAlCM71Lf2UTaR8ID4c12AMmSPJtj9EwTxPySwZrdP"
access_key = "920759201663803393-Ionn5JJjejdcAYBaeM9kfy7QVOQaIp4"
access_secret = "uIz5FrBovzM1NJa7zl2qNXUyUUXFH6LHDzSK7kpr9GPgg"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    media_files = set()
    for status in alltweets :
        media = status.extended_entities.get('media', [])
        # print (media[0])
        if(len(media) > 0):
            for i in range(len(media)):
             media_files.add(media[i]['media_url'])

    for media_file in media_files:

        print(media_file)
        wget.download(media_file)


   
    os.system(" ffmpeg -framerate 1 -pattern_type glob -i '*.jpg'     -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4")


        
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@LiyiCao")

