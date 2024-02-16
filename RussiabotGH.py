
import tweepy
import YazikBotKeys
import os
import pandas
import random

df = pandas.read_csv('filepath/RussianWordsCleanedEnglish.csv')

def printer(x):
    print ('entry used is number: '+str(x))
    print ('word: ' + str(df.at[x,'accented']) + ' ' + 'use in English: ' + str(df.at[x,'usage_en']) + ' ' + 'Difficulty lvl: ' + str(df.at[x, 'level']))
    string = str(('Word: ' +  '\'' + str(df.at[x,'accented']) + '\'' + '\n' + 'English Use: ' + str(df.at[x,'usage_en']) + '\n' + 'Difficulty lvl: ' + str(df.at[x, 'level']) + '\n' + '#Russian #Python #tweepy #learnpython #pythonprogramming'))
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

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(str(printer(listFunction())))
