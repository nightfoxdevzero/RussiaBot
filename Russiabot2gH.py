
import tweepy
import YazikBotKeys
import os
import pandas
import random

df = pandas.read_csv('/Filepath/YazikBot_Repository_Clean.csv')

def printer(x):
    print ('entry used is number: '+str(x))
    if df.at[x,'level'] == 'nan':
        print ('Today\'s word: ' + str(df.at[x,'bare']) + '\n' + 'usage: ' + str(df.at[x,'usage_en']) + ' ' + 'no level found')
        string = str(('Today\'s word: ' +  '\'' + str(df.at[x,'bare']) + '\'' + '\n' + 'Usage: ' + str(df.at[x,'usage_en']) + '\n' + '\n' + '#Russian #Python #tweepy #learnpython #pythonprogramming'))
        return string
    else:
        print ('Today\'s word: ' + str(df.at[x,'bare']) + '\n' + 'usage: ' + str(df.at[x,'usage_en']) + ' ' + 'Difficulty lvl: ' + str(df.at[x, 'level']))
        string = str(('Today\'s word: ' +  '\'' + str(df.at[x,'bare']) + '\'' + '\n' + 'Usage: ' + str(df.at[x,'usage_en']) + '\n' + 'Difficulty lvl: ' + str(df.at[x, 'level']) + '\n' + '#Russian #Python #tweepy #learnpython #pythonprogramming'))
        return string

def listFunction():
    total_items_in_df = len(df.index)
    listofpossibleitemsinit = list(range(0,total_items_in_df))
    if os.path.exists("usedentries.txt"):
        with open("usedentries.txt", "r") as file:
            useditemsfromfile = file.read()
            usedListraw = list(useditemsfromfile.split(','))
            print(usedListraw)
            for items in usedListraw:
                if items in listofpossibleitemsinit:
                    listofpossibleitemsinit.remove(items)
                else: 
                    pass
                
            with open("usedentries.txt", "a") as file:
                x = random.choice(listofpossibleitemsinit)
                file.write(str(x)+ ',')
        return x
    else:
        with open("usedentries.txt","w") as file:
            x = random.choice(listofpossibleitemsinit)
            file.write((str(x))+ ',')
            return x

consumer_key = YazikBotKeys.twitterKeysYazikBot.get('API Key') 
consumer_secret = YazikBotKeys.twitterKeysYazikBot.get('API Key Secret')
access_token = YazikBotKeys.twitterKeysYazikBot.get('Access Token') 
access_token_secret = YazikBotKeys.twitterKeysYazikBot.get('Access Token Secret')



#Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text=str(printer(listFunction())))