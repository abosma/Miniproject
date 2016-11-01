from tkinter import *
import time
from TwitterAPI import TwitterAPI
import pyowm
import threading

tweets = "Geen tweets"

api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5",
                 "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")
owm = pyowm.OWM("a40051c6d53e900889105abcdc376832")

def guiStart():
    root = Tk()  # GUI   #log erbij if time premits

    root.title("DisplayTweetsAndWeather")  # GUI NAME

    tweetsString = StringVar();
    tweetsString.set(tweets);


    # Labels
    thelabel = Label(root, textvariable=tweetsString)

    # frames
    topFrame = Frame(root)
    bottomFrame = Frame(root)

    # packs
    thelabel.pack()

    topFrame.pack()
    bottomFrame.pack(side=BOTTOM)


    def checkChanges():

        global tweets
        tweets = "testtesttest0"
        tweetsString = tweets
        root.after(2000, checkChanges)


    root.after(2000, checkChanges)
    root.mainloop();

def getTweets():
    starttime = time.time()  # start clock

    while True:
        try:
            r = api.request('statuses/home_timeline',
                            {'count': 5})  # api reqeust take from twitter last 5 tweets (json file)
            print(r.status_code);
            for item in r.get_iterator():  # per tweet doe X
                if 'text' in item:  # Als een variable 'text' text dan kijkt hij naar de lengte van de lijst 5
                    if len(tweets) < 5:  # check if 5-
                        tweets.append(item["text"])  # put tweets in list
                        print(item["text"]);  # print list
                    else:  # if ==5
                        if item["text"] in tweets:  # if tweet been here before
                            observation = owm.weather_at_place("Utrecht,NL")  # show weather
                            w = observation.get_weather()
                            weatherCelcius = w.get_temperature('celsius')
                            weatherWindsnelheid = w.get_wind()
                            print("Tempratuur in Utrecht   : °C " + str(weatherCelcius.get("temp")))
                            print("Windsnelheid in Utrecht : " + str(weatherWindsnelheid.get("speed")) + " " + str(
                                weatherWindsnelheid("deg") + "°"))
                        else:
                            tweets.pop(0);  # if tweets is not in list before then remove first tweet
                            tweets.append(item["text"])  # add new tweet
                            for tweet in tweets:
                                print(tweet);  # print all tweets
        except Exception as e:
            print(e);  # erorr handling

        time.sleep(
            60.0 - ((time.time() - starttime) % 60.0))  # wait 60s or else we get blocked max 15 reqeusts per 15 mins

getTweetsThread = threading.Thread(name='getTweetsThread', target=getTweets)
guiThread = threading.Thread(name='guiStartThread', target=guiStart)

getTweetsThread.start()
guiThread.start()