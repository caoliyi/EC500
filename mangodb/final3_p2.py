import re
import tweepy
import wget
import urllib 
import os
import requests
import io
from tweepy import OAuthHandler
import subprocess
import sys
from PIL import Image
import time

# Imports the Google Cloud client library
from google.cloud import vision

from google.cloud.vision import types
from os import listdir
from pymongo import MongoClient
import pprint
import bson



#Twitter API credentials
consumer_key = 
consumer_secret = 
access_key = 
access_secret = 


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
    data = {}
    data['info'] = []
    data['info'].append({
        'name': screen_name
        })
    media_files = set()
    for status in alltweets :
        try :
            media = status.extended_entities.get('media', [])
        except :
            media = status.entities.get('mdeia',[])
        # print (media[0])
        if(len(media) > 0):
            for i in range(len(media)):
             media_files.add(media[i]['media_url'])
    # mm = 1
    for media_file in media_files:
    #     data['info'].append({
    #         'picture ' + str(m): media_file
    #         })
    #     mm = mm + 1
        print(media_file)
        wget.download(media_file)
    
    os.system("ffmpeg -framerate 1 -pattern_type glob -i '*.jpg'  -c:v libx264 -r 30 -pix_fmt yuv420p out1.mp4")
    os.system("ffmpeg -framerate 1 -pattern_type glob -i '*.png' -c:v libx264 -r 30 -pix_fmt yuv420p  out2.mp4")



    

   # for google vision
    client = vision.ImageAnnotatorClient()
    file = open("label.txt","w")

    
    point = 0
    numlist = '0123456789'
    OBJ = [pic for pic in listdir(".") if pic.endswith('jpg') or pic.endswith('png')]
    # print(OBJ)
    for i in OBJ:
        file_name = os.path.join(os.path.dirname(__file__),i)
        
        
        ttt = 1            
        new_name = numlist[point] +'.jpg'
        data['info'].append({
            'picture ' + str(ttt): i
            })
         
        os.renames(file_name,new_name)
             
        print(file_name)
        print("changed down")
        point = point + 1
    # Loads the image into memory
        with io.open(new_name, 'rb') as image_file:
             content = image_file.read()
       
        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
       
        file.write('Lables for  '+new_name+'  :\n')
       
        
        label_list = []
        for label in labels:
           label_list.append(label.description)
           file.write(label.description+'\n')
        
        data['info'].append({
            'description ' + str(ttt):label_list 
            })   
        ttt += 1
    file.close()
    print(data)
    client = MongoClient()
    db = client.picture.database
    collection = db.picture_collection

    posts = db.posts
    posts.insert_one(data)
            
if __name__ == '__main__':
  
    #pass in the username of the account you want to download
    get_all_tweets("@LiyiCao")

