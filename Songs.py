import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import json
import twitter

#Program made by Clint Regeon
#This small program looks up data for one of my songs from a spreadsheet and posts about it on Twitter. 

#Gets the google credentials needed to access the spread sheet. 
#Fought with this thing for a while and got a secure scope that works.
scope = ['https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('d:/Programming Projects/Songs/google_secret.json', scope)
client = gspread.authorize(creds)

#Gets the data for a random song from the spreadsheet
sheet = client.open('Songs').sheet1
songs = sheet.get_all_records()
rand_song = random.sample(songs, 1)

#Gets the twitter credentials needed to post to my twitter account
keys = json.load(open('d:/Programming Projects/Songs/twitter_secret.json'))
twitter_api = twitter.Api(consumer_key=keys.get("consumer_key"),
                          consumer_secret=keys.get("consumer_secret"),
                          access_token_key=keys.get("access_token"),
                          access_token_secret=keys.get("access_secret"))

#Writes the tweet that needs to be sent using the random song's details, then posts it.
status = "Hey! You should check out my song \"" + rand_song[0].get("Song Name") + "\" here: " + rand_song[0].get("Link") + " Thanks for listening to @B_o_y_infinite! #free #beats #instrumentals"
post_update = twitter_api.PostUpdate(status=status)
print(post_update)